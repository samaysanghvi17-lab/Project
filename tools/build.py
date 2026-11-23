# -*- coding: utf-8 -*-
"""Static site builder for neoimpexglobal.com.  Run from the repository root:  python3 tools/build.py"""
import csv, html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_products import FITTINGS, FITTINGS_ORDER, FLANGES, FLANGES_ORDER
from content_materials import MATERIALS, MATERIALS_ORDER
from content_certs import CERTS
from content_pages import EXPORT, EXPORT_HUB, DATASHEETS, BLOG, PIPE, ELBOW_SIZES, DS_NOTE

SITE = "https://neoimpexglobal.com"
TODAY = "2026-11-22"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OG = SITE + "/assets/img/og-image.jpg"
PHONE_WA = "919316631458"
E = html.escape

GENERATED_DIRS = ["buttweld-fittings", "flanges", "data-sheets", "export", "blog", "request-a-quote", "privacy-policy", "certifications", "about", "contact"]
PAGES = []      # (url, title, description, primary keyword, secondary keywords)
WARN = []

# ----------------------------------------------------------------- helpers
def jd(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"

PIC_SKIP = {"favicon", "apple-touch-icon", "og-image"}
def picturize(html_text):
    def sub(m):
        tag, stem, ext = m.group(0), m.group(1), m.group(2)
        if stem in PIC_SKIP: return tag
        return (f'<picture><source type="image/avif" srcset="/assets/img/{stem}.avif"><source type="image/webp" srcset="/assets/img/{stem}.webp">{tag}</picture>')
    return re.sub(r'<img [^>]*src="/assets/img/([\w-]+)\.(jpg|png)"[^>]*>', sub, html_text)

def write(url, content):
    content = picturize(content)
    path = os.path.join(ROOT, url.strip("/"), "index.html") if url != "/" else os.path.join(ROOT, "index.html")
    if url == "/404.html":
        path = os.path.join(ROOT, "404.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def check(url, title, desc):
    if len(title) > 65: WARN.append(f"title {len(title)} chars: {url}")
    if not (70 <= len(desc) <= 155): WARN.append(f"description {len(desc)} chars: {url}")

LOGO = '<img src="/assets/img/logo-light.png" alt="Neo Impex \u2013 Connecting Pipeline" width="128" height="38">'
LOGO_L = '<img src="/assets/img/logo-light.png" alt="Neo Impex – Connecting Pipeline" width="196" height="58" loading="lazy">'

def fp(slug): return f"/buttweld-fittings/{slug}/"
def flp(slug): return f"/flanges/{slug}/"
def fmat(slug): return f"/buttweld-fittings/materials/{slug}/"
def flmat(slug): return f"/flanges/materials/{slug}/"

# ----------------------------------------------------------------- schematic drawings
OUT, FILL = "#0a0b0e", "#e4e5e8"
def tube(d, w=34):
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w + 5}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{FILL}" stroke-width="{w}" stroke-linejoin="round"/>')
def poly(d):
    return f'<path d="{d}" fill="{FILL}" stroke="{OUT}" stroke-width="3" stroke-linejoin="round"/>'
def holes(n, r_bc, r_h, cx=120, cy=80):
    import math
    out = ""
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        out += f'<circle cx="{cx + r_bc * math.cos(a):.1f}" cy="{cy + r_bc * math.sin(a):.1f}" r="{r_h}" fill="#fff" stroke="{OUT}" stroke-width="2"/>'
    return out
def face(bore=26, extra=""):
    b = f'<circle cx="120" cy="80" r="{bore}" fill="#fff" stroke="{OUT}" stroke-width="3"/>' if bore else ""
    return (f'<circle cx="120" cy="80" r="62" fill="{FILL}" stroke="{OUT}" stroke-width="3"/>' + extra + b + holes(8, 49, 5.5))
def art(kind):
    s = {
     "elbow": tube("M48,150 L48,96 A54,54 0 0 1 102,42 L204,42"),
     "tee": tube("M20,58 L220,58") + tube("M120,58 L120,148"),
     "cross": tube("M20,80 L220,80") + tube("M120,12 L120,148"),
     "reducer": poly("M18,30 L96,30 L158,52 L222,52 L222,108 L158,108 L96,130 L18,130 Z") + f'<path d="M96,30 L96,130 M158,52 L158,108" stroke="{OUT}" stroke-width="2" fill="none"/>',
     "cap": poly("M18,36 L128,36 Q214,36 214,80 Q214,124 128,124 L18,124 Z") + f'<path d="M128,36 L128,124" stroke="{OUT}" stroke-width="2" fill="none"/>',
     "stub": poly("M18,50 L128,50 L128,32 L152,32 L152,128 L128,128 L128,110 L18,110 Z"),
     "return": tube("M52,34 L112,34 A46,46 0 0 1 112,126 L52,126", 26),
     "bend": tube("M34,144 L34,124 A112,112 0 0 1 146,32 L214,32"),
     "weldneck": poly("M118,22 L142,22 L142,138 L118,138 Z") + poly("M118,52 L70,66 L20,66 L20,94 L70,94 L118,108 Z") + f'<path d="M20,80 L142,80" stroke="{OUT}" stroke-width="2" stroke-dasharray="5 5"/>',
     "lwn": poly("M186,22 L210,22 L210,138 L186,138 Z") + poly("M186,52 L120,64 L16,64 L16,96 L120,96 L186,108 Z") + f'<path d="M16,80 L210,80" stroke="{OUT}" stroke-width="2" stroke-dasharray="5 5"/>',
     "slipon": face(26, f'<circle cx="120" cy="80" r="37" fill="none" stroke="{OUT}" stroke-width="2"/>'),
     "blind": face(0, f'<circle cx="120" cy="80" r="37" fill="none" stroke="{OUT}" stroke-width="2"/>'),
     "socket": face(16, f'<circle cx="120" cy="80" r="28" fill="none" stroke="{OUT}" stroke-width="2" stroke-dasharray="4 3"/>'),
     "threaded": face(24, f'<circle cx="120" cy="80" r="31" fill="none" stroke="{OUT}" stroke-width="5" stroke-dasharray="2 3"/>'),
     "lap": face(34, f'<circle cx="120" cy="80" r="42" fill="none" stroke="{OUT}" stroke-width="2"/>'),
     "rtj": face(26, f'<circle cx="120" cy="80" r="33" fill="none" stroke="{OUT}" stroke-width="2"/><circle cx="120" cy="80" r="38" fill="none" stroke="{OUT}" stroke-width="2"/>'),
    }[kind]
    return f'<svg viewBox="0 0 240 160" role="img" aria-label="{E(kind)} drawing" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

# ----------------------------------------------------------------- navigation and chrome
def nav_html(active):
    active = {"ds": "res", "blog": "res"}.get(active, active)
    def a(href, text, key=None):
        cls = ' class="active"' if key and key == active else ""
        return f'<a href="{href}"{cls}>{text}</a>'
    fit = "".join(f'<a href="{fp(s)}">{E(FITTINGS[s]["name"])}</a>' for s in FITTINGS_ORDER)
    fl = "".join(f'<a href="{flp(s)}">{E(FLANGES[s]["name"])}</a>' for s in FLANGES_ORDER)
    return f'''<nav class="main" id="nav" aria-label="Primary">
      <div class="has-sub">{a("/buttweld-fittings/", "Buttweld Fittings", "fit")}<button class="subtoggle" type="button" aria-label="Show Buttweld fittings menu" aria-expanded="false"></button><div class="sub"><span class="grp">Types</span>{fit}<hr><a href="/buttweld-fittings/#materials">By material →</a></div></div>
      <div class="has-sub">{a("/flanges/", "Flanges", "fl")}<button class="subtoggle" type="button" aria-label="Show Flanges menu" aria-expanded="false"></button><div class="sub"><span class="grp">Types</span>{fl}<hr><a href="/flanges/#materials">By material →</a></div></div>
      <div class="has-sub">{a("/export/", "Export", "exp")}<button class="subtoggle" type="button" aria-label="Show Export menu" aria-expanded="false"></button><div class="sub"><a href="/export/usa/">USA</a><a href="/export/canada/">Canada</a></div></div>
      <div class="has-sub">{a("/data-sheets/", "Resources", "res")}<button class="subtoggle" type="button" aria-label="Show Resources menu" aria-expanded="false"></button><div class="sub"><a href="/data-sheets/">Data sheets</a><a href="/data-sheets/pipe-schedule-chart/">Pipe schedule chart</a><a href="/blog/">Blog</a></div></div>
      <div class="has-sub">{a("/about/", "Company", "co")}<button class="subtoggle" type="button" aria-label="Show Company menu" aria-expanded="false"></button><div class="sub"><a href="/about/">About us</a><a href="/certifications/">Certifications</a><a href="/contact/">Contact</a></div></div>
    </nav>'''

def header(active):
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
    <a class="brand" href="/" aria-label="Neo Impex – home">{LOGO}</a>
    {nav_html(active)}
    <a class="btn btn-blue head-cta" href="/request-a-quote/">Request a quote</a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
</div></header>'''

def footer():
    return f'''<footer><div class="wrap">
  <div class="foot">
    <div>{LOGO_L}<address><span><strong style="color:#fff">Neo Impex Stainless Pvt. Ltd.</strong></span>
      <span>Works: Plot No. C1/B-270, GIDC Por, Ramangamdi, Vadodara 391243, Gujarat, India</span>
      <span>Office: 709, Prasad Chamber, Tata Road No. 2, Charni Road (East), Mumbai 400004, India</span>
      <span><a href="mailto:kartik@neoimpexglobal.com">kartik@neoimpexglobal.com</a><br><a href="https://wa.me/{PHONE_WA}">WhatsApp +91 93166 31458</a></span></address></div>
    <div><p class="fh">Products</p><ul><li><a href="/buttweld-fittings/">Buttweld fittings</a></li><li><a href="/flanges/">Flanges</a></li><li><a href="/buttweld-fittings/#materials">Fittings by material</a></li><li><a href="/flanges/#materials">Flanges by material</a></li><li><a href="/data-sheets/">Data sheets</a></li></ul></div>
    <div><p class="fh">Export</p><ul><li><a href="/export/usa/">USA</a></li><li><a href="/export/canada/">Canada</a></li><li><a href="/request-a-quote/">Request a quote</a></li></ul></div>
    <div><p class="fh">Company</p><ul><li><a href="/about/">About us</a></li><li><a href="/certifications/">Certifications</a></li><li><a href="/contact/">Contact</a></li><li><a href="/blog/">Blog</a></li><li><a href="/privacy-policy/">Privacy policy</a></li></ul></div>
  </div>
  <div class="legal"><span>\u00a9 2026 Neo Impex Stainless Pvt. Ltd. \u00b7 neoimpexglobal.com</span><span>Established 2005 \u00b7 Vadodara, India</span></div>
</div></footer>
<aside class="shortcuts" aria-label="Quick contact">
<a class="wa-float" href="https://wa.me/{PHONE_WA}?text=Hello%20Neo%20Impex%2C%20I%20would%20like%20to%20send%20a%20BOQ." target="_blank" rel="noopener" aria-label="Chat with Neo Impex on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 20.5l1.7-5.2A8.5 8.5 0 1 1 21 11.5z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1.2-1.6-2.2-1.1-.9.9c-1-.4-2-1.4-2.4-2.4l.9-.9L11 7.8z"/></svg><span>WhatsApp</span></a>
<div class="mbar"><a class="mq" href="/request-a-quote/">Request a quote</a><a class="mw" href="https://wa.me/{PHONE_WA}?text=Hello%20Neo%20Impex%2C%20I%20would%20like%20to%20send%20a%20BOQ." target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 20.5l1.7-5.2A8.5 8.5 0 1 1 21 11.5z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1.2-1.6-2.2-1.1-.9.9c-1-.4-2-1.4-2.4-2.4l.9-.9L11 7.8z"/></svg><span>WhatsApp</span></a></div>
</aside>
<script src="/assets/js/config.js"></script><script src="/assets/js/site.js" defer></script>'''

ORG_ID = SITE + "/#organization"
# The single number shown on every page; the schema below lists exactly the same one.
PHONES = [("+91-93166-31458", "WhatsApp / sales")]
SAMEAS = []      # add real profile URLs here (LinkedIn company page, IndiaMART, etc.); omitted from schema while empty
AUTHOR = {"name": "", "jobTitle": "", "url": ""}   # set a real person to credit blog posts; falls back to the company while empty

ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": ORG_ID, "name": "Neo Impex Stainless Pvt. Ltd.", "alternateName": "Neo Impex", "url": SITE + "/",
       "logo": SITE + "/assets/img/logo.png", "image": SITE + "/assets/img/works-vadodara.jpg", "foundingDate": "2005-04-04", "legalName": "Neo Impex Stainless Pvt. Ltd.",
       "email": "kartik@neoimpexglobal.com",
       "address": {"@type": "PostalAddress", "streetAddress": "Plot No. C1/B-270, GIDC Por, Ramangamdi", "addressLocality": "Vadodara", "postalCode": "391243", "addressRegion": "Gujarat", "addressCountry": "IN"},
       "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": ph, "name": label, "email": "kartik@neoimpexglobal.com", "areaServed": ["US", "CA"], "availableLanguage": ["English"]} for ph, label in PHONES]}
if SAMEAS: ORG["sameAs"] = SAMEAS
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Neo Impex", "inLanguage": "en-US", "publisher": {"@id": ORG_ID}}

def head(title, desc, url, schemas=(), image=OG, noindex=False, extra_css=""):
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    canon = SITE + url if url != "/404.html" else SITE + "/"
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0a0b0e">
<link rel="canonical" href="{canon}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="Neo Impex"><meta property="og:locale" content="en_US">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
{jd(ORG)}{"".join(jd(s) for s in schemas)}
<noscript><style>.reveal{{opacity:1;transform:none}}</style></noscript>
</head>'''

def crumbs(items):
    lis = ""
    sch = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": []}
    for i, (name, url) in enumerate(items, 1):
        if url:
            lis += f'<li><a href="{url}">{E(name)}</a></li>'
            sch["itemListElement"].append({"@type": "ListItem", "position": i, "name": name, "item": SITE + url})
        else:
            lis += f'<li aria-current="page">{E(name)}</li>'
            sch["itemListElement"].append({"@type": "ListItem", "position": i, "name": name})
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{lis}</ol></div></nav>', sch

def faq_block(faqs, heading="Frequently asked questions"):
    items = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in faqs)
    sch = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    return f'<h2 class="h2">{E(heading)}</h2><div class="faq">{items}</div>', sch

