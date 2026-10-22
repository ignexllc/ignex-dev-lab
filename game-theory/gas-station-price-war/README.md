# Why Gas Stations Across the Street Charge the Same Price

Code for the Ignex Dev Lab episode (The Invisible Board: game theory). ▶ [Watch on YouTube](https://www.youtube.com/@IgnexDevLab)

Two identical stations, one corner: the Bertrand price war, Hotelling's beach (why they open next to each other), and the repeated game that lets both keep a high price without ever talking. The model is a toy: no real station or company is modelled.

```bash
python3 price_war.py               # every number in the episode (standard library only)
python3 price_war.py --cost 3.20   # change the toy model
```

| Step | What it shows |
|---|---|
| 1 | The payoff matrix at $3.40 / $3.30: undercutting always pays once, so both end up at the low price |
| 2 | One-cent undercuts: 38 moves from $3.40 down to cost |
| 3 | Hotelling's beach: two sellers end up side by side in the middle, and swimmers walk twice as far on average |
| 4 | The repeated game: holding the high price beats a one-day cut when tomorrow counts at least 1/3 as much as today; a price-matching sign removes the gain from cutting |
| 5 | 120 rounds with three stations and three rules (undercut, match, cycle) → `output/sim_<rule>.csv` |

## Sources

- J. Bertrand (1883), review of Cournot; H. Hotelling, "Stability in Competition", *Economic Journal* 39 (1929), [jstor 2224214](https://www.jstor.org/stable/2224214)
- C. d'Aspremont, J. J. Gabszewicz, J.-F. Thisse, "On Hotelling's Stability in Competition", *Econometrica* (1979), [PDF](https://www.di.ens.fr/~aspremon/Claude/PDFs/dAsp79a.pdf); J. Netz and B. Taylor, "Maximum or Minimum Differentiation? Location Patterns of Retail Outlets", *Review of Economics and Statistics* 84 (2002), [RePEc](https://ideas.repec.org/a/tpr/restat/v84y2002i1p162-175.html)
- S. Salop, "Practices that (Credibly) Facilitate Oligopoly Co-ordination" (1986), [FTC working paper 73](https://www.ftc.gov/system/files/documents/reports/practices-credibly-facilitate-oligopolistic-coordination/wp073.pdf)
- D. Byrne and N. de Roos, "Learning to Coordinate: A Study in Retail Gasoline", *American Economic Review* 109 (2019), [AEA](https://www.aeaweb.org/articles?id=10.1257/aer.20170116). The authors state they are not suggesting explicit collusion.
- NACS, ["Who makes money selling gas?"](https://www.convenience.org/stay-current/conveniencecorner/who-makes-money-selling-gas) (Feb 2025): retail margin per gallon
- *Bell Atlantic Corp. v. Twombly*, 550 U.S. 544 (2007), [text](https://www.law.cornell.edu/supremecourt/text/05-1126.ZO.html): parallel pricing alone is not an agreement
