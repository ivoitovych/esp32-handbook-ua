#!/usr/bin/env python3
"""Контактний відбиток сторінок цілі — для візуальної вичитки верстання.

    tools/preview.py dovidnyk            усі сторінки
    tools/preview.py dovidnyk 3 8        сторінки 3–8
    tools/preview.py dovidnyk 3 8 --cols 2 --scale 0.9

Кладе build/<ціль>/preview.png. Проміжні pgNN.png прибирає за собою.
"""

import argparse
import glob
import os
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("first", nargs="?", type=int, default=1)
    ap.add_argument("last", nargs="?", type=int, default=0)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--scale", type=float, default=0.55)
    ap.add_argument("--ppi", type=int, default=110)
    a = ap.parse_args()

    tdir = ROOT / "build" / a.target
    if not (tdir / "root.typ").exists():
        sys.exit(f"немає {tdir}/root.typ — спершу tools/build.py {a.target}")

    os.chdir(tdir)
    for f in glob.glob("pg*.png"):
        os.remove(f)

    import typst
    from PIL import Image

    typst.compile("root.typ", output="pg{n}.png", format="png",
                  ppi=a.ppi, root=str(ROOT))
    pages = sorted(glob.glob("pg*.png"))
    last = a.last or len(pages)
    sel = pages[a.first - 1:last]
    if not sel:
        sys.exit(f"порожній діапазон: сторінок усього {len(pages)}")

    ims = [Image.open(f) for f in sel]
    w, h = ims[0].size
    w, h = int(w * a.scale), int(h * a.scale)
    ims = [i.resize((w, h)) for i in ims]
    cols = min(a.cols, len(ims))
    rows = (len(ims) + cols - 1) // cols
    pad = 8
    sheet = Image.new("RGB",
                      (w * cols + pad * (cols + 1), h * rows + pad * (rows + 1)),
                      "#9a9a9a")
    for k, im in enumerate(ims):
        sheet.paste(im, ((k % cols) * (w + pad) + pad,
                         (k // cols) * (h + pad) + pad))
    sheet.save("preview.png")

    for f in glob.glob("pg*.png"):
        os.remove(f)

    print(f"сторінок у цілі: {len(pages)}; показано {a.first}–{last}")
    print(f"{(tdir / 'preview.png')}  {sheet.size[0]}×{sheet.size[1]}")


if __name__ == "__main__":
    main()
