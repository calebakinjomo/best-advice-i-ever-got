#!/usr/bin/env python3
"""The Best Advice I Ever Got - make.fun entry.

Writes one sentence - the best advice the writer ever received - to
/output/entry.txt. The line is 127 characters, one sentence, no trailing
newline: exactly the entry and nothing else.
"""

import os

ENTRY = (
    "My dad told me never to borrow money to look rich \u2014 "
    "the people you're trying to impress won't be there "
    "when the debt comes due."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
