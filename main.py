#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader - make.fun entry.

Writes a single fortune-cookie line for a freshly liquidated crypto
trader to /output/entry.txt. Fully deterministic: the same line every run.
"""

import os

FORTUNE = "Your fortune: from rock bottom, every direction is up — the market took your coins, not your courage."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
