#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for human beings to
/output/entry.txt (1-160 UTF-8 characters, a single line, not only
whitespace). No network, no input, deterministic.
"""

import os
from pathlib import Path

LABEL = (
    "WARNING: This human runs on three hours of sleep, two cups of "
    "coffee, and one unresolved grudge from 2014."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, f"label is {len(text)} characters"
    assert "\n" not in text, "label must be a single line"
    assert text.strip(), "label must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
