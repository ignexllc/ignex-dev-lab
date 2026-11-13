# PMC Studio: code and data

The code behind the videos of **[PMC Studio - Statistics & Economics](https://www.youtube.com/@PMCStudioStats)**: the hard ideas in statistics and economics, derived and made visible.

Every number in a video comes from a public dataset or a short simulation. This repository holds those scripts so you can check the numbers, change the assumptions and rerun the analysis yourself.

| Folder | What's inside |
|---|---|
| [`statistics/`](statistics) | Statistics, Derived: Bayes' theorem, the Poisson distribution, the central limit theorem, hypothesis tests, confidence intervals, regression, maximum likelihood |
| [`economics/`](economics) | Economics, Derived: tax incidence, money creation, comparative advantage, inflation and expectations |
| [`finance/`](finance) | Finance Math, Derived: discounting, duration, risk and return |
| [`worked-problems/`](worked-problems) | the solutions of the Worked Problems videos, step by step |
| [`data-projects/`](data-projects) | one real dataset, one question, the full analysis |
| [`archive/`](archive) | code for the channel's earlier videos |

Each video gets one folder with its own README, the script (fixed random seeds, so you get the numbers shown on screen) and its data with source and download date.

## Run it

Python 3.10 or newer; most scripts need only `numpy` (and `pandas` for the data projects).

```bash
git clone https://github.com/ignexllc/pmc-studio.git
cd pmc-studio/statistics/<video-folder>
python3 <script>.py
```

## Notes

- Simplified models are labelled as such in the code and in the videos.
- Finance material is **education only, not financial advice.**
- Found a mistake? Open an issue: corrections are credited in the next video's description.

Code under the [MIT License](LICENSE).
