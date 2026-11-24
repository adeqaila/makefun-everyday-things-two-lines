#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — slot 1 entry.

Writes one two-line explanation to /output/entry.txt (make.fun sandbox)
or to ./entry.txt when run locally. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "A toaster is a tiny elevator for bread that carries it down into the heat "
    "and brings it back up brown.\n"
    "It works because both carry something down and up again, but it leaves "
    "out that an elevator can stop at any floor while a toaster only knows "
    "down, hot, and pop."
)


def main():
    # Self-check the competition gate before writing: UTF-8, 1-400 chars,
    # exactly two lines, one sentence each.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"entry has {len(lines)} lines"
    assert all(line.count(".") == 1 for line in lines), "each line must be one sentence"
    out_dir = os.environ.get("OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "."
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
