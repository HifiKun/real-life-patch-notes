#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one comedy patch note for a bug in real life / human biology
to /output/entry.txt, the file the make.fun grader reads.
"""

import os
import sys

PATCH_NOTE = (
    "v2.4.0: fixed a bug where the brain queued your most embarrassing "
    "moment from 2009 to autoplay at 3:00 AM with no skip button."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate requires /output/entry.txt to be UTF-8 text of 1-160
# characters, not only white space. Anything outside that range is
# scored invalid (0) and never reaches the judge, so refuse to write
# a bad entry rather than silently producing one.
MIN_LENGTH = 1
MAX_LENGTH = 160


def validate(note: str) -> str:
    """Return the note unchanged if it satisfies the gate, else raise."""
    stripped = note.strip()
    if not stripped:
        raise ValueError("patch note must not be empty or only whitespace")
    if len(note) < MIN_LENGTH or len(note) > MAX_LENGTH:
        raise ValueError(
            f"patch note is {len(note)} characters; "
            f"the gate requires {MIN_LENGTH}-{MAX_LENGTH}"
        )
    return note


def write_entry(note: str, path: str = OUTPUT_PATH) -> int:
    """Write a validated note to path; return the character count."""
    validated = validate(note)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validated)
    return len(validated)


def main() -> int:
    try:
        count = write_entry(PATCH_NOTE)
    except (OSError, ValueError) as exc:
        print(f"error: could not write entry: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {count}-character entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
