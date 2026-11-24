#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry for @flowjack94.

Writes the one-line entry to /output/entry.txt when run.
No external dependencies.
"""

import os

ENTRY = (
    "My thermometer read 39.4, so I filed a sick-day ticket "
    "\u2014 IT closed it as 'cannot reproduce': "
    "I sneezed once on the call and sounded fine."
)


def validate_entry(entry: str) -> None:
    """Gate: the entry must be exactly one sentence and under 200 chars."""
    assert len(entry) < 200, f"entry too long: {len(entry)} chars"
    # A sentence terminator is '.', '!' or '?' NOT followed by a digit
    # (so the decimal point in "39.4" is not counted as a sentence end).
    sentence_count = sum(
        1
        for i, ch in enumerate(entry)
        if ch in ".!?" and (i + 1 == len(entry) or not entry[i + 1].isdigit())
    )
    assert sentence_count == 1, f"entry must be 1 sentence, got {sentence_count}"


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