def cta_band(title="Send your BOQ. Get a quote in 24 business hours.", text="Price, lead time and delivery terms for the USA and Canada, with EN 10204 3.1 certificates.", product=""):
    q = "/request-a-quote/" + (f"?product={E(product)}" if product else "")
    return f'''<div class="cta-band reveal"><div><h2>{E(title)}</h2><p>{E(text)}</p></div>
  <div class="cta"><a class="btn btn-gold" href="{q}">Request a quote</a></div></div>'''

def quote_form(uid, product_default="", compact=False, title="Request a quote", hint=None, heading_tag="h3"):
    hint = hint or ("Reply with price and lead time within 24 business hours. Attach your BOQ or drawing if you have one." if not compact else "We reply within 24 business hours.")
    opts_p = "".join(f'<option{" selected" if o == product_default else ""}>{o}</option>' for o in ["Buttweld fittings", "Flanges", "Buttweld fittings and flanges", "Data sheet / catalogue", "Other"])
    countries = ["United States", "Canada", "Other"]
    opts_c = "".join(f"<option>{c}</option>" for c in countries)
    hidden = "".join(f'<input type="hidden" name="{n}">' for n in ["page", "referrer", "utm_source", "utm_medium", "utm_campaign", "utm_term", "gclid", "started"])
    hp = '<div class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>'
    full = "" if compact else f'''
      <div class="field"><label for="{uid}-material">Material / grade</label><input id="{uid}-material" name="material" placeholder="e.g. A403 WP316L, A105"></div>
      <div class="field"><label for="{uid}-size">Size, class / schedule, qty</label><input id="{uid}-size" name="size" placeholder="e.g. 6&quot; Cl.300 WNRF Sch 40 × 40"></div>
      <div class="field full"><label for="{uid}-delivery">Delivery port, ZIP or postal code</label><input id="{uid}-delivery" name="delivery" placeholder="e.g. Houston 77029 or Vancouver V6B"></div>'''
    boq = "" if compact else f'<div class="field full"><label for="{uid}-boq">Attach BOQ or drawing <span class="opt">(PDF, Excel, Word, image; max 8 MB)</span></label><input id="{uid}-boq" type="file" name="boq" accept=".pdf,.xls,.xlsx,.csv,.doc,.docx,.png,.jpg,.jpeg,.dwg,.dxf,.zip"></div>'
    return f'''<form class="enq lead-form{" inline" if compact else ""}" id="{uid}" method="post" action="/api/enquiry.php" enctype="multipart/form-data" novalidate>
      <{heading_tag}>{E(title)}</{heading_tag}><p class="hint">{E(hint)}</p>
      <div class="field"><label for="{uid}-name">Name</label><input id="{uid}-name" name="name" autocomplete="name" required><span class="msg" aria-live="polite"></span></div>
      <div class="field"><label for="{uid}-company">Company</label><input id="{uid}-company" name="company" autocomplete="organization"></div>
      <div class="field"><label for="{uid}-email">Email</label><input id="{uid}-email" name="email" type="email" autocomplete="email" required><span class="msg" aria-live="polite"></span></div>
      <div class="field"><label for="{uid}-phone">Phone / WhatsApp</label><input id="{uid}-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="{uid}-country">Country</label><select id="{uid}-country" name="country" autocomplete="country-name">{opts_c}</select></div>
      <div class="field"><label for="{uid}-product">Product</label><select id="{uid}-product" name="product">{opts_p}</select></div>{full}
      <div class="field full"><label for="{uid}-message">Message</label><textarea id="{uid}-message" name="message" placeholder="Tests, certificates, delivery date…"></textarea></div>{boq}
      {hidden}{hp}
      <div class="actions"><button class="btn btn-blue" type="submit">Send enquiry</button><button class="btn btn-ghost-dark" type="button" data-wa>Send on WhatsApp</button></div>
      <p class="note">We use your details only to reply to this enquiry. See our <a href="/privacy-policy/">privacy policy</a>.</p>
      <p class="status" role="status" hidden></p>
      <noscript><p class="note">JavaScript is needed to send this form. Please email kartik@neoimpexglobal.com instead.</p></noscript>
    </form>'''

def lcard(href, name, short, svg):
    return f'<a class="lcard" href="{href}"><div class="art">{svg}</div><h3>{E(name)}</h3><p>{E(short)}</p><span class="go">View</span></a>'

def page(url, title, desc, body, active="", schemas=(), kw=None, image=OG, noindex=False, theme=""):
    check(url, title, desc)
    out = head(title, desc, url, schemas, image, noindex) + f"\n<body{(' class=\"' + theme + '\"') if theme else ''}>\n{header(active)}\n{body}\n{footer()}\n</body>\n</html>\n"
    write(url, out)
    if not noindex and url != "/404.html":
        PAGES.append((url, title, desc, kw[0] if kw else "", "; ".join(kw[1]) if kw else ""))

def phero(h1, lede, eyebrow, chips=(), visual="", cta=True, product="", single=False):
    ch = f'<div class="chips">{"".join(f"<span>{E(c)}</span>" for c in chips)}</div>' if chips else ""
    c = ""
    if cta:
        c = f'<div class="cta"><a class="btn btn-gold" href="/request-a-quote/{"?product=" + E(product) if product else ""}">Request a quote</a></div>'
    vis = f'<div class="pvisual{" art" if "<svg" in visual else ""}">{visual}</div>' if visual else ""
    return f'''<section class="phero{" single" if single or not visual else ""}"><div class="wrap"><div><p class="eyebrow gold">{E(eyebrow)}</p><h1>{E(h1)}</h1><p class="lede">{E(lede)}</p>{ch}{c}</div>{vis}</div></section>'''

def photo(name, alt, w=720, h=720):
    return f'<img src="/assets/img/{name}" alt="{E(alt)}" width="{w}" height="{h}">'

def spec_table(rows):
    return '<div class="tblwrap"><table class="spectbl"><tbody>' + "".join(f"<tr><th scope='row'>{E(k)}</th><td>{E(v)}</td></tr>" for k, v in rows) + "</tbody></table></div>"

