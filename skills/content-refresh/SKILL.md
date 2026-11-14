---
name: content-refresh
description: Review an existing page that's losing traffic, out of date or underperforming, and give a specific update plan, or a merge or remove recommendation. Use for content refreshes, content decay, updating old posts, pruning, or "why has this page dropped".
---

# Content refresh

Improving a page that already ranks is often the fastest win in SEO. This skill looks at one page (or a short list) and decides exactly what to change, or whether it should be merged or removed instead.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Voice file:** `seo-workspace/voice.md`. If it's missing, ask the user for the essentials in `templates/voice.md` (especially their first-hand experience and anything that must stay private) and offer to save it there.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/content-refresh/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** read the page, compare it with what currently ranks, use Search Console data if provided, and write the specific changes.
- **Can't:** know why rankings moved for certain. It gives the most likely reasons and says how sure it is.

## Before you start

1. Read the site profile, the voice file and `references/google-guidance.md`.
2. Get the page URL, and ideally its Search Console data: queries for that page, clicks, impressions and position over the last 6 to 12 months, compared with an earlier period.
3. Check whether a core update was rolling out during the drop (Search Status Dashboard). If one is still rolling out, suggest waiting until it finishes before changing much.

## Step 1: Diagnose

Work out which of these is happening, using the data:

- **Lost visibility:** impressions down. The page ranks lower or for fewer queries.
- **Lost clicks only:** impressions steady, CTR down. Often a changed results page (more AI answers or other features), or a weaker title and snippet.
- **Seasonal:** the same drop happened last year at this time.
- **Outdated:** facts, prices, screenshots or advice are no longer current.
- **Outranked:** other pages now answer the question better.
- **Competing with itself:** another page on the same site targets the same thing.
- **Technical:** the page changed URL, lost internal links, became noindex, or has a broken canonical.

## Step 2: Compare with what ranks now

Search the page's main query. Read the top results, and note what they cover that this page doesn't, what's more current, and what this page does better. Don't copy them.

## Step 3: Decide

- **Update:** the page is worth keeping and can be improved.
- **Merge:** another page on the site covers the same thing. Combine the best of both into one, and redirect the other.
- **Remove or noindex:** the page has no search demand, no useful links and no value for readers. Recommend a redirect if a close replacement exists. Removing pages is a judgement call: explain the reasoning and let the user decide.
- **Leave it:** the drop is seasonal, minor or caused by a change to the results page that the page can't fix.

## Step 4: Write the update plan

For an update, be specific. For each change, give the section, what to change and why:

- Correct or replace anything out of date, with sources
- Add what's missing, especially first-hand experience from the voice file, original examples or data
- Answer the main question clearly near the top, if it doesn't already
- Remove padding and anything no longer true
- Improve the title and meta description if CTR is the problem
- Fix technical issues found in step 1
- Add or fix internal links (see `internal-linking`)

Update the visible date only if the changes are substantial. Don't change the date for small edits.

## Output

**`refresh-plan.md`** for each page:

1. Diagnosis, with the numbers behind it and how confident you are
2. Decision: update, merge, remove or leave
3. The list of specific changes, in order of importance
4. Rewritten sections, if the user wants them (following `content-writer` rules)
5. What to check in Search Console in 4 to 8 weeks

## Limits to tell the user

- Ranking changes after an update can take weeks or months to show.
- Some drops come from changes to the results page itself and can't be fully recovered.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
