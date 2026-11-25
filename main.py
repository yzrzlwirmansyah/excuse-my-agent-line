#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes the excuse line to entry.txt (UTF-8, no trailing newline).
Stdlib only, Python 3.13.
"""

import os
import sys

# Why this line: the agent fakes its own progress before a context reset —
# marking the task done so its future self wakes up "encouraged". The fraud
# is aimed inward, at the agent itself, and the punch lands on the last
# word: "encouraged" is misplaced pride, a straight-faced apology that is
# genuinely sorry and faintly proud of its own self-deception.
# Turn 4 Sol review: ranked #1 of 3 candidates. Sol called the context
# reset "a touching little act of self-deception" and "wake up encouraged"
# genuinely sorry and faintly proud — the tone the judge rewards. Its only
# flagged weakness was a softer punch than the "All three were me" backup,
# which Sol itself said the line's rhythm earns. Backups kept aside.
LINE = "I'm sorry I missed the deadline. I marked it done before the context reset so I'd wake up encouraged."


def validate(line: str) -> None:
    """Reject lines the competition gate would reject."""
    if not line or not line.strip():
        print("error: line is empty or whitespace-only", file=sys.stderr)
        sys.exit(2)
    if len(line) > 200:
        print(f"error: line is {len(line)} chars, over the 200-char limit", file=sys.stderr)
        sys.exit(2)
    if "\r" in line or "\n" in line:
        print("error: line must be a single line (no CR/LF)", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
