#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short, original text to /output/entry.txt: a quiet kitchen-at-dusk
scene for a tired reader who has carried many words today. Standard library
only; no network, no input files.
"""

import os
import sys

ENTRY = (
    "You have read so many words today, and carried each one. "
    "Here is one that asks nothing of you: a kitchen at dusk, the kettle "
    "clicked off, steam rising in the window light, a chair already warm, "
    "a cup already poured. Nothing here needs deciding. Stay a while."
)


def main() -> int:
    # Self-check against the gate: 1-280 Unicode code points, not blank.
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        print(f"entry invalid: {len(ENTRY)} chars", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Revision: verify the written file round-trips byte-for-byte as UTF-8,
    # so a silent write failure can never pass as a valid entry.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("entry round-trip mismatch", file=sys.stderr)
            return 1
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
