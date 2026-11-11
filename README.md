# Ignex Dev Lab: the lab notebook

The code behind the videos of **[Ignex Dev Lab](https://www.youtube.com/@IgnexDevLab)**: the math behind money, risk and decisions.

Every number in an episode comes from a public dataset or a small simulation. This repository holds those scripts so you can check the numbers, change the assumptions and run the experiment yourself.

| Episode | Series | Folder |
|---|---|---|
| How 1,000 People Can Predict 100 Million Votes | Statistics & Probability | [`statistics/polls-margin-of-error`](statistics/polls-margin-of-error) |
| Did the Betting Markets Beat the Polls? | Statistics & Probability | [`statistics/betting-markets`](statistics/betting-markets) |
| Why Gas Stations Across the Street Charge the Same Price | The Invisible Board (game theory) | [`game-theory/gas-station-price-war`](game-theory/gas-station-price-war) |
| The 1% Fee That Eats a Third of Your Savings | Money Math | [`money-math/fee-drag-calculator`](money-math/fee-drag-calculator) |

## Run it

Python 3.10 or newer. Each folder has its own README; most scripts use only the standard library, some need `numpy`.

```bash
git clone https://github.com/ignexllc/ignex-dev-lab.git
cd ignex-dev-lab/money-math/fee-drag-calculator
python3 fee_drag.py --fee 1 --years 40
```

## Notes

- Simplified models are labelled as such in the code and in the videos. Data files list their source and download date.
- **Education only, not financial advice.** Nothing here recommends a fund, a product or a trade.
- Found a mistake? Open an issue: corrections are credited in the next episode's description.

Code under the [MIT License](LICENSE).
