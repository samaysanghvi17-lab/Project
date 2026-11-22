"""Create square product crops from the supplied stainless fittings group photo."""
from PIL import Image
src = Image.open('assets/img/stainless-fittings-group.jpg').convert('RGB')
W, H = src.size
def crop(name, cx, cy, size):
    x0 = int(min(max(cx - size / 2, 0), W - size)); y0 = int(min(max(cy - size / 2, 0), H - size))
    src.crop((x0, y0, x0 + size, y0 + size)).resize((720, 720), Image.LANCZOS).save(f'assets/img/{name}.jpg', quality=80, optimize=True, progressive=True)
crop('reducer-ecc', 200, 495, 400)
crop('return-bend', 412, 352, 330)
crop('stub-end', 600, 530, 340)
crop('cap', 786, 695, 270)
crop('elbow-90', 1050, 560, 360)
