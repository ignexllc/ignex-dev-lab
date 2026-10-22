"""The 1% fee that eats a third of your savings (Ignex Dev Lab, Money Math).

    python3 fee_drag.py                                   # every number in the episode
    python3 fee_drag.py --fee 0.5 --years 30 --amount 20000 --monthly 300 --ret 6   # your own case

Fee model: the fund takes `fee` of the balance once a year, after the year's market return.
    balance(next year) = balance × (1 + return) × (1 − fee)
For a lump sum you keep (1 − fee)^years of the no-fee result, whatever the return.
The 7% return is an illustration, not a forecast. Education only, not financial advice. Standard library only.
"""
import argparse
import random


def grow(p0, r, fee, years, monthly=0.0):
    """Balance at each year end. Monthly contributions grow at the monthly-equivalent rate;
    the fee is taken at each year end on the whole balance."""
    b, path = p0, [p0]
    rm = (1 + r) ** (1 / 12) - 1
    for _ in range(years):
        for _ in range(12):
            b = b * (1 + rm) + monthly
        b *= 1 - fee
        path.append(b)
    return path


def money(x):
    return f"${x:,.0f}"


def calculator(amount, monthly, ret, fee, years):
    gross, net = grow(amount, ret, 0, years, monthly)[-1], grow(amount, ret, fee, years, monthly)[-1]
    paid_in = amount + monthly * 12 * years
    print(f"start {money(amount)}, {money(monthly)} a month, {ret:.1%} a year, fee {fee:.2%}, {years} years")
    print(f"you put in:        {money(paid_in)}")
    print(f"without the fee:   {money(gross)}")
    print(f"with the fee:      {money(net)}")
    print(f"the fee costs you: {money(gross - net)}  -> you keep {net / gross:.1%}")
    if gross > paid_in:
        print(f"share of your GAINS that goes to the fee: {(gross - net) / (gross - paid_in):.1%}")


def episode():
    P, R, F, Y = 10_000, 0.07, 0.01, 40
    gross, net = grow(P, R, 0, Y), grow(P, R, F, Y)

    print("--- 1. $10,000 for 40 years at 7%, with and without a 1% fee ---")
    print(f"without the fee {money(gross[-1])}, with it {money(net[-1])}: you keep {net[-1] / gross[-1]:.1%}  (0.99^40 = {0.99 ** 40:.4f})")
    print(f"the quick shortcut, 7% becomes 6%: you keep {(1.06 / 1.07) ** 40:.1%}. Either way, about a third is gone")
    print("the share you keep does not depend on the return:",
          ", ".join(f"{r:.0%} -> {grow(P, r, F, Y)[-1] / grow(P, r, 0, Y)[-1]:.1%}" for r in (0.03, 0.05, 0.07, 0.10)))

    print("\n--- 2. Year one: the fee looks tiny ---")
    y1 = P * (1 + R)
    print(f"balance {money(y1)}, fee {money(y1 * F)} = {y1 * F / (y1 - P):.1%} of the year's {money(y1 - P)} gain")

    print("\n--- 3. Where the gap comes from ---")
    fees_paid, b = 0.0, P
    for _ in range(Y):
        b *= 1 + R
        fees_paid += b * F
        b *= 1 - F
    gap = gross[-1] - net[-1]
    print(f"gap {money(gap)} = fees actually paid {money(fees_paid)} + growth those fees would have earned {money(gap - fees_paid)}")
    print("gap by year:", ", ".join(f"year {t}: {money(gross[t] - net[t])}" for t in (1, 5, 10, 20, 30, 40)))

    print("\n--- 4. The fee ladder (ICI 2025 averages, typical adviser fee): share kept after 40 years ---")
    ladder = [("index stock mutual funds", 0.0005), ("index stock ETFs", 0.0014), ("all stock mutual funds", 0.0040),
              ("active stock mutual funds", 0.0064), ("typical adviser fee", 0.01),
              ("adviser + active fund", 0.0164), ("1 stock fund in 10 charges this or more", 0.0184)]
    for name, f in ladder:
        print(f"  {f:6.2%}  {name:42s} keep {(1 - f) ** 40:5.1%}   cost on $10,000: {money(gross[-1] - grow(P, R, f, Y)[-1])}")

    print("\n--- 5. Saving $500 a month for 40 years ---")
    calculator(0, 500, R, F, Y)

    print("\n--- 6. 10,000 random markets (average 7%, swings of ±15% a year; an illustration) ---")
    rng = random.Random(7)
    keeps = []
    for _ in range(10_000):
        bg = bn = 0.0
        for r in (rng.gauss(R, 0.15) for _ in range(Y)):
            rm = (1 + r) ** (1 / 12) - 1 if r > -1 else -1
            for _ in range(12):
                bg = bg * (1 + rm) + 500
                bn = bn * (1 + rm) + 500
            bn *= 1 - F
        keeps.append(bn / bg)
    keeps.sort()
    p5, p50, p95 = (keeps[int(q * 9999)] for q in (0.05, 0.5, 0.95))
    print(f"share kept with $500 a month: median {p50:.1%}, 90% of markets between {p5:.1%} and {p95:.1%}")

    print("\n--- 7. Check against the SEC's investor bulletin ($100,000, 4%, 20 years) ---")
    print(", ".join(f"fee {f:.2%}: {money(100_000 * (1.04 * (1 - f)) ** 20)}" for f in (0.0025, 0.005, 0.01)))


def main():
    ap = argparse.ArgumentParser(description="Fee drag calculator. No options = the episode's numbers.")
    ap.add_argument("--amount", type=float, help="starting balance ($)")
    ap.add_argument("--monthly", type=float, help="monthly contribution ($)")
    ap.add_argument("--ret", type=float, help="yearly return in %% (default 7)")
    ap.add_argument("--fee", type=float, help="yearly fee in %% of the balance (default 1)")
    ap.add_argument("--years", type=int, help="years invested (default 40)")
    a = ap.parse_args()
    if all(v is None for v in vars(a).values()):
        episode()
    else:
        calculator(a.amount if a.amount is not None else 10_000, a.monthly or 0.0,
                   (a.ret if a.ret is not None else 7) / 100, (a.fee if a.fee is not None else 1) / 100, a.years or 40)
    print("\nEducation only, not financial advice.")


if __name__ == "__main__":
    main()
