# The 1% Fee That Eats a Third of Your Savings

Code for the Ignex Dev Lab episode (Money Math). ▶ [Watch on YouTube](https://www.youtube.com/@IgnexDevLab)

A fee of 1% a year sounds small. Over 40 years you keep 0.99⁴⁰ ≈ 67% of what you would have had, whatever the market returns. This folder is the calculator from the episode, plus every number shown on screen.

```bash
python3 fee_drag.py                     # every number in the episode (standard library only)
python3 fee_drag.py --fee 0.5 --years 30 --amount 20000 --monthly 300 --ret 6   # your own case
```

Options: `--amount` starting balance ($), `--monthly` contribution ($), `--ret` yearly return (%, default 7), `--fee` yearly fee (% of the balance, default 1), `--years` (default 40).

| Step | What it shows |
|---|---|
| 1 | $10,000 for 40 years at 7%: $149,745 without the fee, $100,175 with 1%. You keep 66.9% at any return |
| 2 | Year one: the $107 fee is 15% of the year's gain, not 1% |
| 3 | The $49,570 gap = $16,271 of fees paid + $33,299 of growth those fees would have earned |
| 4 | The fee ladder, from index funds (0.05%) to an adviser plus an active fund (1.64%) |
| 5 | $500 a month for 40 years: you keep 75.4% |
| 6 | 10,000 random markets: the share you keep barely moves (median 76.2%) |
| 7 | The model reproduces the SEC investor bulletin's example |

The model is simple on purpose: one yearly fee on the whole balance, no taxes, a steady or random return. Real returns vary, taxes act like a second fee, and a fee can buy something (advice, help not panicking): the episode covers these limits.

## Sources

- Investment Company Institute, [*Trends in the Expenses and Fees of Funds, 2025*](https://www.ici.org/system/files/2026-03/per32-01.pdf) (ICI Research Perspective 32(1), March 2026): asset-weighted average expense ratios
- M. Kitces, ["Financial Advisor Fees Comparison"](https://www.kitces.com/blog/independent-financial-advisor-fees-comparison-typical-aum-wealth-management-fee/) (2017): a median adviser fee of about 1%
- SEC, [Investor Bulletin: How Fees and Expenses Affect Your Investment Portfolio](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-how-fees-expenses-affect-your)
- Morningstar, [*Mind the Gap 2025*](https://www.morningstar.com/business/insights/research/mind-the-gap-2025); Vanguard, [*Advisor's Alpha*](https://www.vanguard.ca/content/dam/intl/americas/canada/en/documents/gas/quantifying-your-value-to-clients-advisor.pdf)

**Education only, not financial advice.** No fund, product or provider is recommended.
