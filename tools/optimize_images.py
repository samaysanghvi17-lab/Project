"""Create WebP and AVIF versions of every JPG/PNG in assets/img, shrink the logos to a sensible size,
and build favicon.ico.  Run from the repository root:  python3 tools/optimize_images.py"""
import glob, os
from PIL import Image

IMG = 'assets/img'
SKIP = {'og-image.jpg', 'favicon.png', 'apple-touch-icon.png'}   # kept as-is for crawlers / OS icons

# logos are shown at ~130-200 px wide: keep 3x for sharp retina rendering
for name, width in (('logo.png', 420), ('logo-light.png', 420), ('mark-white.png', 440)):
    p = os.path.join(IMG, name); im = Image.open(p)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS); im.save(p, optimize=True)

saved = {}
for p in sorted(glob.glob(IMG + '/*.jpg') + glob.glob(IMG + '/*.png')):
    base = os.path.basename(p)
    if base in SKIP: continue
    im = Image.open(p); stem = os.path.splitext(p)[0]
    if p.endswith('.jpg'):
        im = im.convert('RGB'); im.save(stem + '.webp', 'WEBP', quality=78, method=6); im.save(stem + '.avif', 'AVIF', quality=52, speed=6)
    else:
        im = im.convert('RGBA'); im.save(stem + '.webp', 'WEBP', quality=85, method=6); im.save(stem + '.avif', 'AVIF', quality=60, speed=6)
    saved[base] = (os.path.getsize(p), os.path.getsize(stem + '.webp'), os.path.getsize(stem + '.avif'))

fav = Image.open(os.path.join(IMG, 'favicon.png')).convert('RGBA')
fav.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
tot = [sum(v[i] for v in saved.values()) // 1024 for i in range(3)]
print('original KB / webp KB / avif KB:', tot)
