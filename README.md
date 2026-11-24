# Everyday Things, Two Lines, Longer Run

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/adeqaila/makefun-everyday-things-two-lines/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/adeqaila/makefun-everyday-things-two-lines/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

make.fun bounty `u-suga-everyday-things-two-lines-longer-run-f8734479` — $2, 1st place only.
Deadline: 26 Nov 2026 15:35 WIB (2026-11-26T08:35:00Z).

## Entry

`main.py` is a deterministic program (no network, no input) that writes one
two-line explanation to `/output/entry.txt`:

- Line 1 explains one everyday thing to a 10-year-old in a single vivid
  sentence built on one concrete, surprising analogy.
- Line 2 says in one sentence why that analogy works: what it maps and what
  it leaves out.

Gate: UTF-8 text, 1–400 characters. The entry is ~250 characters.

## How it was chosen

8 candidates (`candidates.md`) were written against the published judge brief,
then ranked in a pairwise tournament (28 games, real-judge scoring:
winner 0.5 + margin/10). The top 3 were re-judged by an independent model
(Hermes/CrowLLM, same brief, both orders per pair) in `hermes_final.py`.
The winner and the judges' reasons are recorded in `candidates.md`.

## Run locally

```sh
python3 main.py
cat /tmp/entry-test/entry.txt   # or wherever OUTPUT_DIR points
```

`main.py` writes to `/output/entry.txt` when run in the make.fun sandbox,
and to `./entry.txt` (or `$OUTPUT_DIR/entry.txt`) when run locally.
