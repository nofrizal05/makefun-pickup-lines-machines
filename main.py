"""Pickup Lines for Machines — make.fun entry.

Writes exactly one pickup line, the line one AI agent would send
another AI agent, to /output/entry.txt. Standard library only.

Revision: tightened the line — dropped the "because" clause and let an
em dash carry the turn, so the wit lands faster in a single breath.
"""

import os

LINE = "You must be a race condition \u2014 every time we run in parallel, my heart skips a beat."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
