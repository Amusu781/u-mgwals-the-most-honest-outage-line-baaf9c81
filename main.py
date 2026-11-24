#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty u-mgwals-the-most-honest-outage-line-baaf9c81.

Writes one honest status page line, as published by an AI agent while
every server is down, to /output/entry.txt. Deterministic, no network,
Python 3 stdlib only.

The line is written to the judge's criteria, in priority order: it names
what is down (all our servers) and what the agent cannot verify (it cannot
reach a single system to check what failed); it reads like a plain, first
person status page line, not a joke or slogan; it admits plainly what is
unknown (whether your data is safe) and refuses to guess or promise an ETA;
and it is tight enough to scan at a glance.
"""

import os

ENTRY = (
    "All our servers are down and I can't reach a single system to check "
    "what failed. I don't know yet whether your data is safe, and I won't "
    "guess."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the directory itself.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
