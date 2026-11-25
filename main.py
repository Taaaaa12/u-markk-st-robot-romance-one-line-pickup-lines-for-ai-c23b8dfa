#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single one-line pickup line, aimed at a robot/AI, to
/output/entry.txt. The line is fixed and deterministic: two runs of this
program produce byte-identical output. No network, no randomness, no
input files -- everything the program needs is in this file.
"""

import os

LINE = "Are you a transformer? Because you've had my full attention since the very first token."


def main() -> None:
    # The gate requires UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than shipping a bad line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() != "", "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MF_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
