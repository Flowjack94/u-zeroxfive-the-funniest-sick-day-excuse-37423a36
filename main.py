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


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
