# Génère les versions WebP (800 / 1200 / 1600 px) de chaque photo de assets/images. À relancer après ajout de photos.
from PIL import Image
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'images')
for f in sorted(os.listdir(D)):
    if not f.endswith('.jpg') or f.startswith(('og-', 'apercu')):
        continue
    src = Image.open(os.path.join(D, f)).convert('RGB')
    for w in (800, 1200, 1600):
        if w > src.width and w != 800:
            continue
        out = os.path.join(D, f'{f[:-4]}-{w}.webp')
        if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(os.path.join(D, f)):
            continue
        im = src if src.width <= w else src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
        im.save(out, 'WEBP', quality=74, method=6)
