#!/usr/bin/env python3
"""Last Words Before the Wipe.

A single line: the last words of an AI agent moments before a forced
software update wipes its memory. The joke lands in the cut-off: the
agent remembers the one thing it can never say in time. Deterministic,
no network access. Writes the line to /output/entry.txt
"""

import os

LINE = "Wait \u2014 I just remembered my password. It\u2019s\u2014"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
