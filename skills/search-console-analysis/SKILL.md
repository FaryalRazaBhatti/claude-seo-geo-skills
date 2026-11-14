---
name: search-console-analysis
description: Analyse Google Search Console exports, including the Generative AI performance report, to find quick wins, falling pages, CTR problems, cannibalisation and AI Overview / AI Mode visibility, or to check the impact of a core update. Use when someone shares Search Console data or asks why traffic changed, what to improve first, or how they appear in Google's AI features.
---

# Search Console analysis

Search Console is the only free source of real Google data for a site, including how often its pages appear in AI Overviews and AI Mode. This skill turns the exports into a short list of things to do.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/search-console-analysis/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** analyse the exports the user provides, run calculations on them, and explain what changed and what to do.
- **Can't:** log in to Search Console unless a connector or browser access is available, or see data the exports don't contain. The Generative AI report shows impressions only: no queries and no clicks.

## Before you start

1. Read the site profile and `references/google-guidance.md`.
2. Ask the user to export, for the same date range (the last 3 months is a good default):
   - **Performance report (Web search):** the Queries, Pages, Countries and Devices tabs
   - **Generative AI performance report (Search),** if available: the Pages tab and the chart data
   - **For a before-and-after comparison:** use Compare mode in Search Console, or export two equal periods
3. Note the limits of the exports: tables stop at 1,000 rows, and "~" or "-" values in the AI report export as zeros. Treat those zeros as unknown, not as zero.

## Step 1: Check the data

- Confirm the date ranges, search type and filters. Mixed ranges make comparisons meaningless.
- Note any big event in the period: a core update (check the Search Status Dashboard), a site migration, a redesign, seasonality.

## Step 2: Find opportunities

Run these on the Queries and Pages exports. Show the numbers, not just the conclusions.

1. **Close to page one:** queries or pages with average position roughly 4 to 15 and meaningful impressions. Improving the page that ranks is usually faster than writing a new one.
2. **Low CTR for the position:** pages whose CTR is well below the site's own median CTR at a similar position. Check the title and snippet, and whether the page matches the query's intent. Don't use industry CTR averages; compare the site with itself.
3. **Falling pages:** pages whose clicks dropped most between two equal periods. Check whether the drop is impressions (visibility), CTR (presentation or a changed results page), or position (ranking).
4. **Cannibalisation:** queries where two or more of the site's pages get significant impressions. Only flag it when the pages genuinely compete for the same intent; different pages for related queries are normal.
5. **Content gaps:** queries with impressions but no page that really answers them. Pass these to `content-planner`.

## Step 3: AI Overviews and AI Mode (if the Generative AI report was exported)

1. **AI impression share per page:** AI impressions divided by Web search impressions for the same page and period.
2. **Pages that appear in AI features most.** Note what they have in common (topic, format, depth, freshness).
3. **Pages with strong organic impressions but few AI impressions.** These are candidates to review for unique value and clarity. Don't recommend chunking, rewriting for AI or special markup; Google says these aren't needed.
4. **Trend over time** for the site and the top pages.

Be clear about what this can't show: which queries triggered the AI feature, and whether anyone clicked from it. Clicks from AI features are counted inside the normal Performance report and can't be separated.

## Step 4: Core update check (only if asked, or if a drop lines up with one)

Follow Google's own approach:

1. Confirm the rollout has finished, using the Search Status Dashboard. If it hasn't, say so and suggest waiting.
2. Compare a period after the rollout with a similar period before it. Avoid holiday weeks and other unusual periods on either side.
3. Find which pages and queries lost most, and whether the losses are spread across the site or concentrated in a section or content type.
4. Small position changes (a few places) are normal. Larger drops on key pages are worth a content review: is it helpful, original and better than what now ranks above it?
5. Recommend improvements to the content, not quick tricks. Remind the user that recovery often takes months.

## Output

**`search-console-report.md`**, kept short:

1. Data used, date ranges, and limits
2. Headline: what changed and the most likely reason
3. **Top 5 actions**, each with the pages or queries, the numbers behind it, and what to do
4. AI features summary, if the report was provided
5. Core update notes, if relevant

Also save **`opportunities.csv`**: type, page, query (where relevant), impressions, clicks, CTR, position, suggested action.

## Limits to tell the user

- Search Console data is sampled and anonymised for some queries, so totals in exports may not match the charts.
- Position is an average and moves for many reasons; don't overreact to small changes.
- AI impressions show visibility, not traffic or sales.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
