# How 1,000 People Can Predict 100 Million Votes

Code for the Ignex Dev Lab episode (Statistics & Probability). ▶ [Watch on YouTube](https://www.youtube.com/@IgnexDevLab)

Where a poll's "±3.1%" comes from, why the size of the country barely matters, and the errors no sample size fixes (non-response, weighting). The episode explains the mechanism only: no prediction, no side taken.

```bash
pip install numpy
python3 polls.py                         # every number in the episode
python3 polls.py --n 2500 --truth 0.48   # your own poll
```

| Step | What it shows |
|---|---|
| 1 | Margin of error = 1.96 × √(p(1−p)/n): ±3.1 points at n = 1,000; 9,604 people for ±1 point |
| 2 | The finite-population correction: a town of 10,000 or a country of 100 million gives almost the same margin |
| 3 | 10,000 simulated polls of a population with 52% for A: about 95% land within ±3.1 points, and about 1 in 10 shows A behind |
| 4 | Non-response bias: a 6.0% vs 5.5% answer rate turns a 50/50 town into 52/48, even in a poll of a million |
| 5 | Weighting: fixing an unbalanced sample shrinks its effective size (1,000 → 800) |
| 6–7 | Real polls vs results: the 2022 House generic ballot and AAPOR's 2000–2020 errors |

Data and sources: [`data/SOURCES.md`](data/SOURCES.md).
