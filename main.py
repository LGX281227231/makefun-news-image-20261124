"""make.fun news-image-20261124 entry (Python 3.13, standard library only).

The image is entry.png beside this file, drawn by draw.py from the
headlines reported on Tuesday 24 November 2026. The grader runs this
program with no network, so it only copies the image to /output.
"""

import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
# Deterministic: the same bytes are copied on every run, twice in grading.
if not os.path.isfile(src):
    raise SystemExit("entry.png missing from repository")
os.makedirs(os.path.dirname(out), exist_ok=True)
shutil.copyfile(src, out)
