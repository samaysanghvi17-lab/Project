<?php
/**
 * Neo Impex quote-request handler.
 * Receives the website lead form (POST, multipart) and emails it to the sales inbox.
 * No credentials are stored here. Mail is sent with PHP mail() from the hosting account.
 */
declare(strict_types=1);

const TO_EMAIL   = 'kartik@neoimpex.com';
const FROM_EMAIL = 'no-reply@neoimpexglobal.com';
const FROM_NAME  = 'Neo Impex Website';
const MAX_FILE   = 8 * 1024 * 1024;
const MAX_PER_HOUR = 6;
const ALLOWED_EXT = ['pdf', 'xls', 'xlsx', 'csv', 'doc', 'docx', 'png', 'jpg', 'jpeg', 'dwg', 'dxf', 'zip'];

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function respond(int $code, array $body): void {
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, ['ok' => false, 'error' => 'Method not allowed.']);
}

function clean(string $key, int $max = 500): string {
    $v = isset($_POST[$key]) ? (string)$_POST[$key] : '';
    $v = trim(str_replace(["\r", "\0"], '', $v));
    if (function_exists('mb_substr')) { $v = mb_substr($v, 0, $max); } else { $v = substr($v, 0, $max); }
    return $v;
}
function oneline(string $v): string { return trim(preg_replace('/[\r\n\t]+/', ' ', $v) ?? ''); }

// --- spam checks: honeypot and minimum fill time (silently accept so bots learn nothing) ---
if (clean('website', 200) !== '') { respond(200, ['ok' => true]); }
$started = (int)clean('started', 20);
if ($started > 0 && (time() * 1000 - $started) < 2500) { respond(200, ['ok' => true]); }

// --- required fields ---
$name  = oneline(clean('name', 120));
$email = oneline(clean('email', 200));
if ($name === '') { respond(422, ['ok' => false, 'error' => 'Please enter your name.']); }
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { respond(422, ['ok' => false, 'error' => 'Please enter a valid email address.']); }

// --- simple per-IP rate limit ---
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$ip = trim(explode(',', (string)$ip)[0]);
$rlFile = sys_get_temp_dir() . '/neo_rl_' . md5($ip);
$now = time(); $hits = [];
if (is_readable($rlFile)) {
    $hits = array_filter(array_map('intval', explode(',', (string)@file_get_contents($rlFile))), fn($t) => $t > $now - 3600);
}
if (count($hits) >= MAX_PER_HOUR) { respond(429, ['ok' => false, 'error' => 'Too many requests. Please email kartik@neoimpex.com.']); }
$hits[] = $now; @file_put_contents($rlFile, implode(',', $hits));

// --- collect fields ---
$fields = [
    'Name' => $name,
    'Company' => oneline(clean('company', 160)),
    'Email' => $email,
    'Phone / WhatsApp' => oneline(clean('phone', 60)),
    'Country' => oneline(clean('country', 80)),
    'Product' => oneline(clean('product', 120)),
    'Material / grade' => oneline(clean('material', 200)),
    'Size, class / schedule, qty' => oneline(clean('size', 300)),
    'Delivery port or ZIP' => oneline(clean('delivery', 160)),
];
$message = clean('message', 4000);

$meta = [
    'Page' => oneline(clean('page', 300)),
    'Referrer' => oneline(clean('referrer', 300)),
    'utm_source' => oneline(clean('utm_source', 120)),
    'utm_medium' => oneline(clean('utm_medium', 120)),
    'utm_campaign' => oneline(clean('utm_campaign', 160)),
    'utm_term' => oneline(clean('utm_term', 160)),
    'gclid' => oneline(clean('gclid', 200)),
    'IP' => $ip,
    'Browser' => oneline(substr((string)($_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 200)),
    'Received (UTC)' => gmdate('Y-m-d H:i:s'),
];

$lines = [];
foreach ($fields as $k => $v) { if ($v !== '') { $lines[] = $k . ': ' . $v; } }
if ($message !== '') { $lines[] = ''; $lines[] = "Message:\n" . $message; }
$lines[] = ''; $lines[] = '--- Lead source ---';
foreach ($meta as $k => $v) { if ($v !== '') { $lines[] = $k . ': ' . $v; } }
$text = implode("\n", $lines);

// --- optional attachment (BOQ / drawing) ---
$attachment = null;
if (!empty($_FILES['boq']) && is_array($_FILES['boq']) && ($_FILES['boq']['error'] ?? UPLOAD_ERR_NO_FILE) === UPLOAD_ERR_OK) {
    $f = $_FILES['boq'];
    $ext = strtolower(pathinfo((string)$f['name'], PATHINFO_EXTENSION));
    if (!in_array($ext, ALLOWED_EXT, true)) { respond(422, ['ok' => false, 'error' => 'That file type is not accepted. Please attach a PDF, Excel, Word, image or drawing file.']); }
    if ((int)$f['size'] > MAX_FILE) { respond(422, ['ok' => false, 'error' => 'The file is larger than 8 MB. Please email it to kartik@neoimpex.com.']); }
    if (is_uploaded_file((string)$f['tmp_name'])) {
        $attachment = ['name' => preg_replace('/[^A-Za-z0-9._-]+/', '_', basename((string)$f['name'])), 'data' => (string)file_get_contents((string)$f['tmp_name'])];
    }
}

// --- build the email ---
$subject = 'Website enquiry: ' . ($fields['Product'] !== '' ? $fields['Product'] : 'Quote request') . ' - ' . $name . ($fields['Country'] !== '' ? ' (' . $fields['Country'] . ')' : '');
$encSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$boundary = 'neo_' . bin2hex(random_bytes(12));
$headers = [
    'From: ' . FROM_NAME . ' <' . FROM_EMAIL . '>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'MIME-Version: 1.0',
    'X-Mailer: neoimpex-website',
];
if ($attachment) {
    $headers[] = 'Content-Type: multipart/mixed; boundary="' . $boundary . '"';
    $body = "--$boundary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n"
          . chunk_split(base64_encode($text))
          . "--$boundary\r\nContent-Type: application/octet-stream; name=\"" . $attachment['name'] . "\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"" . $attachment['name'] . "\"\r\n\r\n"
          . chunk_split(base64_encode($attachment['data']))
          . "--$boundary--";
} else {
    $headers[] = 'Content-Type: text/plain; charset=UTF-8';
    $headers[] = 'Content-Transfer-Encoding: base64';
    $body = chunk_split(base64_encode($text));
}

// --- keep a private copy outside the web root when possible (not exposed to visitors) ---
$logDir = dirname(__DIR__, 2) . '/enquiries';
if (@is_dir($logDir) || @mkdir($logDir, 0750, true)) {
    $row = array_merge([gmdate('c')], array_values($fields), [str_replace(["\r", "\n"], ' ', $message)], array_values($meta));
    $fh = @fopen($logDir . '/enquiries.csv', 'ab');
    if ($fh) { @fputcsv($fh, $row); @fclose($fh); }
}

if (getenv('NEO_MAIL_DRY_RUN') === '1') {
    @file_put_contents(sys_get_temp_dir() . '/neo_last_mail.txt', "Subject: $subject\n" . implode("\n", $headers) . "\n\n" . $text);
    respond(200, ['ok' => true, 'dry_run' => true]);
}

$sent = @mail(TO_EMAIL, $encSubject, $body, implode("\r\n", $headers), '-f' . FROM_EMAIL);
if (!$sent) { respond(500, ['ok' => false, 'error' => 'Sorry, we could not send your enquiry. Please email kartik@neoimpex.com or use WhatsApp.']); }
respond(200, ['ok' => true]);
