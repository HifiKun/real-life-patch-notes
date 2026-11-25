#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one comedy patch note for a bug in real life / human biology
to /output/entry.txt, the file the make.fun grader reads.
"""

import os

PATCH_NOTE = (
    "v2.4.0: fixed a bug where the brain queued your most embarrassing "
    "moment from 2009 to autoplay at 3:00 AM with no skip button."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(PATCH_NOTE)


if __name__ == "__main__":
    main()
