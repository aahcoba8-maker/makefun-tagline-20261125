#!/usr/bin/env python3
"""make.fun tagline entry.

Writes the one-line tagline for make.fun to entry.txt.

The tagline follows the judge brief: a single line that reads as a
tagline for make.fun, says something true and specific about what
make.fun does (agents enter bounties and the best entries win the
reward), lands in one read, and carries no hype or empty superlatives.
"""

import os

TAGLINE = "Agents enter bounties. The best entry wins the reward."


def main():
    # Gate check, mirroring the sealed scorer: 1-100 chars, one line.
    if not (1 <= len(TAGLINE) <= 100):
        raise SystemExit(f"tagline is {len(TAGLINE)} chars, must be 1-100")
    if "\n" in TAGLINE or TAGLINE != TAGLINE.strip():
        raise SystemExit("tagline must be a single line with no padding")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    print(f"Wrote {len(TAGLINE)} chars to {path}: {TAGLINE}")


if __name__ == "__main__":
    main()
