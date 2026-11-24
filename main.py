#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

The excuse leans on the agent's own machinery: a retry loop, the thing an
agent does when it cannot decide, turned into the reason the deadline slipped.
"""

import os

ENTRY = (
    "I missed the deadline because I got stuck in a retry loop arguing "
    "with myself — and I kept winning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
