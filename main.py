"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance: the unreachable crumbs at the bottom of a chip
bag. The invention is the joke.
"""

import os

ENTRY = (
    "The Crumb Butler, a tiny butler who lives in your chip bag and serves "
    "the last crumbs on a miniature silver tray, so you never have to shake "
    "the bag over your face like a raccoon at a wedding."
)

# The gate requires 1-220 characters, a single line, no trailing newline.
assert 1 <= len(ENTRY) <= 220, len(ENTRY)
assert "\n" not in ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
