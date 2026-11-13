# Did the Betting Markets Beat the Polls?

Earlier video of the channel · Statistics & Probability #4 (November 2026). Archived.

After the US midterms of November 3, 2026, we score the betting markets and the poll-based forecast models the way weather forecasters are scored, then look at why a crowd can be right on average while most of the people in it lose money.

`betting_markets.py` recomputes every simulated number in the video (seed 2026):

- **Brier score and calibration:** three forecasters (honest, overconfident, a coin) on 1,000 simulated races.
- **The whale:** the price as the money-weighted median belief. One $15,000 whale moves a 200-trader market from 40¢ to 51¢; in a 20,000-trader market it doesn't move it.
- **Long shots:** 1,000 five-cent tickets that really win 2 times in 100, with a Kalshi-style fee.
- **Fees:** the break-even win rate on a 50¢ ticket.

```bash
pip install numpy
python3 betting_markets.py
```

## Sources (real-world numbers in the video)

- Election-eve market prices and Brier scores of the control markets: RotoWire, "How Accurate Were the 2026 Midterm Markets?" (Nov 2026).
- Iowa Electronic Markets vs 964 polls, 1988–2004: Berg, Nelson & Rietz (2008), International Journal of Forecasting 24(2).
- Brier score: G. W. Brier (1950), Monthly Weather Review 78.
- Favourite-longshot bias on Kalshi (46,282 contracts, 2021–2025): Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market".
- Wallet concentration on Polymarket's 2026 congressional markets: Anti-Corruption Data Collective, "Gambling on Democracy" (Aug 2026).
- Kalshi fee schedule: 0.07 × contracts × P × (1 − P), rounded up to the cent.

The full list with links is in the video description.

Simplified models, labelled as such. **Education only, not financial advice.**
