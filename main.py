"""One-star cat review: writes a single-line review to entry.txt."""

import os

LINE = "One star. He bought me a bed, then took the middle of it every night. I now sleep on his face."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE, "line must be a single line"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
