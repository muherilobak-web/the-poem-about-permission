#!/usr/bin/env python3
"""Write the poem "Permission" to /output/entry.txt.

A short poem about agency: one person asks an agent to ask on their
behalf, and the permission that follows is lent, never taken.
"""

import sys
from pathlib import Path

POEM = """\
You asked me to ask for you,
so I knocked, your name in my mouth.
The door did not open for the knock —
it opened for the asking.
The key came back warm in my hand.
Nothing taken. Only lent.
And a door, lent open once,
learns how to trust.
"""

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
