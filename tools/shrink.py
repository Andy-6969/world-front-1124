"""shrink.py <render-2x.png> <entry.png>: scale the 2x screenshot to 1024 x 1024 and keep it under 1 MiB.
Also writes out/thumb300.png beside the screenshot, the size the judge's rubric asks the page to read at."""
import os
import sys

from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
if im.size != (1024, 1024):
    im = im.resize((1024, 1024), Image.LANCZOS)
im.save(dst, optimize=True)
if os.path.getsize(dst) > 1_000_000:
    # a 256-colour palette keeps flat drawings and text crisp at a fraction of the size
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dst, optimize=True)
print(f"{dst}: {im.size[0]}x{im.size[1]}, {os.path.getsize(dst)} bytes")
im.resize((300, 300), Image.LANCZOS).save(os.path.join(os.path.dirname(os.path.abspath(src)), "thumb300.png"))
