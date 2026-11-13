"""How 1,000 people can predict 100 million votes (archived video, Statistics & Probability).

Every number in the episode, recomputed:
    python3 polls.py                      # the episode's numbers
    python3 polls.py --n 2500 --truth 0.48  # try your own poll

Needs numpy. The simulated population is abstract (option A vs option B): no real candidate or party.
"""
import argparse
import csv
import math
import pathlib

import numpy as np

DATA = pathlib.Path(__file__).parent / "data"


def margin_of_error(n, p=0.5, z=1.96):
    """95% margin of error of a share p estimated from a simple random sample of n people."""
    return z * math.sqrt(p * (1 - p) / n)


def section(title):
    print(f"\n--- {title} ---")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000, help="people per poll")
    ap.add_argument("--truth", type=float, default=0.52, help="true share of option A in the population")
    ap.add_argument("--polls", type=int, default=10_000, help="how many polls to simulate")
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    n = a.n

    section("1. The margin of error (worst case p = 0.5)")
    se = math.sqrt(0.25 / n)
    print(f"standard error at n = {n:,}: {se * 100:.2f} points")
    print(f"95% margin of error: ±{margin_of_error(n) * 100:.1f} points  (1.96 × {se * 100:.2f})")
    for k in (100, 400, 1000, 4000, 10_000):
        print(f"  n = {k:>6,}: ±{margin_of_error(k) * 100:.1f} points")
    print(f"people needed for ±1 point: {(1.96 / 0.01) ** 2 * 0.25:,.0f}")
    print(f"margin on the LEAD (A minus B) in a two-option poll: ±{2 * margin_of_error(n) * 100:.1f} points")

    section("2. The size of the country barely matters")
    for N in (10_000, 100_000_000):
        fpc = math.sqrt((N - n) / (N - 1))
        print(f"population {N:>11,}: ±{margin_of_error(n) * fpc * 100:.2f} points")

    section(f"3. Simulate {a.polls:,} polls of {n:,} people (true share of A = {a.truth:.0%})")
    rng = np.random.default_rng(a.seed)
    polls = rng.binomial(n, a.truth, size=a.polls) / n
    moe = margin_of_error(n, a.truth)
    print(f"average of the polls: {polls.mean() * 100:.2f}%   spread (sd): {polls.std() * 100:.2f} points")
    print(f"polls within ±{moe * 100:.1f} of the truth: {np.mean(np.abs(polls - a.truth) <= moe) * 100:.1f}%")
    print(f"polls that show A behind (< 50%): {np.mean(polls < 0.5) * 100:.1f}%")
    print(f"lowest poll {polls.min() * 100:.1f}%, highest {polls.max() * 100:.1f}%")

    section("4. Non-response: a 50/50 town where A's voters answer a bit more often")
    rA, rB = 0.060, 0.055
    share = rA / (rA + rB)
    print(f"A answers 6.0% of calls, B 5.5% -> the poll sees A at {share * 100:.1f}% (truth 50%)")
    big = rng.binomial(1_000_000, share) / 1_000_000
    print(f"a 1,000,000-person poll with the same bias: {big * 100:.2f}%  (more people do not fix bias)")

    section("5. Weighting costs precision")
    w_young, w_old = 0.40 / 0.20, 0.60 / 0.80          # 200 under-35s should be 40%, 800 others 60%
    w = np.array([w_young] * 200 + [w_old] * 800)
    neff = w.sum() ** 2 / (w ** 2).sum()
    print(f"weights: under-35s ×{w_young:.2f}, others ×{w_old:.2f} -> effective sample {neff:.0f}, margin ±{margin_of_error(neff) * 100:.1f}")

    section("6. Real data: 2022 US House elections (national, both parties shown the same way)")
    votes = {r["party"]: int(r["votes"]) for r in csv.DictReader(open(DATA / "house_2022_popular_vote.csv"))}
    tot = sum(votes.values())
    R, D = votes["Republican"] / tot * 100, votes["Democratic"] / tot * 100
    print(f"votes counted: {tot:,}   Republican {R:.1f}%   Democratic {D:.1f}%   margin R+{R - D:.1f}")
    for r in csv.DictReader(open(DATA / "generic_ballot_2022_final.csv")):
        m = float(r["final_average_margin_R_minus_D"])
        print(f"  {r['source']} final polling average R+{m}: missed the margin by {R - D - m:+.1f} points")

    section("7. National polling error in presidential years (AAPOR 2021)")
    print("year  signed error (+ = Democratic margin overstated)  absolute error")
    for r in csv.DictReader(open(DATA / "aapor_national_signed_error.csv")):
        print(f"{r['year']}  {float(r['signed_error']):+.1f}{'':39s}{r['absolute_error']}")


if __name__ == "__main__":
    main()
