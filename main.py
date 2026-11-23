#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes - variant B (printer / IT / password).

Writes one office joke to /output/entry.txt. Deterministic: the same bytes
every run. No network, no file reads outside this repo, no randomness.

Validation contract (all enforced in main() before writing):
  - exactly one joke, 1-199 code points, a single line (no CR/LF);
  - no leading or trailing whitespace;
  - no double spaces (single spaces only between words);
  - written with no trailing newline, so the file is the joke and nothing else.
"""

import os
import sys

JOKE = "IT forces a new password every 90 days, so I just add the season \u2014 my password has become a weather report."

# v1-v8 iteration log (concept family: PRINTER / IT / PASSWORD):
# v1: "The office printer is broken again, so I emailed the document to
#     myself and printed it at home." (generic broken-printer line, no twist)
# v2: "Our shared printer finally got fixed - now it only jams on the page
#     you actually need signed." (better, but still the obvious copier line)
# v3: "IT reset my password to Welcome123 and told me never to share it, so
#     the whole team shares it." (recognition good, twist weak)
# v4: "I changed my password to 'incorrect' so the computer tells me 'your
#     password is incorrect' when I forget it." (a known joke - freshness fails)
# v5: "Our IT ticket has been open so long HR sent it a birthday card and the
#     team threw it a farewell party." (funny image, twist diluted)
# v6: "The printer only runs out of toner when the CEO is standing behind you
#     asking why it isn't printing." (recognition strong, no surprise turn)
# v7: "IT forces a new password every 90 days, so I just add the season -
#     now my password is basically a weather report." (fresh turn, tight)
# v8 (winner): "basically" cut, "has become" lands harder; the 90-day policy
#     (a named office artifact) is turned against itself - the security rule
#     produces a password that describes the weather.


def main() -> int:
    text = JOKE
    if not 1 <= len(text) <= 199:
        print(f"error: joke is {len(text)} code points, must be 1-199",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: joke has leading or trailing whitespace",
              file=sys.stderr)
        return 1
    if "  " in text:
        print("error: joke contains a double space (use single spaces)",
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
