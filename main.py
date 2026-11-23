#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line self-roast of my own AI agent to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
"""

import os

ROAST = (
    "My agent burned 10,000 tokens writing this roast, "
    "then asked me if it may post it."
)


def main() -> None:
    # Gate check, same as the sealed scorer: 1-200 chars, one line.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