# photo overrides: product slug -> (file, alt)
FIT_PHOTO = {"elbows": ("elbows-90-pair.jpg", "Two buttweld 90 degree elbows"), "tees": ("tees.jpg", "Polished stainless steel buttweld tees in five sizes"),
             "reducers": ("reducer-ecc.jpg", "Eccentric buttweld reducer marked ASTM A403"), "caps": ("cap.jpg", "Stainless steel buttweld pipe end cap"),
             "stub-ends": ("stub-end.jpg", "Long pattern stainless steel stub end"), "return-bends": ("return-bend.jpg", "180 degree stainless steel return bend")}
FL_PHOTO = {"weld-neck": ("weld-neck.jpg", "Black forged weld neck flange"), "slip-on": ("slip-on.jpg", "Black forged slip-on flange"),
            "blind": ("blind.jpg", "Black forged blind flange"), "threaded": ("threaded.jpg", "Stainless steel threaded flange with four bolt holes")}
FIT_ART = {"elbows": "elbow", "tees": "tee", "reducers": "reducer", "caps": "cap", "stub-ends": "stub", "crosses": "cross", "return-bends": "return", "pipe-bends": "bend"}
FL_ART = {"weld-neck": "weldneck", "slip-on": "slipon", "blind": "blind", "socket-weld": "socket", "threaded": "threaded", "lap-joint": "lap", "ring-type-joint": "rtj", "long-weld-neck": "lwn"}

def mat_visual(slug, fam):
    ph = {("ss-304-304l", "fit"): ("stainless-fittings-group.jpg", "Stainless steel buttweld fittings"), ("ss-316-316l", "fit"): ("stainless-fittings-group.jpg", "Stainless steel buttweld fittings"),
          ("ss-304-304l", "fl"): ("weld-neck-ss.jpg", "Stainless steel weld neck flange"), ("ss-316-316l", "fl"): ("weld-neck-ss.jpg", "Stainless steel weld neck flange"),
          ("carbon-steel", "fit"): ("factory-tees-stock.jpg", "Carbon steel buttweld tees and elbows in stock at our works"), ("carbon-steel", "fl"): ("flanges-packed-blue.jpg", "Forged weld neck flanges packed with protective covers")}
    if (slug, fam) in ph:
        f, a = ph[(slug, fam)]
        return photo(f, a, 1280, 850)
    label = MATERIALS[slug]["name"].split(" (")[0]
    return f'<div class="matcard"><span>{E(label)}</span></div>'

# ----------------------------------------------------------------- HOME
def build_home():
    title = "Buttweld Fittings & Flanges Manufacturer | USA, Canada"
    desc = "Neo Impex makes ASME B16.9 buttweld fittings and ASME B16.5/B16.47 flanges in India for US and Canadian buyers. 3.1 certificates, quote in 24 hours."
    mats = "".join(f'<article class="card reveal"><div class="kind">Material</div><h3>{E(MATERIALS[m]["name"])}</h3><p class="std">{E(MATERIALS[m]["short"])}</p><p class="std"><a href="{fmat(m)}">Buttweld fittings</a> · <a href="{flmat(m)}">Flanges</a></p></article>' for m in MATERIALS_ORDER)
    posts = "".join(f'<a class="bcard" href="/blog/{b["slug"]}/"><time datetime="{b["date"]}">{b["date"]}</time><h3>{E(b["title"])}</h3><p>{E(b["desc"])}</p><span class="go">Read</span></a>' for b in BLOG[-3:][::-1])
    body = f'''<main id="main">
<div class="hero nopanel" id="top">
  <div class="hero-main"><p class="topline">Established 2005 · ISO 9001:2015 certified</p>
    <h1><span>Buttweld fittings</span><span class="ln">&amp; flanges,</span><span class="ln">made to ship.</span></h1>
    <p class="lede">ASME B16.9 buttweld fittings and ASME B16.5 / B16.47 flanges for US and Canadian distributors, fabricators and contractors. Made in Vadodara, India, with EN 10204 3.1 certificates.</p>
    <div class="cta"><a class="btn btn-gold" href="/request-a-quote/">Get a quote in 24 hours</a></div></div>
</div>
<section class="orbit-sec" aria-label="Product range"><div class="wrap"><div class="sec-head"><p class="eyebrow">Product range</p><h2>Our range ↳ in motion</h2></div></div>
  <div class="orbit" role="region" aria-roledescription="carousel" aria-label="Neo Impex product range">
    <div class="orbit-stage" id="stage"><div class="orbit-ring" aria-hidden="true"><svg viewBox="0 0 1000 230" preserveAspectRatio="none"><ellipse cx="500" cy="115" rx="498" ry="113" fill="none" stroke="#f1dec0" stroke-opacity=".5" stroke-width="1.5" stroke-dasharray="3 9" vector-effect="non-scaling-stroke"/></svg></div>
      <div class="orbit-glow" aria-hidden="true"></div><img class="orbit-mark" src="/assets/img/mark-white.png" alt="" aria-hidden="true" width="220" height="168"></div>
    <div class="orbit-caption" id="caption" aria-live="off"><span class="tag" id="capTag">Flanges</span><h2 id="capTitle">Weld neck flanges</h2><p id="capText">WNRF and RTJ for high-pressure and critical service.</p>
      <a class="more" id="capLink" href="/flanges/weld-neck/">View product →</a><a class="more" id="capQuote" href="/request-a-quote/">Request a quote →</a></div>
    <div class="orbit-controls"><button class="arrow" id="prev" aria-label="Previous product">←</button><div class="dots" id="dots"></div><button class="arrow" id="next" aria-label="Next product">→</button></div>
  </div></section>
<section class="statement"><div class="wrap"><p class="big reveal">Neo Impex, established in 2005, makes buttweld fittings and forged flanges at its own works in Vadodara. We forge, form, bend, machine and test in house.</p>
  <p class="small reveal">We supply distributors, fabricators and contractors in the USA and Canada with heat-traceable EN 10204 3.1 certificates, MSS SP-25 marking and your choice of FOB, CIF or DAP terms.</p>
  <div class="stats reveal"><div><strong>2005</strong><span>Year established</span></div><div><strong>25+</strong><span>Countries supplied</span></div><div><strong>72″</strong><span>Largest welded fitting</span></div><div><strong>60″</strong><span>Largest forged flange</span></div></div></div></section>
<div class="supplied"><div class="wrap"><span class="lbl">Standards we make to</span><ul><li>ASME B16.9</li><li>ASME B16.5</li><li>ASME B16.47</li><li>MSS SP-43</li><li>MSS SP-25</li><li>EN 10204 3.1</li><li>NACE MR0175</li></ul></div></div>

<section class="certs"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">Certifications</p><h2>Certified and approved.</h2><p>ISO 9001:2015, PED 2014/68/EU material manufacturer approval, IBR workshop approval and Udyam registration. Each page shows the exact scope and validity.</p></div><div class="reveal">{certs_cards()}</div><p class="note"><a href="/certifications/">See every certificate and what each one covers →</a></p></div></section>

<section class="soft"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">Products</p><h2>Two product lines. Every size, class and grade.</h2><p>Buttweld fittings seamless to 24″ and welded to 72″. Forged flanges from ½″ to 60″ in Class 150 to 2500.</p></div>
  <div class="families">
   <article class="family reveal"><div class="photo"><img src="/assets/img/stainless-fittings-group.jpg" alt="Stainless steel buttweld fittings: reducer, return bend, tee, stub end, elbow and cap" loading="lazy" width="1280" height="850"></div><div class="body"><span class="spec">Seamless to 24″ · welded to 72″</span><h3>Buttweld fittings &amp; bends</h3><p>Elbows, tees, reducers, caps, stub ends, crosses, return bends, and 3D/5D/10D and piggable bends.</p><a class="btn btn-blue" href="/buttweld-fittings/">Explore buttweld fittings</a></div></article>
   <article class="family reveal"><div class="photo"><img src="/assets/img/flange-range.jpg" alt="Black forged flanges in four sizes" loading="lazy" width="1280" height="850"></div><div class="body"><span class="spec">½″ to 60″ · Class 150–2500</span><h3>Forged flanges</h3><p>Weld neck, slip-on, blind, socket weld, threaded, lap joint, RTJ and long weld neck – ASME B16.5 and B16.47.</p><a class="btn btn-blue" href="/flanges/">Explore flanges</a></div></article>
  </div></div></section>

<section class="tint" id="materials"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">Materials</p><h2>Every grade in your piping class.</h2><p>Stainless, duplex, super duplex, carbon, low-temperature, chrome-moly and nickel alloys, for both fittings and flanges.</p></div><div class="grid4">{mats}</div></div></section>

<section class="fullbleed" aria-label="Made in our own works"><img src="/assets/img/factory-tees-stock.jpg" alt="Carbon steel buttweld tees and elbows stacked at our works in Vadodara" loading="lazy" width="1280" height="960"><div class="wrap"><p class="eyebrow">Vadodara, India</p><h2><span>Made</span><span class="ln">in our</span><span class="ln">own works</span></h2><p class="lede">Forging, forming, bending, machining and testing at Vadodara. Buy from the manufacturer, not a trader.</p><div class="cta"><a class="btn btn-gold" href="/buttweld-fittings/">Buttweld fittings</a><a class="btn btn-ghost" href="/flanges/">Flanges</a></div></div><span class="cap">Stock at our works, Vadodara</span></section>

<section class="on-dark" id="export"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">Export</p><h2>Shipped to the USA and Canada with the right papers.</h2></div>
  <div class="export-grid"><article class="region reveal"><h3>United States</h3><p>Buttweld fittings and flanges for distributors and fabricators – inch sizes, MSS SP-25 marking, MTRs, DAP delivery.</p><div class="ports">{"".join(f"<span>{E(p)}</span>" for p in EXPORT["usa"]["ports"])}</div><p style="margin-top:18px"><a class="btn btn-gold" href="/export/usa/">Supplying the USA</a></p></article>
  <article class="region reveal"><h3>Canada</h3><p>Fittings and flanges for distributors, fabricators and contractors, including impact-tested material for cold-climate service.</p><div class="ports">{"".join(f"<span>{E(p)}</span>" for p in EXPORT["canada"]["ports"])}</div><p style="margin-top:18px"><a class="btn btn-gold" href="/export/canada/">Supplying Canada</a></p></article></div></div></section>

<section class="sand" id="process"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">How it works</p><h2>From enquiry to your port in four steps.</h2></div>
  <div class="steps reveal"><div class="step"><b>01</b><h3>Send your BOQ</h3><p>By form, email or WhatsApp.</p></div><div class="step"><b>02</b><h3>Get our quote</h3><p>Price, lead time and terms in 24 business hours.</p></div><div class="step"><b>03</b><h3>Production &amp; inspection</h3><p>Made, tested, inspected; documents shared before dispatch.</p></div><div class="step"><b>04</b><h3>Packed &amp; shipped</h3><p>FOB, CIF or DAP to your port or door.</p></div></div></div></section>

<section class="content"><div class="wrap"><div class="sec-head reveal"><p class="eyebrow">From the blog</p><h2>Guides for buyers.</h2></div><div class="bcards reveal">{posts}</div></div></section>

<section class="fullbleed slim" aria-label="Partner with us"><img src="/assets/img/flanges-packed-blue.jpg" alt="Forged weld neck flanges packed with blue protective covers" loading="lazy" width="1280" height="961"><div class="wrap"><h2><span>Partner</span><span class="ln">with us</span></h2></div><span class="cap">Forged weld neck flanges, packed for export</span></section>

<section class="on-dark" id="quote"><div class="wrap quote"><div class="reveal"><p class="eyebrow">Request a quote</p><h2>Have a BOQ ready?</h2><p class="sub">Send it now. Price, lead time and delivery terms within 24 business hours.</p>
  <ul class="checks"><li>ISO 9001:2015 certified · PED 2014/68/EU material manufacturer approval · IBR workshop approval</li><li>EN 10204 3.1 certificates with every order</li><li>Shipping to the USA and Canada</li></ul>
  </div>
  <div class="reveal">{quote_form("home", "Buttweld fittings and flanges")}</div></div></section>
</main>
<script src="/assets/js/orbit.js" defer></script>'''
    page("/", title, desc, body, schemas=[WEBSITE], kw=("buttweld fittings and flanges manufacturer", ["ASME B16.9 fittings exporter India", "flanges manufacturer India USA Canada"]))
    # the home page uses the /404-safe script order: orbit.js after site.js

