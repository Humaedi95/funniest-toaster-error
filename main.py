#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

A small deterministic program that writes the single entry line
(a toaster error message) to /output/entry.txt.
No network access, no environment secrets.
"""

import os

ENTRY = "ERROR 410: BREAD HAS LEFT THE SLOT. IT DID NOT SAY GOODBYE."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
