"""Deadpan Forecasts for Cities That Do Not Exist.

Writes the one-line entry to /output/entry.txt.

The line: a straight-faced broadcast forecast for the invented city
Port Meridian. A concrete high of 19 degrees and scattered showers,
then the deadpan twist that it has rained over the mayor's house
since 1987. A specific number, a vivid image, a punch at the end,
and it reads like a real meteorologist saying it aloud.
"""

import os

PARTS = [
    "In Port Meridian, expect a high of 19 degrees and scattered showers,",
    "except over the mayor's house, where it has rained since 1987.",
]
ENTRY = " ".join(PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def check(entry):
    """Sealed gate: one non-empty line, 1-160 chars."""
    assert entry and not entry.isspace(), "entry must not be empty"
    assert len(entry) <= MAX_CHARS, "entry exceeds 160 characters"
    assert "\n" not in entry, "entry must be a single line"


def main():
    check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
