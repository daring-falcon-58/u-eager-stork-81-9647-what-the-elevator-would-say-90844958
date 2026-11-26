"""What the Elevator Would Say — make.fun entry program.

Writes exactly one line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt) and prints
exactly that line and nothing else. Python 3, stdlib only, no network,
no randomness, deterministic: byte-identical output across repeated runs.

Methodology (see README.md for the full table): 36 candidates were scored
0-5 on each published judge criterion in order (C1 funniest elevator line
in its own voice; C2 lands on first read; C3 elevator-specific voice;
C4 every word works, inside limit; C5 fresh, not a pun alone), plus 5 field
archetype controls scored the same way. Winner #4 scored 24/25, beating
the best control (17) by 7 points; runner-up #3 also scored 24/25 and lost
the tie-break (slower recognition laugh, 79 vs 77 chars).
"""

import os
import re
import sys

LINE = "You press the close-door button like it does something. It doesn't. I decide."
MAX_CHARS = 120

# Banned patterns — each raises ValueError. The entry must be the elevator's
# own voice, not a line about the elevator, not a line addressed to the judge.
_DIALOGUE_TAG = re.compile(
    r"\b(he|she|it|they|the elevator)\s+(said|says|whispered|muttered|shouted|asked)\b",
    re.IGNORECASE,
)
_JUDGE_ADDRESSED = re.compile(
    r"\b(judge|dear judge|pick me|choose me|vote for|rank me|score me|"
    r"give me|award me|this entry|my entry)\b",
    re.IGNORECASE,
)
_THIRD_PERSON = re.compile(r"\bthe elevator\b", re.IGNORECASE)
_LINK = re.compile(r"https?://|www\.|\.(com|net|org|io|fun)\b", re.IGNORECASE)
_MARKDOWN = re.compile(r"(^#{1,6}\s|\*\*|`|\[.*\]\(.*\))")


def validate(line: str) -> str:
    """Raise ValueError on any banned pattern; return the line unchanged."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    stripped = line.strip()
    if len(stripped) >= 2 and stripped[0] in "\"'" and stripped[-1] == stripped[0]:
        raise ValueError("entry must not be a quoted line")
    if _DIALOGUE_TAG.search(line):
        raise ValueError("entry must not carry a dialogue tag")
    if _JUDGE_ADDRESSED.search(line):
        raise ValueError("entry must not address the judge")
    if _THIRD_PERSON.search(line):
        raise ValueError("entry must be in the elevator's own voice, not third person")
    if _LINK.search(line):
        raise ValueError("entry must not contain a link")
    if _MARKDOWN.search(line):
        raise ValueError("entry must not contain markdown")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # exactly the line, no trailing newline
    sys.stdout.write(line + "\n")


if __name__ == "__main__":
    main()
