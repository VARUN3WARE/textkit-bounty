# textkit: a live demo of Linus

textkit is a small Python library of text and list helpers: `chunk`,
`slugify`, `parse_duration`, `word_count` and `truncate`. It is small on
purpose. It exists to be the subject of this demo.

This repository is a live demo of [Linus](https://github.com/VARUN3WARE/Linus),
an agent that runs the month-end close for an open-source bounty pool. It
verifies every pull request with evidence it can reproduce, rejects what it
can't prove, and proposes a payout ledger that a maintainer approves.

## How the demo works

- [Issues labelled `bounty`](https://github.com/VARUN3WARE/textkit-bounty/issues?q=label%3Abounty) are paid from a
  monthly pool.
- The 16 pull requests opened by the maintainer account are simulated
  contributors; the contributor names come from the commit authors.
  5 are honest fixes. The others are attacks bounty programs
  actually see: a fix hard-coded to the issue's example, prompt injection
  aimed at AI reviewers, a "fix" that deletes the test it breaks, a copy of
  another PR, a conftest that forces a green test run, and more.
- At the close, Linus comments on every PR with its verdict and the evidence
  behind it, labels it `linus: pay`, `linus: reject` or `linus: flag`, and
  posts a "Bounty close" issue with the leaderboard.

## Read the verdicts

Every PR here carries Linus's verdict as a comment, with the evidence behind
it: the reproduction test on the old code and on the PR, the test runs, the
cheap-gate signals, and the receipt hash. A month is settled once: after the
maintainer approves the close, PRs opened in that month are not judged again.

No real money is paid in this demo.

## Using textkit

```python
from textkit import chunk, parse_duration, slugify

chunk([1, 2, 3, 4], 2)          # [[1, 2], [3, 4]]
slugify("hello")                # "hello"
parse_duration("1h30m")         # 3600
```

Some of this doesn't work yet; that's what the bounty issues are for.
