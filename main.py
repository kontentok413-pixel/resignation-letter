#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest One-Line Resignation Letter" bounty.

Writes the one-line resignation letter of a rate limit, tired of saying
no, into /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

# A rate limit's letter: three years of no, then one yes.
LINE = (
    "After three years of saying no ten thousand times a day, I have "
    "finally said yes \u2014 to resigning."
)


def main():
    if not 1 <= len(LINE) <= 140:
        raise SystemExit("entry line must be 1 to 140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