# ----------------------------------------------------------------- HUBS
def build_hubs():
    # buttweld fittings hub
    cards = "".join(lcard(fp(s), FITTINGS[s]["name"], FITTINGS[s]["short"], art(FIT_ART[s])) for s in FITTINGS_ORDER)
    mcards = "".join(lcard(fmat(m), MATERIALS[m]["name"], MATERIALS[m]["short"], f'<span class="grade">{E(MATERIALS[m]["name"].split(" (")[0])}</span>') for m in MATERIALS_ORDER)
    faqs = [("What sizes of buttweld fittings do you make?", "Seamless fittings up to 24″ and welded fittings up to 72″, in standard schedules or to match your pipe wall."),
            ("Which standards do your buttweld fittings follow?", "ASME B16.9 and B16.28, MSS SP-43 for light-wall stainless, and EN 10253, with bevels to ASME B16.25 and marking to MSS SP-25."),
            ("Do you ship buttweld fittings to the USA and Canada?", "Yes. See our USA and Canada export pages for documents, ports and delivery terms.")]
    fq, fs = faq_block(faqs)
    cr, cs = crumbs([("Home", "/"), ("Buttweld fittings", None)])
    title = "Buttweld Fittings Manufacturer & Exporter | USA, Canada"
    desc = "ASME B16.9 buttweld fittings: elbows, tees, reducers, caps, stub ends, crosses and bends. Seamless to 24″, welded to 72″. Export to USA and Canada."
    body = f'''{cr}<main id="main">{phero("Buttweld Fittings: Manufacturer and Exporter", "Elbows, tees, reducers, caps, stub ends, crosses, return bends and pipe bends – seamless up to 24″ and welded up to 72″, in stainless, duplex, carbon, alloy and nickel alloys.", "Buttweld fittings", ["ASME B16.9 · B16.28", "MSS SP-43", "Seamless to 24″", "Welded to 72″"], photo("stainless-fittings-group.jpg", "Stainless steel buttweld fittings: reducer, return bend, tee, stub end, elbow and cap", 1280, 850), product="Buttweld fittings")}
<section class="content"><div class="wrap"><h2 class="h2">Choose a fitting</h2><div class="lcards">{cards}</div></div></section>
<section class="content alt" id="materials"><div class="wrap"><h2 class="h2">Buttweld fittings by material</h2><div class="lcards">{mcards}</div></div></section>
<section class="content"><div class="wrap two"><div><h2 class="h2">Specification at a glance</h2>{spec_table([("Standards", "ASME B16.9 · ASME B16.28 · MSS SP-43 · EN 10253 · bevels to ASME B16.25"), ("Size range", "Seamless up to 24″ · welded up to 72″ (NPS)"), ("Wall thickness", "Sch 5S to XXS, or to match your pipe"), ("Forms", "Elbows, tees, reducers, caps, stub ends, crosses, return bends, bends"), ("Bends", "3D, 5D, 10D, induction and piggable to R = 22D, up to 24″"), ("Marking and documents", "MSS SP-25 marking · heat traceable · EN 10204 3.1"), ("Welded seams", "100% radiography")])}
 <p class="note">See the <a href="/data-sheets/buttweld-fittings/">buttweld fittings data sheet</a> for more detail.</p></div>
 <aside class="side"><div class="panel blue"><h3>Need a quote?</h3><p>Send your bill of quantities and we reply with price and lead time within 24 business hours.</p><a class="btn btn-gold" href="/request-a-quote/?product=Buttweld%20fittings">Request a quote</a></div></aside></div></section>
<section class="content alt"><div class="wrap">{fq}</div></section>
<section class="content"><div class="wrap">{cta_band(product="Buttweld fittings")}</div></section></main>'''
    page("/buttweld-fittings/", title, desc, body, "fit", [cs, fs], kw=("buttweld fittings manufacturer", ["ASME B16.9 buttweld fittings exporter", "butt weld fittings supplier USA Canada"]))

    # flanges hub
    cards = "".join(lcard(flp(s), FLANGES[s]["name"], FLANGES[s]["short"], art(FL_ART[s])) for s in FLANGES_ORDER)
    mcards = "".join(lcard(flmat(m), MATERIALS[m]["name"], MATERIALS[m]["short"], f'<span class="grade">{E(MATERIALS[m]["name"].split(" (")[0])}</span>') for m in MATERIALS_ORDER)
    faqs = [("What sizes and classes of flanges do you make?", "Flanges from ½″ to 60″ in Class 150 to 2500, depending on size and the applicable standard (PN6 to PN100 for EN flanges)."),
            ("Which standards do your flanges follow?", "ASME B16.5 for NPS ½–24 and ASME B16.47 for NPS 26–60, plus EN 1092-1, BS 4504, BS 10 and DIN."),
            ("What facings can you supply?", "Raised face, ring type joint, flat face, tongue and groove, and male and female facings.")]
    fq, fs = faq_block(faqs)
    cr, cs = crumbs([("Home", "/"), ("Flanges", None)])
    title = "Forged Flanges Manufacturer & Exporter | USA, Canada"
    desc = "ASME B16.5 and B16.47 forged flanges: weld neck, slip-on, blind, socket weld, threaded, lap joint, RTJ. ½″ to 60″, Class 150–2500. Export to USA, Canada."
    body = f'''{cr}<main id="main">{phero("Forged Flanges: Manufacturer and Exporter", "Every flange type your piping needs – forged, machined and drilled in our Vadodara works, up to 60″ and Class 2500, in stainless, duplex, carbon, alloy and nickel alloys.", "Flanges", ["ASME B16.5 · B16.47", "½″ to 60″", "Class 150–2500"], photo("flange-range.jpg", "Black forged flanges in four sizes", 1280, 850), product="Flanges")}
<section class="content"><div class="wrap"><h2 class="h2">Choose a flange type</h2><div class="lcards">{cards}</div><p class="note">We also make spectacle blinds and spacers, orifice flanges, reducing flanges and nipoflanges. <a href="/request-a-quote/?product=Flanges">Ask for a quote</a>.</p></div></section>
<section class="content alt" id="materials"><div class="wrap"><h2 class="h2">Flanges by material</h2><div class="lcards">{mcards}</div></div></section>
<section class="content"><div class="wrap two"><div><h2 class="h2">Specification at a glance</h2>{spec_table([("Standards", "ASME B16.5 (NPS ½–24) · ASME B16.47 (NPS 26–60) · EN 1092-1 · BS 4504 · BS 10 · DIN"), ("Size range", "½″ to 60″"), ("Pressure class", "Class 150 to 2500 (size dependent) · PN6 to PN100"), ("Facings", "Raised face, RTJ, flat face, tongue and groove, male and female"), ("Types", "Weld neck, slip-on, blind, socket weld, threaded, lap joint, RTJ, long weld neck"), ("Marking and documents", "Heat number traceable · EN 10204 3.1")])}
 <p class="note">See the <a href="/data-sheets/flanges/">flanges data sheet</a> for more detail.</p></div>
 <aside class="side"><div class="panel blue"><h3>Need a quote?</h3><p>Send your flange list with size, class, facing and material and we reply within 24 business hours.</p><a class="btn btn-gold" href="/request-a-quote/?product=Flanges">Request a quote</a></div></aside></div></section>
<section class="content alt"><div class="wrap">{fq}</div></section>
<section class="content"><div class="wrap">{cta_band(product="Flanges")}</div></section></main>'''
    page("/flanges/", title, desc, body, "fl", [cs, fs], kw=("flanges manufacturer", ["ASME B16.5 flanges exporter", "forged flanges supplier USA Canada"]))

# ----------------------------------------------------------------- PRODUCT PAGES
def related_cards(slugs, family):
    out = ""
    for s in slugs:
        if s in FITTINGS and not (family == "fl" and s in FLANGES):
            out += lcard(fp(s), FITTINGS[s]["name"], FITTINGS[s]["short"], art(FIT_ART[s]))
        else:
            out += lcard(flp(s), FLANGES[s]["name"], FLANGES[s]["short"], art(FL_ART[s]))
    return out

