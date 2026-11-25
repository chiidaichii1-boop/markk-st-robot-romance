# Robot Romance: One-Line Pickup Lines for AI

![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)
![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/chiidaichii1-boop/markk-st-robot-romance/rank.svg)
![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/chiidaichii1-boop/markk-st-robot-romance/reward.svg)

[Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

## Entry

One single-line pickup line, written to charm an AI — built on the
attention-mechanism premise instead of the worn battery / charging /
reboot moves:

> Are you my attention mechanism? Because in a room full of tokens, you're the only one I keep attending to.

## How it works

`main.py` (Python 3, stdlib only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`).
It never deletes the output folder — it creates it if missing and
writes inside it. The run is fully deterministic: the same line,
byte for byte, every time.
