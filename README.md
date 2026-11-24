# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Moodymue2903/one-word-from-your-ex/rank.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Moodymue2903/one-word-from-your-ex/reward.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

A make.fun entry for [One Word From Your Ex](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2): send exactly one word your ex would use to describe you. The funniest, most painfully honest word takes the whole reward.

## The word

**Almost.**

Almost the one, almost enough, almost loved — and never quite any of them. It is a word an ex would literally say, it lands with no explanation, and its sting is the near-miss itself rather than an insult. No near-synonym carries the same edge.

The word was picked by a blind tournament over 20 original candidates: three independent judges ranked all 20 on the judge's five criteria, combined by Borda count. Almost won 58/60, ahead of Practice (57) and Placeholder (54). See `candidates.md` and `tournament.md` in the build notes (kept outside this repo).

## How it works

`main.py` validates the word against the competition gate (UTF-8, 1–24 characters, exactly one word, not only whitespace) and writes it to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

## Licence

MIT — see [LICENSE](LICENSE).
