---
name: geo-visibility
description: Test how often AI tools (ChatGPT, Gemini, Perplexity, Google AI Overviews, Copilot, Claude) mention and cite a brand for the questions that matter, compare with competitors, and turn the gaps into content and PR fixes. Use for GEO, AEO, AI visibility, AI share of voice, "does ChatGPT mention us", or AI search audits.
---

# GEO visibility check

This skill measures one thing properly: **when real people ask AI tools the questions that matter, does this brand come up, is it cited, and is what's said about it accurate?**

The method is designed to be repeatable. The same question set runs each time, so results can be compared month to month instead of being one-off screenshots.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/geo-visibility/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## Google vs other AI tools

- **Google AI Overviews and AI Mode:** Google says these run on its normal ranking systems, so improving visibility there is SEO. Its own data is in Search Console's Generative AI performance report; use `search-console-analysis` for that. This skill adds what Search Console can't show: what the answers actually say.
- **ChatGPT, Gemini app, Perplexity, Copilot, Claude and others:** no equivalent public data exists, so checking the answers directly is the only way to measure them.

## What this skill can and can't do

- **Can:** ask the questions (in a browser, or using answers the user pastes), record and score the answers, and diagnose gaps.
- **Can't:** see how any AI tool chooses its sources, or produce numbers that are stable from run to run. Treat results as a snapshot.

## Before you start

1. Read the site profile and `references/google-guidance.md`. You need the brand name and other names, website, competitors, and priority questions. Follow its house rules.
2. If there are no priority questions, draft 15 to 20 using the mix in step 1, show them to the user, and wait for approval. The question set is the foundation; don't run on questions the user hasn't agreed.
3. Ask which AI tools matter for their audience. Default to ChatGPT, Google AI Overviews / AI Mode, Gemini and Perplexity.

## Step 1: Lock the question set

A good set covers different ways people ask:

- **Category:** "best [category] for [need]"
- **Problem:** "how do I [problem the brand solves]"
- **Comparison:** "[brand] vs [competitor]", "alternatives to [competitor]"
- **Brand:** "is [brand] any good", "what does [brand] do"
- **Local**, if relevant: "[service] near [place]"

Write them as a person would say them, not as keywords. Tag each question **branded** (it names the brand or its products) or **unbranded**. Branded questions mention the brand by definition, so they're scored separately. Make at least half the set unbranded. Save as `questions.csv` with an ID and type for each question. On reruns, reuse this file unchanged; add new questions with new IDs instead of editing old ones.

## Step 2: Collect answers

Use the best method available, and record which one you used:

- **Browser mode:** if browser tools are available, open each AI tool, ask each question in a fresh chat, and copy the full answer plus any cited links. Use a logged-out or fresh session where possible.
- **Paste mode:** if not, give the user the question list and ask them to paste each tool's answers into a file. Keep this easy: one tool at a time, numbered answers.
- **Search-grounded check (fallback):** if neither of the above is possible, search the web for each question and record what the top results show: whether the brand's own site appears, whether the brand or its products are mentioned, which domains appear, and the general sentiment. This shows the sources AI tools are likely to draw on, but it is not an AI answer. Label every output from this mode clearly, never present it as another tool's answer, and recommend a rerun in browser or paste mode.

AI answers vary between runs. Where time allows, ask each question twice and note if the answers differ. Record the date, tool, mode, and location if known.

Never fill in an answer you didn't actually collect.

## Step 3: Record each answer

For every question and tool, record in `results.csv`:

| Field | Values |
|---|---|
| question_id, tool, date, run | |
| brand_mentioned | yes / no |
| mention_position | first / early / later / none |
| brand_cited | yes / no (a link to the brand's own site) |
| cited_url | the brand page cited, if any |
| sentiment | positive / neutral / negative / mixed |
| accuracy | correct / outdated / partly wrong / wrong / n/a, plus a note on what's wrong |
| competitors_mentioned | list |
| sources_cited | domains cited in the answer |

Match the brand using all the names in the site profile.

## Step 4: Score

Calculate, per tool and overall, **for unbranded and branded questions separately**. Lead with the unbranded numbers: they show whether the brand comes up when people don't already have it in mind.

- **Mention rate:** answers mentioning the brand / total answers
- **Citation rate:** answers linking to the brand's site / total answers
- **Share of voice:** brand mentions / all brand mentions (brand plus competitors) across the set
- **First-mention rate:** answers where the brand is named first / answers mentioning it
- **Negative mentions:** answers where the brand comes up in a negative light
- **Accuracy issues:** count and list, including outdated information (old products, prices or policies)

Show competitors' mention rates and share of voice alongside, so the numbers have context.

## Step 5: Find out where answers come from

Count the domains cited across all answers. Leave out spam, scraped copies and hijacked domains (for example, unrelated government or university domains hosting product pages). The top 10 tell you where AI tools get their information for this market: the brand's own site, competitors, publishers, review sites, directories, forums, video.

This list is often the most useful part of the report. A brand that isn't on the sources AI tools trust is hard to recommend, however good its own site is.

## Step 6: Diagnose each gap

For each question where the brand isn't mentioned, or is mentioned wrongly, decide the main cause:

1. **No page answers this.** The site has nothing that genuinely answers the question. Fix: plan a page with something original to say (pass to `content-planner`).
2. **A page exists but isn't used.** Check that the page is indexed and snippet-eligible, answers the question clearly, offers something beyond generic advice, and is current. Fix the weakest of these (pass to `content-refresh`).
3. **Answers rely on third-party sources.** The cited sources are publishers, review sites, directories or forums where the brand is absent. Fix: earn a genuine presence there through PR, real customer reviews, accurate listings (including Google Business Profile for local businesses) or useful contributions. Never suggest fake or paid-for mentions; Google's spam systems target them and they risk the brand's reputation.
4. **Wrong, outdated or negative information.** For negative sentiment, find the sources driving it and decide whether to fix the issue itself, answer it on the brand's own site, or respond on those sources. For wrong or outdated information, find where it likely comes from (an outdated page, old listing or third-party article) and correct it at the source.
5. **Competitor strength.** A competitor is the obvious answer. Point to the `competitor-analysis` skill to decide whether this is worth contesting.

**Never recommend** the tactics `references/google-guidance.md` lists as unnecessary for Google: llms.txt files, chunking content, rewriting for AI, special AI markup or inauthentic mentions. For other AI tools, don't present them as proven fixes either; there's no reliable public evidence they help.

## Output

1. **`geo-scorecard.md`**, kept short:
   - Date, tools, method, number of questions, and limits
   - Headline numbers: mention rate, citation rate, share of voice, against competitors
   - Top sources AI tools cite in this market
   - Accuracy problems, if any, first
   - Top 5 fixes, each tied to specific questions
2. **`results.csv`** and **`questions.csv`**.

End by suggesting a rerun date (monthly is usually enough) and noting that the same `questions.csv` must be used for a fair comparison.

## Limits to tell the user

- AI answers change with time, account, location and wording. This is a snapshot, not a ranking.
- A small question set gives a rough picture. Treat small differences between runs as noise.
- Being mentioned more doesn't guarantee traffic or sales.
- No one can guarantee inclusion in AI answers. These fixes improve the odds.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
