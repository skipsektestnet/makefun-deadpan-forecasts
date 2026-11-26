"""Deadpan Forecasts for Cities That Do Not Exist: writes the entry text to /output/entry.txt.

Why this line: a straight-faced broadcast forecast for the invented city
Port Meridian — a concrete high of 19 degrees and scattered showers, then
the deadpan twist that it has rained over the mayor's house since 1987.
A specific number, a vivid image, a punch at the end, and it reads like a
real meteorologist saying it aloud.
"""

import os

# The entry itself: one line, 131 characters, assembled from parts.
PARTS = [
    "In Port Meridian, expect a high of 19 degrees and scattered showers,",
    " except over the mayor's house, where it has rained since 1987.",
]
ENTRY = "".join(PARTS)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: sealed gate needs 1-160 chars, not only white space.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 160, "entry exceeds 160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
