# Example: GEO visibility check for Apple (UK)

> Test run of the `geo-visibility` skill, 12 November 2026, as a worked example. Not affiliated with or endorsed by Apple, Samsung or Google.
>
> **Method: search-grounded check only.** A browser wasn't available, so this run looked at what web search surfaces for each question, which is what many AI tools draw on. It is **not** a record of what ChatGPT, Gemini or Perplexity actually answered. A full run uses browser or paste mode.

## Question set

| ID | Question | Type |
|---|---|---|
| Q1 | best smartphone for privacy UK | Category (unbranded) |
| Q2 | how to switch from Android to iPhone | Problem (branded) |
| Q3 | iPhone vs Samsung Galaxy which is better | Comparison (branded) |
| Q4 | best laptop for university students UK | Category (unbranded) |
| Q5 | is Apple Trade In worth it UK | Brand |
| Q6 | best smartwatch for fitness tracking UK | Category (unbranded) |

## Headline numbers (unbranded questions only)

Branded questions mention the brand by definition, so they're kept out of the headline.

| | Apple | Samsung | Google |
|---|---|---|---|
| Products mentioned in top results | 3 / 3 | 2 / 3 | 2 / 3 |
| Own website among top results | 0 / 3 | 0 / 3 | 0 / 3 |

Across all six questions, Apple's own site didn't appear in the top results once. Apple is visible through other people's content, not its own.

## Where the answers come from

Most frequent sources across the six questions: TechRadar, Expert Reviews, Which?, Digital Trends, Uswitch, mobiles.co.uk, whatsthebest.co.uk, Swappa and Yahoo. Spam and hijacked domains in the results were excluded.

These publishers, review and comparison sites are where buyers, and the AI tools that summarise for them, get their information in this market.

## Issues found

1. **Sentiment on Trade In (Q5).** The top results are mostly negative: a major publisher concluding it isn't a good deal, comparison sites claiming higher prices elsewhere, and review complaints about the trade-in partner. An AI answer built on these sources is likely to steer people away.
2. **Outdated information.** Several top results compare or recommend models that are years old. AI answers that lean on these risk recommending outdated products.
3. **No citable how-to of its own (Q2).** Publishers' step-by-step guides lead, while Apple's own switch page has no numbered steps.

## Top fixes

1. **Trade In:** publish a clear, current page on how values are set and what to expect, and address it on the sources that rank (Q5).
2. **Publisher roundups:** make sure current models reach the outlets that dominate category questions, so fresh reviews replace old ones (Q1, Q4, Q6).
3. **Switch page:** add numbered steps and an FAQ so it can be quoted directly (Q2).
4. **Rerun in browser mode** across ChatGPT, Google AI Overviews, Gemini and Perplexity with the same question set, to measure real AI answers.

## What this test changed in the skill

- Branded and unbranded questions are now scored separately, so branded questions can't inflate the headline numbers.
- Added a sentiment field, because being mentioned negatively is a different problem from not being mentioned.
- Added "outdated" as an accuracy problem.
- Defined exactly what search-grounded mode records, and that it must always be labelled.
- Spam and hijacked domains are now excluded from source counts.
