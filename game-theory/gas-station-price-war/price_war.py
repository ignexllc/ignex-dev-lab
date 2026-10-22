"""Why gas stations across the street charge the same price (Ignex Dev Lab, The Invisible Board).

Every number in the episode, recomputed (standard library only):
    python3 price_war.py              # prints the numbers, writes output/sim_<rule>.csv
    python3 price_war.py --cost 3.20  # change the toy model

Toy model (an illustration, as in the video): two identical stations across the street, cost $3.00 a gallon
(wholesale + taxes + delivery), 2,000 gallons a day sold at the corner in total. The cheaper station gets every
driver; equal prices split the drivers 50/50. No real station or company is modelled.
"""
import argparse
import csv
import pathlib

OUT = pathlib.Path(__file__).parent / "output"
COST, Q = 3.00, 2000
HIGH, LOW = 3.40, 3.30


def profit(p_me, p_rival):
    """A station's profit for a day at the corner."""
    if p_me < p_rival - 1e-9:
        share = 1.0
    elif abs(p_me - p_rival) < 1e-9:
        share = 0.5
    else:
        share = 0.0
    return round((p_me - COST) * Q * share, 2)


def undercut_ladder(start=HIGH, step=0.01):
    """Bertrand: each station in turn undercuts the other by one cent while that still beats matching."""
    p, steps, i = [start, start], [(start, start)], 0
    while True:
        cand = round(p[1 - i] - step, 2)
        if cand < COST - 1e-9 or profit(cand, p[1 - i]) <= profit(p[1 - i], p[1 - i]):
            break
        p[i] = cand
        steps.append(tuple(p))
        i = 1 - i
    return steps


def avg_walk(a, b, n=100_000):
    """Hotelling's beach (1 mile): average walk to the nearest of two sellers at a and b."""
    return sum(min(abs((k + 0.5) / n - a), abs((k + 0.5) / n - b)) for k in range(n)) / n


def simulate(rule, rounds=120, n=3, start=HIGH):
    """Three stations move in turn.
    undercut: one cent below the lowest rival (never below cost)
    match:    match the lowest rival; a test cut at round 30, a raise at round 60 that the others follow
              (a price-matching sign / price leadership)
    cycle:    undercut by 2 cents until near cost, then jump back to the high price
              (an Edgeworth cycle, the sawtooth seen in some real fuel markets)"""
    p = [start] * n
    rows = [[0, *p]]
    for t in range(1, rounds + 1):
        i = t % n
        rivals = [p[j] for j in range(n) if j != i]
        low = min(rivals)
        if rule == "undercut":
            p[i] = round(max(COST, low - 0.01), 2)
        elif rule == "match":
            if t == 30:
                p[2] = round(HIGH - 0.05, 2)
            elif t == 60:
                p[0] = HIGH
            elif t > 60:
                p[i] = max(rivals)
            else:
                p[i] = low
        elif rule == "cycle":
            p[i] = HIGH if low <= COST + 0.02 else round(max(COST, low - 0.02), 2)
        rows.append([t, *p])
    return rows


def main():
    global COST, Q
    ap = argparse.ArgumentParser()
    ap.add_argument("--cost", type=float, default=COST, help="cost per gallon ($)")
    ap.add_argument("--gallons", type=int, default=Q, help="gallons a day sold at the corner")
    a = ap.parse_args()
    COST, Q = a.cost, a.gallons

    print(f"--- 1. The payoff matrix (profit per day, cost ${COST:.2f}, {Q:,} gal/day) ---")
    print(f"{'':14s}{'B at $' + format(HIGH, '.2f'):>20s}{'B at $' + format(LOW, '.2f'):>20s}")
    for pa in (HIGH, LOW):
        cells = [f"A {profit(pa, pb):>5.0f} / B {profit(pb, pa):>5.0f}" for pb in (HIGH, LOW)]
        print(f"A at ${pa:.2f}   " + "   ".join(f"{c:>17s}" for c in cells))

    ladder = undercut_ladder()
    print(f"\n--- 2. The price war (Bertrand) ---")
    print(f"one-cent undercuts: {len(ladder) - 1} moves, from ${ladder[0][0]:.2f} down to "
          f"${ladder[-1][0]:.2f} / ${ladder[-1][1]:.2f} (cost ${COST:.2f})")

    print(f"\n--- 3. Hotelling's beach (1 mile) ---")
    print(f"sellers at the quarters: average walk {avg_walk(0.25, 0.75):.4f} mi, longest 0.25 mi")
    print(f"both in the middle:      average walk {avg_walk(0.5, 0.5):.4f} mi, longest 0.5 mi")

    coop, cheat = profit(HIGH, HIGH), profit(LOW, HIGH)
    print(f"\n--- 4. The game that never ends (grim trigger) ---")
    print(f"both hold ${HIGH:.2f}: ${coop:.0f} a day each, every day")
    print(f"cheat once at ${LOW:.2f}: ${cheat:.0f} for one day, then a price war at cost ($0) forever")
    print(f"holding the high price pays when tomorrow counts at least {1 - coop / cheat:.4f} of today (1/3)")
    print(f"if the rival matches the cut at once (a price-matching sign): ${profit(LOW, LOW):.0f} a day each, so cutting gains nothing")

    print(f"\n--- 5. Simulated 120 rounds, three stations ---")
    OUT.mkdir(exist_ok=True)
    for rule in ("undercut", "match", "cycle"):
        rows = simulate(rule)
        with open(OUT / f"sim_{rule}.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["round", "a", "b", "c"])
            w.writerows(rows)
        avg = sum(sum(r[1:]) / 3 for r in rows[1:]) / (len(rows) - 1)
        print(f"{rule:9s} average price ${avg:.3f}, average margin {(avg - COST) * 100:.0f} cents a gallon"
              f" -> output/sim_{rule}.csv")

    print("\n--- 6. Real-world anchor (NACS, Feb 2025) ---")
    print("US retail fuel: about 35 cents a gallon above the fuel's cost, about 22 cents of it running costs, about 13 cents profit")


if __name__ == "__main__":
    main()