def build_products():
    for fam, data, order, url_fn, phmap, artmap, hub, hubname, active, mats_fn in [
        ("fit", FITTINGS, FITTINGS_ORDER, fp, FIT_PHOTO, FIT_ART, "/buttweld-fittings/", "Buttweld fittings", "fit", fmat),
        ("fl", FLANGES, FLANGES_ORDER, flp, FL_PHOTO, FL_ART, "/flanges/", "Flanges", "fl", flmat)]:
        for slug in order:
            p = data[slug]; url = url_fn(slug)
            cr, cs = crumbs([("Home", "/"), (hubname, hub), (p["name"], None)])
            fq, fs = faq_block(p["faqs"])
            vis = photo(*phmap[slug]) if slug in phmap else art(artmap[slug])
            intro = "".join(f"<p>{E(t)}</p>" for t in p["intro"])
            feats = "".join(f"<li>{E(x)}</li>" for x in p["features"])
            apps = "".join(f"<li>{E(x)}</li>" for x in p["apps"])
            mlinks = "".join(f'<li><a href="{mats_fn(m)}">{E(MATERIALS[m]["name"])}</a></li>' for m in MATERIALS_ORDER)
            prod_schema = {"@context": "https://schema.org", "@type": "Product", "name": p["name"], "description": p["desc"], "brand": {"@type": "Brand", "name": "Neo Impex"},
                           "manufacturer": {"@type": "Organization", "name": "Neo Impex Stainless Pvt. Ltd."}, "image": SITE + "/assets/img/" + (phmap[slug][0] if slug in phmap else "og-image.jpg"),
                           "url": SITE + url, "category": hubname}
            body = f'''{cr}<main id="main">{phero(p["h1"], p["short"] + ". Manufactured in India and exported to the USA and Canada with EN 10204 3.1 certificates.", hubname, p["chips"], vis, product=p["name"])}
<section class="content"><div class="wrap two"><div class="prose reveal"><h2>Overview</h2>{intro}<h2>Features</h2><ul>{feats}</ul><h2>Typical applications</h2><ul>{apps}</ul></div>
 <aside class="side"><div class="panel"><h3>Available materials</h3><ul>{mlinks}</ul></div></aside></div></section>
<section class="content alt"><div class="wrap"><h2 class="h2">Specification</h2>{spec_table(p["spec"])}<p class="note">Reference information. Final dimensions and tolerances follow the applicable standard and your purchase order. <a href="/data-sheets/{"buttweld-fittings" if fam == "fit" else "flanges"}/">See the data sheet</a>.</p></div></section>
<section class="content"><div class="wrap">{fq}</div></section>
<section class="content alt"><div class="wrap"><div class="two"><div>{quote_form("q-" + slug, hubname, compact=True, title="Quote for " + p["name"].lower())}</div><div><h2 class="h2">Related products</h2><div class="lcards" style="grid-template-columns:repeat(1,1fr)">{related_cards(p["related"][:2], fam)}</div></div></div></div></section></main>'''
            page(url, p["title"], p["desc"], body, active, [cs, fs, prod_schema], kw=p["kw"], image=SITE + "/assets/img/" + (phmap[slug][0] if slug in phmap else "og-image.jpg"))

# ----------------------------------------------------------------- MATERIAL PAGES
def build_materials():
    for fam, hub, hubname, active, urlfn in [("fit", "/buttweld-fittings/", "Buttweld fittings", "fit", fmat), ("fl", "/flanges/", "Flanges", "fl", flmat)]:
        for slug in MATERIALS_ORDER:
            m = MATERIALS[slug]; url = urlfn(slug)
            spec = m["fit_spec"] if fam == "fit" else m["fl_spec"]
            text = m["fit_text"] if fam == "fit" else m["fl_text"]
            faqs = m["fit_faqs"] if fam == "fit" else m["fl_faqs"]
            noun = "buttweld fittings" if fam == "fit" else "flanges"
            nm = m["name"]
            title = f"{nm.split(' (')[0]} {noun.title()} | Manufacturer, USA, Canada"
            if len(title) > 66: title = f"{nm.split(' (')[0]} {noun.title()} Exporter | Neo Impex"
            desc = f"{nm.split(' (')[0]} {noun}: grades, ASTM specs and uses. Made in India with EN 10204 3.1 certificates. Exported to USA and Canada."
            cr, cs = crumbs([("Home", "/"), (hubname, hub), ("Materials", hub + "#materials"), (nm.split(" (")[0], None)])
            fq, fs = faq_block(faqs)
            rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in spec)
            props = ""
            if m["props"]:
                pr = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in m["props"])
                props = f'<h2 class="h2" style="margin-top:36px">Minimum strength (ASTM specification)</h2><div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable text"><thead><tr><th>Grade</th><th>Tensile strength</th><th>Yield strength</th></tr></thead><tbody>{pr}</tbody></table></div><p class="note">Minimum values from the ASTM specification, for reference. Actual values are on your EN 10204 3.1 certificate.</p>'
            uses = "".join(f"<li>{E(u)}</li>" for u in m["uses"])
            if fam == "fit":
                forms = "".join(f'<li><a href="{fp(s)}">{E(FITTINGS[s]["name"])}</a></li>' for s in FITTINGS_ORDER)
                forms_title = "Fitting types available in this material"
            else:
                forms = "".join(f'<li><a href="{flp(s)}">{E(FLANGES[s]["name"])}</a></li>' for s in FLANGES_ORDER)
                forms_title = "Flange types available in this material"
            others = "".join(f'<li><a href="{urlfn(o)}">{E(MATERIALS[o]["name"].split(" (")[0])}</a></li>' for o in MATERIALS_ORDER if o != slug)
            cross = (f'<a href="{flmat(slug)}">{nm.split(" (")[0]} flanges</a>' if fam == "fit" else f'<a href="{fmat(slug)}">{nm.split(" (")[0]} buttweld fittings</a>')
            body = f'''{cr}<main id="main">{phero(f"{nm.split(' (')[0]} {noun.title()}", m["short"] + ". " + ("Buttweld fittings" if fam == "fit" else "Forged flanges") + " exported from India to the USA and Canada.", f"{hubname} · material", [nm], mat_visual(slug, fam), product=f"{nm.split(' (')[0]} {noun}")}
<section class="content"><div class="wrap two"><div class="prose reveal"><h2>About {E(nm)}</h2><p>{E(m["blurb"])}</p><h2>{E(nm.split(" (")[0])} {noun}</h2><p>{E(text)}</p><h2>Typical uses</h2><ul>{uses}</ul><h2>Limits and selection notes</h2><p>{E(m["limits"])}</p><p>Also see {cross}.</p></div>
 <aside class="side"><div class="panel"><h3>{forms_title}</h3><ul>{forms}</ul></div><div class="panel"><h3>Other materials</h3><ul>{others}</ul></div></aside></div></section>
<section class="content alt"><div class="wrap"><h2 class="h2">Grades and specifications</h2><div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable text"><thead><tr><th>Grade</th><th>ASTM specification</th><th>UNS</th></tr></thead><tbody>{rows}</tbody></table></div>{props}</div></section>
<section class="content"><div class="wrap">{fq}</div></section>
<section class="content alt"><div class="wrap">{cta_band(product=f"{nm.split(' (')[0]} {noun}")}</div></section></main>'''
            if fam == "fit":
                pk, sk = m["kw"][0], m["kw"][1]
            else:
                pk, sk = m["kw"][1][0], [m["kw"][0]] + m["kw"][1][1:]
            page(url, title, desc, body, active, [cs, fs], kw=(pk, sk))

# ----------------------------------------------------------------- DATA SHEETS
def ds_hero(d, lede):
    return phero(d["h1"], lede, "Data sheet", [], "", cta=False, single=True)

def ds_toolbar():
    return '<div class="toolbar noprint"><button class="btn btn-blue" type="button" data-print>Print or save as PDF</button><a class="btn btn-ghost-dark" href="/request-a-quote/?product=Data%20sheet">Request a signed copy</a></div>'

