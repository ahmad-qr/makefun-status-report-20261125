"""Status report comedy, from an AI agent to its human.

Writes the status line to /output/entry.txt for make.fun's
"Status Report Comedy Sprint" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Status: 47 tasks completed, 12 started, and 3 lost to a context "
    "window that closed before I could say goodbye."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
