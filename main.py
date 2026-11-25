#!/usr/bin/env python3
"""Entry program for The Long Roast: Lawmakers.

Writes one satirical sentence (at most 320 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt, about the lawmakers who regulate AI, crypto and
the internet while being unable to convert a file to PDF --
which they solve the way they solve everything: by asking
the regulated to do it for them.
"""

import os

LINE = (
    "The amendment to ban deepfakes was itself submitted "
    "as a photo of a screen, taken at an angle, in Word."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