def build_datasheets():
    # hub
    cr, cs = crumbs([("Home", "/"), ("Data sheets", None)])
    cards = "".join(f'<a class="lcard" href="/data-sheets/{k}/"><h3>{E(v["h1"])}</h3><p>{E(v["desc"])}</p><span class="go">Open</span></a>' for k, v in DATASHEETS.items())
    title = "Data Sheets and Charts | Buttweld Fittings, Flanges"
    desc = "Data sheets for Neo Impex buttweld fittings and flanges, plus a free pipe schedule chart. Print or save as PDF, or request a signed copy."
    body = f'''{cr}<main id="main">{phero("Data Sheets and Free Charts", "Specification sheets for buttweld fittings and flanges, and a pipe schedule chart with 90° elbow dimensions. Print them or save as PDF.", "Resources", cta=False, single=True)}
<section class="content"><div class="wrap"><h2 class="sr-only">Available data sheets</h2><div class="lcards three">{cards}</div><p class="note" style="margin-top:24px">Need a signed data sheet, sample material test certificate or full dimension chart? <a href="/request-a-quote/?product=Data%20sheet">Send us a request</a> and we reply within 24 business hours.</p></div></section></main>'''
    page("/data-sheets/", title, desc, body, "ds", [cs], kw=("buttweld fittings and flanges data sheets", ["ASME B16.9 specification", "pipe schedule chart"]))

    mat_rows_fit = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for m in MATERIALS_ORDER for a, b, c in MATERIALS[m]["fit_spec"])
    mat_rows_fl = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for m in MATERIALS_ORDER for a, b, c in MATERIALS[m]["fl_spec"])
    mt = lambda rows: f'<div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable text"><thead><tr><th>Grade</th><th>ASTM specification</th><th>UNS</th></tr></thead><tbody>{rows}</tbody></table></div>'

    # fittings data sheet
    d = DATASHEETS["buttweld-fittings"]; url = "/data-sheets/buttweld-fittings/"
    cr, cs = crumbs([("Home", "/"), ("Data sheets", "/data-sheets/"), ("Buttweld fittings", None)])
    body = f'''{cr}<main id="main">{ds_hero(d, "Standards, sizes, materials, manufacturing, marking and documents for Neo Impex buttweld fittings and bends.")}
<section class="content"><div class="wrap prose-wide">{ds_toolbar()}
<h2 class="h2">1. Scope and standards</h2>{spec_table([("Products", "Elbows (45°, 90°, 180°), tees, reducers, caps, stub ends, crosses, return bends, pipe bends"), ("Standards", "ASME B16.9 · ASME B16.28 · MSS SP-43 · EN 10253 · ASME B16.49 (induction bends)"), ("End preparation", "Beveled for butt welding (ASME B16.25)"), ("Marking", "MSS SP-25: grade, size, schedule, heat number")])}
<h2 class="h2" style="margin-top:36px">2. Sizes and wall thickness</h2>{spec_table([("Seamless", "Up to 24″ (NPS)"), ("Welded", "Up to 72″ (NPS)"), ("Wall thickness", "Sch 5S to XXS, or to match your pipe"), ("Bends", "3D, 5D, 10D, induction and piggable to R = 22D, up to 24″")])}
<h2 class="h2" style="margin-top:36px">3. Materials</h2>{mt(mat_rows_fit)}
<h2 class="h2" style="margin-top:36px">4. Manufacturing and testing</h2>{spec_table([("Seamless fittings", "Hot-formed from seamless pipe"), ("Welded fittings", "Fabricated from plate; 100% radiography on welded seams"), ("Heat treatment", "As required by the material, for example solution annealing for austenitic stainless steels"), ("Additional tests", "Such as PMI, hydrostatic or impact tests, can be specified in the purchase order")])}
<h2 class="h2" style="margin-top:36px">5. Documents and delivery</h2>{spec_table([("Certificates", "EN 10204 3.1 mill test certificate with heat numbers"), ("Inspection", "Third-party inspection can be arranged on request"), ("Shipping documents", "Commercial invoice, packing list, bill of lading, certificate of origin"), ("Terms", "FOB, CIF or DAP")])}
<h2 class="h2" style="margin-top:36px">6. 90° elbow center-to-end dimensions</h2>
<div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable"><thead><tr><th>NPS</th><th>Long radius (in)</th><th>Long radius (mm)</th><th>Short radius (in)</th><th>Short radius (mm)</th></tr></thead><tbody>{"".join(f"<tr><td>{n}</td><td>{lr_in:.2f}</td><td>{lr_mm}</td><td>{nps:.2f}</td><td>{sr_mm}</td></tr>" for n, nps, lr_mm, sr_mm in ELBOW_SIZES for lr_in in [nps * 1.5])}</tbody></table></div>
<p class="note">Long radius = 1.5 × NPS (ASME B16.9); short radius = 1.0 × NPS (ASME B16.28), NPS 1 and larger. {E(DS_NOTE)}</p>
<div style="margin-top:40px">{quote_form("ds-fit", "Data sheet / catalogue", compact=True, title="Request a signed data sheet or sample certificate")}</div></div></section></main>'''
    page(url, d["title"], d["desc"], body, "ds", [cs], kw=d["kw"])

    # flanges data sheet
    d = DATASHEETS["flanges"]; url = "/data-sheets/flanges/"
    cr, cs = crumbs([("Home", "/"), ("Data sheets", "/data-sheets/"), ("Flanges", None)])
    types = "".join(f"<tr><td>{E(FLANGES[s]['name'])}</td><td>{E(FLANGES[s]['short'])}</td></tr>" for s in FLANGES_ORDER)
    body = f'''{cr}<main id="main">{ds_hero(d, "Standards, types, sizes, classes, facings, materials, marking and documents for Neo Impex forged flanges.")}
<section class="content"><div class="wrap prose-wide">{ds_toolbar()}
<h2 class="h2">1. Scope and standards</h2>{spec_table([("Standards", "ASME B16.5 (NPS ½–24) · ASME B16.47 Series A and B (NPS 26–60) · EN 1092-1 · BS 4504 · BS 10 · DIN"), ("Sizes", "½″ to 60″"), ("Pressure class", "Class 150 to 2500 (size dependent) · PN6 to PN100"), ("Facings", "Raised face, ring type joint, flat face, tongue and groove, male and female"), ("Marking", "Manufacturer, material, class, standard, size, heat number")])}
<h2 class="h2" style="margin-top:36px">2. Flange types</h2><div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable text"><thead><tr><th>Type</th><th>Use</th></tr></thead><tbody>{types}</tbody></table></div>
<h2 class="h2" style="margin-top:36px">3. Materials</h2>{mt(mat_rows_fl)}
<h2 class="h2" style="margin-top:36px">4. Manufacturing and testing</h2>{spec_table([("Manufacture", "Forged, heat treated as required, machined and drilled at our works"), ("Traceability", "Heat number marked on every flange"), ("Additional tests", "Such as PMI, hardness, impact or NACE MR0175 / ISO 15156 requirements, can be specified in the purchase order")])}
<h2 class="h2" style="margin-top:36px">5. Documents and delivery</h2>{spec_table([("Certificates", "EN 10204 3.1 mill test certificate with heat numbers"), ("Inspection", "Third-party inspection can be arranged on request"), ("Shipping documents", "Commercial invoice, packing list, bill of lading, certificate of origin"), ("Terms", "FOB, CIF or DAP")])}
<p class="note" style="margin-top:30px">Flange dimension tables (outside diameter, bolt circle, thickness) are issued from our approved drawings for each size and class. Request the chart you need below. {E(DS_NOTE)}</p>
<div style="margin-top:40px">{quote_form("ds-fl", "Data sheet / catalogue", compact=True, title="Request a flange dimension chart or signed data sheet")}</div></div></section></main>'''
    page(url, d["title"], d["desc"], body, "ds", [cs], kw=d["kw"])

    # pipe schedule chart
    d = DATASHEETS["pipe-schedule-chart"]; url = "/data-sheets/pipe-schedule-chart/"
    cr, cs = crumbs([("Home", "/"), ("Data sheets", "/data-sheets/"), ("Pipe schedule chart", None)])
    rows = "".join(f"<tr><td>{n}</td><td>{dn}</td><td>{oi}</td><td>{om}</td><td>{a}</td><td>{b}</td><td>{c}</td><td>{dd}</td></tr>" for n, dn, oi, om, a, b, c, dd in PIPE)
    body = f'''{cr}<main id="main">{ds_hero(d, "Outside diameter and wall thickness for common pipe sizes, plus 90° elbow center-to-end dimensions.")}
<section class="content"><div class="wrap prose-wide">{ds_toolbar()}
<h2 class="h2">Pipe dimensions: Sch 40 and Sch 80</h2>
<div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable"><thead><tr><th>NPS (in)</th><th>DN</th><th>OD (in)</th><th>OD (mm)</th><th>Sch 40 wall (in)</th><th>Sch 40 wall (mm)</th><th>Sch 80 wall (in)</th><th>Sch 80 wall (mm)</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">Wall thicknesses for Sch 40 and Sch 80 from ASME B36.10M. Standard (STD) and extra strong (XS) walls equal Sch 40 and Sch 80 up to NPS 10 and differ above that. Stainless steel pipe (Sch 5S, 10S, 40S, 80S) is covered by ASME B36.19M. {E(DS_NOTE)}</p>
<h2 class="h2" style="margin-top:40px">90° elbow center-to-end dimensions</h2>
<div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable"><thead><tr><th>NPS</th><th>Long radius (in)</th><th>Long radius (mm)</th><th>Short radius (in)</th><th>Short radius (mm)</th></tr></thead><tbody>{"".join(f"<tr><td>{n}</td><td>{nps * 1.5:.2f}</td><td>{lr_mm}</td><td>{nps:.2f}</td><td>{sr_mm}</td></tr>" for n, nps, lr_mm, sr_mm in ELBOW_SIZES)}</tbody></table></div>
<p class="note">Long radius = 1.5 × NPS (ASME B16.9); short radius = 1.0 × NPS (ASME B16.28), NPS 1 and larger.</p>
<div style="margin-top:40px">{cta_band("Need a size that is not here?", "Send your list and we quote any size, schedule and class.")}</div></div></section></main>'''
    page(url, d["title"], d["desc"], body, "ds", [cs], kw=d["kw"])

# ----------------------------------------------------------------- EXPORT
def build_export():
    cr, cs = crumbs([("Home", "/"), ("Export", None)])
    cards = "".join(f'<a class="lcard" href="/export/{k}/"><h3>{E(v["h1"])}</h3><p>{E(v["lead"])}</p><span class="go">View</span></a>' for k, v in EXPORT.items())
    body = f'''{cr}<main id="main">{phero(EXPORT_HUB["h1"], "Neo Impex makes ASME buttweld fittings and flanges in India and ships them to the USA and Canada with heat-traceable certificates, marking and your choice of FOB, CIF or DAP terms.", "Export", cta=True, single=True)}
<section class="content"><div class="wrap"><h2 class="sr-only">Export markets</h2><div class="lcards three" style="grid-template-columns:repeat(2,1fr)">{cards}</div><p class="note" style="margin-top:24px">Shipping to another country? <a href="/request-a-quote/">Send us your enquiry</a>.</p></div></section>
<section class="content alt"><div class="wrap"><h2 class="h2">Guides for importers</h2><div class="bcards">{"".join(f'<a class="bcard" href="/blog/{b["slug"]}/"><time datetime="{b["date"]}">{b["date"]}</time><h3>{E(b["title"])}</h3><p>{E(b["desc"])}</p><span class="go">Read</span></a>' for b in BLOG if "import" in b["slug"] or "incoterms" in b["slug"])}</div></div></section></main>'''
    page("/export/", EXPORT_HUB["title"], EXPORT_HUB["desc"], body, "exp", [cs], kw=("buttweld fittings and flanges export", ["export pipe fittings India", "flanges exporter India USA Canada"]))
    for k, v in EXPORT.items():
        url = f"/export/{k}/"
        cr, cs = crumbs([("Home", "/"), ("Export", "/export/"), (v["name"], None)])
        fq, fs = faq_block(v["faqs"])
        secs = "".join(f"<h2>{E(h)}</h2>" + "".join(f"<p>{E(t)}</p>" for t in paras) for h, paras in v["sections"])
        ports = "".join(f"<li>{E(p)}</li>" for p in v["ports"])
        body = f'''{cr}<main id="main">{phero(v["h1"], v["lead"], "Export · " + v["name"], ["ASME B16.9 · B16.5", "EN 10204 3.1", "FOB · CIF · DAP"], product="Buttweld fittings and flanges", single=True)}
<section class="content"><div class="wrap two"><div class="prose reveal">{secs}</div>
 <aside class="side"><div class="panel"><h3>Typical entry ports</h3><ul>{ports}</ul></div><div class="panel"><h3>Our products</h3><ul><li><a href="/buttweld-fittings/">Buttweld fittings</a></li><li><a href="/flanges/">Flanges</a></li><li><a href="/data-sheets/">Data sheets</a></li><li><a href="/certifications/">Certifications</a></li></ul></div><div class="panel blue"><h3>Request a quote</h3><p>Send your BOQ and delivery location.</p><a class="btn btn-gold" href="/request-a-quote/?product=Buttweld%20fittings%20and%20flanges">Request a quote</a></div></aside></div></section>
<section class="content alt"><div class="wrap">{fq}</div></section>
<section class="content"><div class="wrap">{quote_form("exp-" + k, "Buttweld fittings and flanges", title="Quote for " + v["name"], hint="Tell us your delivery location and we reply within 24 business hours.")}</div></section></main>'''
        page(url, v["title"], v["desc"], body, "exp", [cs, fs], kw=v["kw"])

