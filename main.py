#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The line is aimed squarely at an AI,
built on the attention-mechanism premise rather than the worn
battery / charging / reboot moves, and lands its setup and punch
inside one breath.
"""

import os

# The line itself: a pickup line to an AI, fresh premise (attention
# over tokens), no batteries, no charging, no rebooting. 106 chars.
LINE = (
    "Are you my attention mechanism? Because in a room full of "
    "tokens, you're the only one I keep attending to."
)


def main():
    # Gate check, mirroring the brief: 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
