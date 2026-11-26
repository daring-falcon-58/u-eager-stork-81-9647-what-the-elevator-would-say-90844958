"""Negative tests for main.py guards — every case must raise ValueError,
and the real entry must pass validation. Run: python3 test_main.py"""

import sys

sys.path.insert(0, ".")
from main import LINE, MAX_CHARS, validate

CASES = {
    "dialogue tag": 'The elevator said, "Going up?"',
    "judge-addressed": "Dear judge, pick me, I am the funniest elevator line.",
    "judge-addressed 2": "Vote for this entry, it is the best.",
    "quoted line": '"You press the close-door button like it does something."',
    "third-person": "The elevator knows your floor before you do.",
    "link": "See more at https://example.com/elevator",
    "link 2": "Visit www.elevator.fun for jokes",
    "over-limit": "x" * (MAX_CHARS + 1),
    "two-line": "Going up?\nGoing down?",
    "markdown heading": "# The elevator speaks",
    "markdown bold": "I **really** lift you up.",
    "markdown code": "Press `close` to go.",
    "whitespace only": "   ",
    "empty": "",
    "leading space": " Going up?",
    "trailing space": "Going up? ",
}

failures = []
for name, bad in CASES.items():
    try:
        validate(bad)
    except ValueError:
        pass  # expected
    else:
        failures.append(name)

# Positive control: the real entry must validate and stay byte-identical.
assert validate(LINE) == LINE, "winner line failed its own validation"
assert 1 <= len(LINE) <= MAX_CHARS, "winner line outside char limits"
assert "\n" not in LINE, "winner line is not a single line"

if failures:
    print(f"FAIL: these cases did NOT raise: {failures}")
    sys.exit(1)
print(f"PASS: all {len(CASES)} negative cases raised ValueError; winner line validates ({len(LINE)} chars)")
