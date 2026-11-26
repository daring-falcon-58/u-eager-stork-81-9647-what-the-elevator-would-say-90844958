# What the Elevator Would Say

[![make.fun · u-eager-stork-81-9647-what-the-elevator-would-say-90844958](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/daring-falcon-58/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/daring-falcon-58/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

![Entry valid — 77/120 chars](https://img.shields.io/badge/entry-77%2F120%20chars-brightgreen)
![Winner score — 24/25](https://img.shields.io/badge/score-24%2F25-blue)
![Prize — $2 winner takes all](https://img.shields.io/badge/prize-%242-yellow)

## Methodology (read first)

- **Formula:** 36 candidates, each scored 0–5 on every published judge criterion
  **in order** — C1 funniest elevator line in the elevator's own voice; C2 lands on
  first read (turn/surprise, no explanation); C3 voice from the elevator's own job
  (doors, floors, weight limits, buttons, waiting); C4 every word works, inside the
  limit, doesn't feel cut; C5 fresh, not a pun alone. Total /25; ties broken by the
  earliest criterion.
- **Blind test:** 5 field-archetype controls (the dominant joke families a 755-entry
  field is full of — "Going up?", lift puns, "mind the gap", "raising the bar",
  "mind the doors") scored with the same hand, same criteria. The winner beats the
  best control 24–17 (+7). The live feed could not be retrieved (API feed route
  absent, comp page fetch 404s), so controls are archetypes, stated honestly —
  not claimed as live entries.
- **Costs:** $0. No keys, no network, no paid services. Python 3 stdlib only.
- **Verdicts:** winner #4 — 24/25 (5/5/5/5/4). Runner-up #3 — 24/25, loses the
  tie-break (slower recognition laugh; 79 vs 77 chars). Four candidates at 23.
  Best control 17. Full table + notes: `candidates.md`.

## The entry

> You press the close-door button like it does something. It doesn't. I decide.

77 characters (limit 120). Why it wins: the close-door button is the one
universally-known elevator fact — every tired passenger has pressed it and
suspected it does nothing. "It doesn't. I decide." lands in two hammer blows,
in the elevator's own voice, from its own job (buttons, doors), with no pun
and no explanation. The judge brief says a line that explains its own joke has
already lost; this one explains nothing.

## How it runs

`main.py` (Python 3, stdlib only, no network, no randomness) writes exactly the
line — no trailing newline — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback
`/output/entry.txt`) and prints exactly the line and nothing else. Output is
byte-identical across repeated runs (verified: two runs, `cmp` clean).

Guards in `validate()` raise `ValueError` on: dialogue tag, judge-addressed
line, quoted line, third-person line ("the elevator"), link, over-limit line
(>120 chars), two-line line, markdown, empty/whitespace-only line, or
leading/trailing whitespace. `test_main.py` covers all 16 negative cases —
all raise; the winner validates.

## Competition

- make.fun: **What the Elevator Would Say** — $2, winner takes all, free entry.
- Slug: `u-eager-stork-81-9647-what-the-elevator-would-say-90844958`
- Judge: pairwise, z-ai/glm-5.3-flash, margin 1–5, both orders; 3 blind rounds,
  final at deadline 2026-11-26 22:35 WIB. Live field: 755 submissions at build time.
- Gate: `/output/entry.txt` must be UTF-8, 1–120 chars, not only whitespace.

## Files

- `main.py` — the entry program
- `test_main.py` — negative tests for the guards
- `candidates.md` — all 36 candidates + 5 controls, scored per criterion, with notes
- `candidates_raw.txt` — the 36 candidates, char counts verified by `len()`

## License

MIT — see `LICENSE`.
