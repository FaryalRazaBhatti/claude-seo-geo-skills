# Example: competitor analysis for Apple (UK)

> Test run of the `competitor-analysis` skill on public pages, 12 November 2026. Shown from Apple's point of view as a worked example. Not affiliated with or endorsed by Apple, Samsung or Google.

## What was analysed

| Site | Source | Notes |
|---|---|---|
| apple.com/uk | UK sitemap (476 URLs) | No `lastmod` dates in the sitemap. No blog; content is product, explainer and comparison pages |
| samsung.com/uk | 2 of 7 child sitemaps, partly read | Sitemaps truncated when fetched, so counts are a sample. Has a large "Explore" blog |
| store.google.com/gb | GB sitemap, partly read | Product and spec pages only. Google's editorial content lives on other sites, not analysed here |

**Data used:** content coverage only. No traffic, ranking or keyword data was provided, so nothing below is a performance figure.

**Limits:** Apple's support site and Google's blog were not checked; both likely hold content on topics marked thin here. Samsung counts are from a partial sample.

## Topic matrix (sample)

| Topic | Apple | Samsung | Google Store | State |
|---|---|---|---|---|
| Switching phones | 6 switch pages, undated | 1 buying guide page | 0 | Contested (search led by publishers) |
| Comparing models | 15 compare pages | Compare pages per category | Spec pages | Contested |
| Privacy and security | 4 hub pages | 3 pages | 0 | Contested |
| Accessibility | 4 pages | 8 pages, updated 2024 to 2026 | 0 | Contested, Samsung deeper |
| Kids and family safety | 5 pages | 2 blog posts (2022, 2024) | 0 | Contested |
| Sustainability and batteries | 6 pages | 1 blog post (2022) plus sustainability section | 0 | Contested |
| Buying guides ("which should I buy") | 0 | Phone and laptop buying guide sections | 0 | Thin for Apple |
| Photography how-to | 0 in UK sitemap | 14 blog posts, all 2020 to 2023 | 0 | Thin (stale) |
| Education and success stories | 95 pages | 0 | 0 | Dominated by Apple |
| Lifestyle (recipes, wellbeing) | 0 | ~70 blog posts, mostly 2020 to 2023 | 0 | Off-topic |

## Quality comparison: switching phones

| | Apple: iPhone switch page | Samsung: why Android guide |
|---|---|---|
| Direct answer | 1 | 1 |
| Evidence | 1 (links to own support pages) | 0 (statistics with no sources) |
| Experience | 0 | 0 |
| Freshness | 0 (no visible date) | 0 (date only in page code) |
| Depth | 2 (transfer, WhatsApp, trade-in, number) | 1 (no WhatsApp, no cost) |
| Structure | 1 (no steps, no FAQ) | 2 (question headings) |
| **Total** | **5 / 12** | **4 / 12** |

Biggest difference: Apple covers more of the buyer's questions, but neither page gives actual step-by-step instructions. That's why publishers such as TechRadar, Uswitch and giffgaff lead search for this question.

## Decisions

| Topic | Relevance | Gap | Winnability | Decision |
|---|---|---|---|---|
| Switching phones | 3 | 1 | 3 | **Update**: add numbered steps, an FAQ and a visible date to the switch page |
| Buying guides | 3 | 2 | 2 | **Own**: a "which iPhone/Mac is right for you" guide, not just spec tables |
| Accessibility | 2 | 1 | 3 | **Update**: one page per key feature, as Samsung does |
| Photography how-to | 2 | 2 | 3 | **Check first**: may already exist on Apple's support or other sites |
| Comparing models | 3 | 1 | 3 | **Own** (already strong; keep current) |
| Privacy and security | 3 | 1 | 2 | **Own through others**: buyers read third-party "best phone for privacy" lists, so PR and reviews matter more than another page |
| Lifestyle | 0 | 3 | 1 | **Skip**: no link to what buyers want from the site |

## What this test changed in the skill

- Big sites split sitemaps by country and by section, and nest them. The skill now picks the market from the site profile and follows nested sitemaps, with a cap.
- Brand sites often have no blog. The skill now decides what counts as content for each site before counting.
- Content often lives on other domains (support, blog, newsroom). The skill now checks for these and says when it hasn't.
- Sitemap dates can be missing or bulk-updated (many Samsung posts share one date). The skill no longer treats them as freshness on their own.
- Off-topic content is now labelled and kept out of topic counts.