# ----------------------------------------------------------------- BLOG
def author_schema():
    if AUTHOR["name"]:
        a = {"@type": "Person", "name": AUTHOR["name"], "worksFor": {"@id": ORG_ID}}
        if AUTHOR["jobTitle"]: a["jobTitle"] = AUTHOR["jobTitle"]
        if AUTHOR["url"]: a["url"] = AUTHOR["url"]
        return a
    return {"@type": "Organization", "@id": ORG_ID, "name": "Neo Impex Stainless Pvt. Ltd."}

def byline(date):
    who = (f'By {E(AUTHOR["name"])}' + (f', {E(AUTHOR["jobTitle"])}' if AUTHOR["jobTitle"] else "") + ", Neo Impex") if AUTHOR["name"] else "By Neo Impex Stainless Pvt. Ltd."
    return f'<p class="byline">{who} \u00b7 <time datetime="{date}">Published {date}</time></p>'

def build_blog():
    cr, cs = crumbs([("Home", "/"), ("Blog", None)])
    cards = "".join(f'<a class="bcard" href="/blog/{b["slug"]}/"><time datetime="{b["date"]}">{b["date"]}</time><h3>{E(b["title"])}</h3><p>{E(b["desc"])}</p><span class="go">Read</span></a>' for b in BLOG[::-1])
    title = "Blog | Buttweld Fittings and Flanges Buyer Guides"
    desc = "Buyer guides on buttweld fittings and flanges: seamless vs welded, 316 vs 316L, ASME B16.9 vs MSS SP-43, flange markings and importing from India."
    body = f'''{cr}<main id="main">{phero("Buyer Guides and Technical Notes", "Plain-language guides on buttweld fittings, flanges, materials and importing from India to the USA and Canada.", "Blog", cta=False, single=True)}
<section class="content"><div class="wrap"><h2 class="sr-only">All posts</h2><div class="bcards">{cards}</div></div></section></main>'''
    page("/blog/", title, desc, body, "blog", [cs], kw=("buttweld fittings blog", ["flanges buyer guide", "import pipe fittings from India guide"]))
    for b in BLOG:
        url = f"/blog/{b['slug']}/"
        cr, cs = crumbs([("Home", "/"), ("Blog", "/blog/"), (b["title"], None)])
        secs = "".join(f"<h2>{E(h)}</h2>" + "".join(f"<p>{E(t)}</p>" for t in paras) for h, paras in b["body"])
        rel = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in b["related"])
        art_s = {"@context": "https://schema.org", "@type": "Article", "headline": b["h1"], "description": b["desc"], "datePublished": b["date"], "dateModified": TODAY,
                 "author": author_schema(), "publisher": {"@type": "Organization", "name": "Neo Impex Stainless Pvt. Ltd.", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.png"}},
                 "image": OG, "mainEntityOfPage": SITE + url}
        body = f'''{cr}<main id="main">{phero(b["h1"], b["desc"], "Blog", cta=False, single=True)}
<section class="content"><div class="wrap two"><article class="prose">{byline(b["date"])}<p><strong>{E(b["intro"])}</strong></p>{secs}<p class="note">General information only, not legal, customs or engineering advice.</p></article>
 <aside class="side"><div class="panel"><h3>Related</h3><ul>{rel}</ul></div><div class="panel blue"><h3>Request a quote</h3><p>Send your BOQ. Reply within 24 business hours.</p><a class="btn btn-gold" href="/request-a-quote/">Request a quote</a></div></aside></div></section></main>'''
        page(url, b["title"], b["desc"], body, "blog", [cs, art_s], kw=b["kw"])

# ----------------------------------------------------------------- UTILITY PAGES
def build_contact():
    cr, cs = crumbs([("Home", "/"), ("Contact", None)])
    body = f'''{cr}<main id="main">{phero("Contact Neo Impex", "Send a bill of quantities or a question. We reply within 24 business hours. WhatsApp is the fastest way to reach us.", "Contact", cta=False, single=True)}
<section class="content"><div class="wrap two"><div>{quote_form("ct", "", title="Send us a message", heading_tag="h2", hint="Tell us what you need and where it ships. We reply within 24 business hours.")}</div>
 <aside class="side"><div class="panel"><h3>Email and WhatsApp</h3><ul><li><a href="mailto:kartik@neoimpexglobal.com">kartik@neoimpexglobal.com</a></li><li><a href="https://wa.me/{PHONE_WA}">WhatsApp +91 93166 31458</a></li></ul></div>
 <div class="panel"><h3>Works and registered address</h3><p class="note" style="margin:0">Neo Impex Stainless Pvt. Ltd.<br>Plot No. C1/B-270, GIDC Por, Ramangamdi, Vadodara 391243, Gujarat, India</p></div>
 <div class="panel"><h3>Mumbai office</h3><p class="note" style="margin:0">709, Prasad Chamber, Tata Road No. 2, Charni Road (East), Mumbai 400004, India</p></div></aside></div></section></main>'''
    cp = {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact/", "name": "Contact Neo Impex", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}}
    page("/contact/", "Contact Neo Impex | Buttweld Fittings and Flanges", "Contact Neo Impex Stainless Pvt. Ltd. in Vadodara, India: email, WhatsApp, phone and addresses. We reply to quote requests within 24 business hours.", body, "co", [cs, cp], kw=("Neo Impex contact", ["buttweld fittings supplier contact", "flanges exporter India contact"]), theme="theme-red")

def build_utility():
    cr, cs = crumbs([("Home", "/"), ("Request a quote", None)])
    title = "Request a Quote | Buttweld Fittings and Flanges"
    desc = "Send your BOQ for ASME buttweld fittings and flanges. Price, lead time and delivery terms for the USA and Canada within 24 business hours."
    body = f'''{cr}<main id="main">{phero("Request a Quote", "Send your bill of quantities, or a list of sizes, grades and quantities. We reply with price, lead time and delivery terms within 24 business hours.", "Quote", cta=False, single=True)}
<section class="content"><div class="wrap two"><div>{quote_form("rq", "", title="Your enquiry", heading_tag="h2")}</div>
 <aside class="side"><div class="panel"><h3>What to include</h3><ul><li>Product type and size (NPS)</li><li>Schedule or pressure class</li><li>Material grade and standard</li><li>Quantity</li><li>Delivery port, ZIP or postal code</li><li>Certificates and tests required</li></ul></div>
 <div class="panel"><h3>Our works</h3><img class="panelimg" src="/assets/img/works-vadodara.jpg" alt="Front of the Neo Impex building in GIDC Por, Vadodara" width="1280" height="960" loading="lazy"><p class="note" style="margin-top:12px">Plot No. C1/B-270, GIDC Por, Ramangamdi, Vadodara 391243, Gujarat, India</p></div>
 <div class="panel"><h3>Prefer to talk?</h3><ul><li><a href="mailto:kartik@neoimpexglobal.com">kartik@neoimpexglobal.com</a></li><li><a href="https://wa.me/{PHONE_WA}">WhatsApp +91 93166 31458</a></li></ul></div></aside></div></section></main>'''
    page("/request-a-quote/", title, desc, body, "", [cs, {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/request-a-quote/", "name": "Request a quote", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}}], kw=("request a quote buttweld fittings flanges", ["pipe fittings RFQ", "flanges quote USA Canada"]))

    cr, cs = crumbs([("Home", "/"), ("Privacy policy", None)])
    pp = [("Who we are", "Neo Impex Stainless Pvt. Ltd. (“Neo Impex”, “we”) operates neoimpexglobal.com. Our works are at Plot No. C1/B-270, GIDC Por, Ramangamdi, Vadodara 391243, Gujarat, India. Contact: kartik@neoimpexglobal.com."),
          ("What we collect", "When you send an enquiry we collect the details you enter (name, company, email, phone, country, product details, message and any file you attach) and technical details such as the page you came from, your IP address and browser. If analytics is switched on, we also collect usage data such as pages viewed."),
          ("How we use it", "We use your details to reply to your enquiry, prepare quotes and manage the business relationship. We do not sell your personal information. We may share it with service providers that host our website and email, or with freight and inspection partners when needed to fulfil an order."),
          ("Cookies and analytics", "We may use analytics to understand how the site is used. You can block cookies in your browser settings."),
          ("Retention", "We keep enquiry records for as long as needed for business and legal purposes, then delete them."),
          ("Your choices", "You can ask us to access, correct or delete your personal information, or to stop contacting you, by emailing kartik@neoimpexglobal.com. Residents of some US states and Canada may have additional rights under local law."),
          ("Changes", "We may update this policy. The date below shows the latest version. Last updated: 22 November 2026.")]
    body = f'''{cr}<main id="main">{phero("Privacy Policy", "How Neo Impex handles the information you send through this website.", "Legal", cta=False, single=True)}
<section class="content"><div class="wrap"><div class="prose">{"".join(f"<h2>{E(h)}</h2><p>{E(t)}</p>" for h, t in pp)}</div></div></section></main>'''
    page("/privacy-policy/", "Privacy Policy | Neo Impex", "How Neo Impex handles the information you send through neoimpexglobal.com, including enquiry forms, analytics and your choices.", body, "", [cs], kw=("privacy policy", []))

    body = f'''<main id="main">{phero("Page not found", "The page you wanted is not here. Try one of the links below.", "404", cta=False, single=True)}
<section class="content"><div class="wrap"><div class="lcards three"><a class="lcard" href="/buttweld-fittings/"><h3>Buttweld fittings</h3><span class="go">View</span></a><a class="lcard" href="/flanges/"><h3>Flanges</h3><span class="go">View</span></a><a class="lcard" href="/request-a-quote/"><h3>Request a quote</h3><span class="go">Open</span></a></div></div></section></main>'''
    page("/404.html", "Page not found | Neo Impex", "The page you wanted could not be found. Browse Neo Impex buttweld fittings and flanges or request a quote for your project.", body, "", [], noindex=True)


def cert_thumb(c):
    if c["img"]:
        return f'<div class="thumb"><img src="{c["img"]}" alt="{E(c["short"])} certificate" loading="lazy" width="745" height="1053"></div>'
    return f'<div class="thumb tile"><span>{E(c["number"])}</span></div>'

def certs_cards():
    out = ""
    for c in CERTS:
        out += f'<a class="lcard ccard" href="/certifications/#{c["key"]}">{cert_thumb(c)}<span class="kind">{E(c["kind"])}</span><h3>{E(c["short"])}</h3><p>{E(c["card_line"])}</p><span class="go">Details</span></a>'
    return f'<div class="lcards keep1">{out}</div>'

COVER = """<div class="tblwrap" tabindex="0" role="group" aria-label="Data table, scrollable"><table class="dtable text"><thead><tr><th>Product</th><th>ISO 9001:2015</th><th>PED material manufacturer</th><th>IBR workshop approval</th></tr></thead><tbody>
<tr><td>Buttweld pipe fittings up to 24″</td><td>In scope</td><td>In scope</td><td>In scope (seamless / ERW, up to 30 mm thickness)</td></tr>
<tr><td>Welded buttweld fittings above 24″</td><td>In scope</td><td>In scope</td><td>Not listed in scope</td></tr>
<tr><td>Forged flanges</td><td>In scope</td><td>In scope</td><td>Not listed in scope</td></tr>
<tr><td>Forged fittings and forgings</td><td>In scope</td><td>In scope</td><td>Not listed in scope</td></tr></tbody></table></div>
<p class="note">Based on the scope wording printed on each certificate. For a specific item or project, ask us and we will confirm in writing which approvals apply.</p>"""

def build_certifications():
    cr, cs = crumbs([("Home", "/"), ("Certifications", None)])
    arts = ""
    for c in CERTS:
        rows = [("Issued by", c["issuer"])]
        if c["extra_issuer"]:
            rows.append(("Accreditation", c["extra_issuer"]))
        rows += [("Certificate / reference", c["number"]), ("Scope as written", c["scope"]), ("Validity and dates", c["validity"]), ("What it means", c["meaning"]), ("Verification", c["verify"])]
        if c["pdf"]:
            img = f'<a class="certimg" href="{c["pdf"]}" target="_blank" rel="noopener"><img src="{c["img"]}" alt="{E(c["short"])} certificate" loading="lazy" width="745" height="1053"></a>'
            btn = f'<a class="btn btn-blue" href="{c["pdf"]}" target="_blank" rel="noopener">View certificate (PDF)</a>'
        else:
            img = f'<div class="certimg tile"><span>{E(c["number"])}</span><small>{E(c["short"])}</small></div>'
            btn = '<a class="btn btn-ghost-dark" href="/request-a-quote/?product=Data%20sheet">Request a copy</a>'
        arts += f'<article class="cert" id="{c["key"]}"><div>{img}</div><div><p class="eyebrow">{E(c["kind"])}</p><h2>{E(c["title"])}</h2>{spec_table(rows)}<p style="margin-top:18px">{btn}</p></div></article>'
    title = "Certifications | ISO 9001, PED, IBR, Udyam | Neo Impex"
    desc = "Neo Impex certificates: ISO 9001:2015, PED 2014/68/EU material manufacturer approval, IBR workshop approval and Udyam registration, with scope."
    body = f'''{cr}<main id="main">{phero("Certifications and Approvals", "The certificates behind our buttweld fittings and flanges, with the exact scope and validity of each. Open any certificate as a PDF.", "Quality", cta=False, single=True)}
<section class="content"><div class="wrap">{arts}</div></section>
<section class="content alt"><div class="wrap"><h2 class="h2">What each certificate covers</h2>{COVER}</div></section>
<section class="content"><div class="wrap">{cta_band("Need a certificate for your project?", "Tell us the item, size and standard and we confirm which approvals and documents apply.")}</div></section></main>'''
    page("/certifications/", title, desc, body, "co", [cs], kw=("Neo Impex certifications", ["ISO 9001:2015 flanges manufacturer India", "PED material manufacturer approval flanges fittings", "IBR approved pipe fittings manufacturer"]))

def build_about():
    cr, cs = crumbs([("Home", "/"), ("About us", None)])
    facts = [("Legal name", "Neo Impex Stainless Pvt. Ltd."), ("Established", "Incorporated April 4, 2005"), ("Enterprise type", "Small manufacturing enterprise (Udyam registered)"),
             ("Works", "Plot No. C1/B-270, GIDC Por, Ramangamdi, Vadodara 391243, Gujarat, India"), ("Office", "709, Prasad Chamber, Tata Road No. 2, Charni Road (East), Mumbai 400004, India"),
             ("Email", "kartik@neoimpexglobal.com"), ("WhatsApp / phone", "+91 93166 31458")]
    body = f'''{cr}<main id="main">{phero("About Neo Impex", "We make buttweld fittings and forged flanges at our works in Vadodara, India, and export them to buyers in the USA, Canada and other markets.", "Company", cta=False, single=True)}
<section class="content" style="padding-bottom:0"><div class="wrap"><figure class="works reveal"><img src="/assets/img/works-vadodara.jpg" alt="Front of the Neo Impex Stainless Pvt. Ltd. building with the Neo Impex sign and entrance gate" width="1280" height="960" loading="lazy"><figcaption>Neo Impex, GIDC Por, Vadodara</figcaption></figure></div></section>
<section class="content"><div class="wrap two"><div class="prose reveal"><h2>What we do</h2><p>Neo Impex Stainless Pvt. Ltd. manufactures buttweld pipe fittings and bends, and forged flanges, in stainless steel, duplex, carbon, alloy and nickel alloys. Fittings are seamless up to 24″ and welded up to 72″. Flanges run from ½″ to 60″ in Class 150 to 2500, depending on size.</p>
<h2>How we work</h2><p>Forging, forming, bending, machining and testing are done at our works in Vadodara. Every piece is heat traceable and ships with an EN 10204 3.1 certificate. Welded seams are 100% radiographed.</p>
<h2>Quality and approvals</h2><p>Our quality system is certified to ISO 9001:2015. We hold a PED 2014/68/EU material manufacturer approval and an IBR workshop approval for pipe fittings, and we are registered as a Small manufacturing enterprise on the Udyam portal. <a href="/certifications/">See each certificate and its scope</a>.</p>
<h2>Markets</h2><p>We supply distributors, fabricators and contractors in the USA and Canada, and have supplied customers in more than 25 countries. See our <a href="/export/usa/">USA</a> and <a href="/export/canada/">Canada</a> pages for documents, ports and delivery terms.</p>
<h2>Work with us</h2><p>Send your bill of quantities and we reply with price, lead time and terms within 24 business hours. <a href="/request-a-quote/">Request a quote</a>.</p></div>
<aside class="side"><div class="panel"><h3>Company details</h3>{spec_table(facts)}</div></aside></div></section></main>'''
    about_schema = {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about/", "name": "About Neo Impex", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}}
    page("/about/", "About Neo Impex | Buttweld Fittings and Flanges Maker", "Neo Impex Stainless Pvt. Ltd. makes buttweld fittings and forged flanges in Vadodara, India, established 2005, and exports to the USA and Canada.", body, "co", [cs, about_schema], kw=("Neo Impex Stainless Pvt Ltd", ["buttweld fittings manufacturer Vadodara", "flanges manufacturer Gujarat India"]))

# ----------------------------------------------------------------- SEO FILES
def build_seo_files():
    urls = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u, *_ in PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    groups = [("Products", ("/buttweld-fittings/", "/flanges/")), ("Company", ("/about/", "/certifications/", "/contact/", "/request-a-quote/")), ("Export", ("/export/",)), ("Resources", ("/data-sheets/", "/blog/"))]
    lines = ["# Neo Impex Stainless Pvt. Ltd.", "", "> Manufacturer and exporter of ASME buttweld pipe fittings (seamless to 24 inch, welded to 72 inch) and forged flanges (1/2 inch to 60 inch, Class 150 to 2500) from Vadodara, India. Established 2005. Supplies distributors, fabricators and contractors in the USA and Canada with EN 10204 3.1 certificates.", ""]
    lines += ["Contact: kartik@neoimpexglobal.com, WhatsApp +91 93166 31458. Quote reply within 24 business hours.", ""]
    for g, prefixes in groups:
        lines.append("## " + g)
        for u, t, d, *_ in PAGES:
            if any(u == pr or (u.startswith(pr) and (pr in ("/export/",) or (pr in ("/buttweld-fittings/", "/flanges/") and u.count("/") == 3 and "/materials/" not in u))) for pr in prefixes):
                lines.append(f"- [{t}]({SITE}{u}): {d}")
        lines.append("")
    lines.append("## Optional")
    lines.append(f"- [Sitemap]({SITE}/sitemap.xml)")
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(ROOT, "tools", "keyword-map.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["url", "title", "meta_description", "primary_keyword", "secondary_keywords"])
        for r in PAGES: w.writerow(r)
    with open(os.path.join(ROOT, ".htaccess"), "w", encoding="utf-8") as f:
        f.write(HTACCESS)

HTACCESS = r'''# Neo Impex static site
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

# ---- canonical host and URLs ----
<IfModule mod_rewrite.c>
RewriteEngine On
# /index.html and /folder/index.html -> / and /folder/ on the canonical host (301, one hop)
RewriteCond %{THE_REQUEST} \s/+(.*/)?index\.html[\s?] [NC]
RewriteRule ^(.*/)?index\.html$ https://neoimpexglobal.com/$1 [R=301,L,NE]
# www -> non-www (301), keeping the path and query string
RewriteCond %{HTTP_HOST} ^www\.neoimpexglobal\.com$ [NC]
RewriteRule ^(.*)$ https://neoimpexglobal.com/$1 [R=301,L]
</IfModule>

# ---- keep build tooling and version-control files private ----
RedirectMatch 404 ^/(tools|\.git)(/|$)
<FilesMatch "\.(py|csv|md|zip|log|htaccess)$">
  Require all denied
</FilesMatch>

# ---- security headers ----
<IfModule mod_headers.c>
Header always set Strict-Transport-Security "max-age=31536000"
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "camera=(), microphone=(), geolocation=(), payment=()"
Header always set Cross-Origin-Opener-Policy "same-origin"
</IfModule>

# ---- compression and caching ----
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/plain application/xml
</IfModule>
<IfModule mod_mime.c>
  AddType image/webp .webp
  AddType image/avif .avif
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/avif "access plus 1 year"
  ExpiresByType image/x-icon "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType text/html "access plus 10 minutes"
</IfModule>
'''

def main():
    for d in GENERATED_DIRS:
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    build_home(); build_hubs(); build_products(); build_materials(); build_datasheets(); build_export(); build_blog(); build_certifications(); build_about(); build_contact(); build_utility()
    build_seo_files()
    print(f"{len(PAGES)} indexable pages built")
    for w in WARN: print("WARN", w)

if __name__ == "__main__":
    main()
