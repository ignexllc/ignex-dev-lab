"""Did the Betting Markets Beat the Polls? (archived video, Statistics & Probability #4)

Every simulated number in the video, with the same seed:
  1. three forecasters on 1,000 races: Brier score and calibration
  2. one whale in a thin market and in a thick one (price = money-weighted median belief)
  3. Lucky buys 1,000 five-cent long shots that really win 2 times in 100
  4. Kalshi-style fee 0.07 x P x (1 - P) and the break-even rate at 50 cents

    python3 betting_markets.py            (needs numpy)
Simplified models, labelled as such. Education only, not financial advice.
"""
import numpy as np

rng = np.random.default_rng(2026)

# 1. three forecasters
R = 1000
p_true = rng.uniform(0.05, 0.95, R)                 # each race's real chance
won = rng.random(R) < p_true
logit = lambda p: np.log(p / (1 - p))
sig = lambda x: 1 / (1 + np.exp(-x))
honest = np.clip(sig(logit(p_true) + rng.normal(0, 0.25, R)), 0.01, 0.99)
overconfident = np.clip(sig(2.5 * logit(honest)), 0.01, 0.99)   # same info, shouted toward 0 or 100
coin = np.full(R, 0.5)
brier = lambda f: np.mean((f - won) ** 2)
print("Brier score (lower is better)")
for name, f in (("honest", honest), ("overconfident", overconfident), ("coin", coin)):
    print(f"  {name:14s} {brier(f):.3f}")
m = overconfident >= 0.9
print(f"Overconfident '90%+' calls: {m.sum()}, came true {won[m].mean():.1%}")
print("Calibration (said -> happened, n):")
for name, f in (("honest", honest), ("overconfident", overconfident)):
    rows = []
    for a, b in zip(np.linspace(0, 0.9, 10), np.linspace(0.1, 1, 10)):
        k = (f >= a) & (f < b)
        if k.sum() >= 15:
            rows.append(f"{f[k].mean():.2f}->{won[k].mean():.2f} ({k.sum()})")
    print(f"  {name}: " + ", ".join(rows))


# 2. the whale
def wmedian(v, w):
    o = np.argsort(v)
    v, w = v[o], w[o]
    c = np.cumsum(w)
    return v[np.searchsorted(c, c[-1] / 2)]


def market(n, whale_money, whale_belief=0.95):
    b = np.clip(rng.normal(0.40, 0.10, n), 0.02, 0.98)   # small traders: a 40% shot
    w = np.full(n, 100.0)                                 # $100 each
    before = wmedian(b, w)
    after = wmedian(np.append(b, whale_belief), np.append(w, whale_money))
    return before, after


WHALE = 15_000
for n in (200, 20_000):
    before, after = market(n, WHALE)
    print(f"{n:6d} traders x $100, one ${WHALE:,} whale: price {before * 100:.0f}c -> {after * 100:.0f}c")

# 3. Lucky's long shots
L, price, true_p = 1000, 0.05, 0.02
fee = np.ceil(0.07 * L * price * (1 - price) * 100) / 100     # Kalshi rounds the order's fee up to the cent
wins = (rng.random(L) < true_p).sum()
spent = L * price + fee
print(f"Lucky: {L} tickets at {price * 100:.0f}c, {wins} winners, spent ${spent:.2f} (fee ${fee:.2f}), "
      f"got ${wins:.2f} back, net ${wins - spent:.2f}")

# 4. fees and break-even
print(f"Fee on a 50c ticket: {0.07 * 0.25 * 100:.2f}c -> you must be right {50 + 0.07 * 0.25 * 100:.2f}% of the time to break even")
