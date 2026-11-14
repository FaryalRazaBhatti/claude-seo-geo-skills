---
name: competitor-analysis
description: Map what competitors cover, where they're strong or thin, who AI tools mention, and turn it into a list of topics to own, update or skip. Use when someone asks for competitor analysis, content gap analysis, topic strategy, "what should I write about", or how their content compares with a rival's.
---

# Competitor analysis for topic and content strategy

Most competitor reports stop at "they rank for keywords you don't". This skill answers a more useful question: **which topics can this site realistically win, and what should it do about each one?**

The output is a decision for every topic: **Own**, **Update**, or **Skip**, each with a reason.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/competitor-analysis/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## Before you start

1. Read the site profile and `references/google-guidance.md`. You need the brand, website, competitors, topics and priority questions. If competitors or topics are missing, ask for them before going further. Everything else is optional.
2. Follow any house rules in the profile. Don't add rules of your own.
3. Ask which of these the user has, and use whatever they have. None of them are required:
   - Keyword exports from any tool (Semrush, Ahrefs, Moz, Search Console, Bing Webmaster Tools), as CSV
   - Search Console performance export for their own site
   - Results from the `geo-visibility` skill, if they've run it

Never invent traffic, volume or ranking figures. If no data has been provided, say the analysis is based on content coverage only, and label every estimate as an estimate.

## Step 1: Build a content inventory

For the user's site and each competitor (up to 5):

1. **Decide what counts as content for this site.** Many sites, especially brands and shops, have no blog. Content is whatever answers a reader's questions: blog posts, guides, explainers, comparison pages, buying guides, help articles. Exclude pure product, category, tag, author, legal and careers pages unless they're the site's main way of answering questions. Note your choice per site.
2. **Find the sitemaps.** Check `/robots.txt` first, as it often lists several. Then try `/sitemap.xml` and `/sitemap_index.xml`.
   - Sitemaps are often nested: an index points to more indexes. Follow them, but only into children that look relevant (by market and section).
   - Multi-country sites split sitemaps by country or language. Use only the market in the site profile (for example `/uk/` or `_gb`).
3. **Check other domains.** Content often lives on a subdomain or separate site (support, help, blog, newsroom, magazine). Look for links to these from the main site, include them if they're in scope, and say in the report if you couldn't check them.
4. **If there's no usable sitemap**, use the blog or resources index page. If that fails too, ask the user for a list of URLs. Don't scrape aggressively, and don't bypass anything that blocks access.
5. **Large sites:** cap at about 200 content URLs per site. Very large sitemap files may only be partly readable; if so, say the counts are a sample.
6. For each URL, record: site, URL, title, content type, and date.

**Dates need care.** Sitemap `lastmod` dates are often missing, or bulk-updated (many pages sharing the same date usually means a site migration, not fresh content). Prefer a date shown on the page. Treat sitemap dates as a hint only, and flag bulk dates.

Save as `inventory.csv`.

## Step 2: Group into topics

Cluster every URL into topics. A topic is a theme a reader would recognise ("email deliverability"), not a single keyword ("how to warm up an IP").

- Start from the user's topics in the site profile, then add any clusters that show up repeatedly in competitor content.
- Aim for 10 to 25 topics. Merge anything with fewer than 2 pages across all sites into a related topic, or drop it.
- If keyword exports were provided, attach keywords to topics too.
- Label content that has nothing to do with the site's audience as **off-topic** (for example, recipes on a tech brand's blog). Keep it out of topic counts, but mention it: a large off-topic section can be a useful finding in itself.

Build a **coverage matrix**: one row per topic, one column per site, showing number of pages and the most recent date.

## Step 3: Classify each topic

For each topic, pick one state:

| State | What it means |
|---|---|
| **Dominated** | One competitor has 5+ pages, recently updated, clearly the reference on this topic |
| **Contested** | Two or more sites cover it in reasonable depth |
| **Thin** | Covered, but only by 1 or 2 shallow or outdated pages |
| **Open** | Relevant to the audience, but nobody covers it well |

"Recently updated" means within the last 12 months, based on visible dates. If you can't find a date, treat the page as undated, not as fresh.

## Step 4: Check who AI tools mention (optional but recommended)

If `geo-visibility` results exist, use them. If not, offer to run a short version: pick 1 or 2 priority questions per topic and check which brands get mentioned or cited.

Add to each topic: which site, if any, AI answers mention most, and which third-party sources they cite. A topic can look Open in search but already be owned in AI answers, or the reverse.

## Step 5: Compare quality where it matters

For the most important Contested and Dominated topics (up to 5), compare the strongest competitor page with the user's best page on the same topic (or note that the user has none).

Score each page 0, 1 or 2 on:

1. **Direct answer:** does it answer the main question in the first few lines?
2. **Evidence:** are claims backed by linked, credible sources or original data?
3. **Experience:** is there first-hand experience, examples or original work, not just summary?
4. **Freshness:** is a date visible to readers, and is it current? A date only in the page code scores 0.
5. **Depth:** does it cover the follow-up questions a reader would have?
6. **Structure:** clear headings, scannable, easy for a person or an AI tool to quote?

Total out of 12. Show both scores side by side with one line on the biggest difference. Don't copy or closely paraphrase competitor text in the report.

## Step 6: Decide

Score each topic 0 to 3 on three things:

- **Relevance:** how closely it fits the audience and what the site wants readers to do
- **Gap:** how much room there is (Open = 3, Thin = 2, Contested = 1, Dominated = 0)
- **Winnability:** whether the user can realistically produce something better, given their experience and existing content (use the quality comparison where available)

Then decide:

- **Own:** total 7 or more, and relevance at least 2. Plan new content, but only where the user has something original to add. Winning a topic means one strong page per real question, not many similar pages (see the scaled content abuse policy in `references/google-guidance.md`).
- **Update:** the user already has content on the topic, and their quality score is lower than the competitor's or it's out of date. Improve before writing more.
- **Skip:** relevance under 2, or winnability 0. Say why in one line, so it's a decision, not an oversight.
- **Own through others:** where search or AI answers for the topic are led by third-party sites (publishers, review and comparison sites), another page on the user's own site may not help much. Recommend earning a presence on those sites instead.
- **Check first:** where the topic may already be covered on a domain you couldn't check.

These thresholds are a starting point. If the user's situation makes a different call sensible, make it and explain why.

## Output

1. **`competitor-report.md`**, kept short:
   - What was analysed (sites, page counts, data sources, date) and any limits
   - Top 5 topics to own, each with the gap and a suggested angle
   - Pages to update first, with the specific fix
   - Topics to skip, one line each
   - AI visibility notes, if step 4 was run
2. **`topic-matrix.csv`**: topic, state, pages per site, latest date per site, AI leader, relevance, gap, winnability, decision, reason.
3. **`inventory.csv`** from step 1.

End by offering to pass the Own topics to the `content-planner` skill.

## Limits to tell the user

- Content coverage shows what competitors publish, not how well it performs. Performance needs real data.
- AI answers change between runs, accounts and locations. Treat AI findings as a snapshot.
- Sampled sites may have content that wasn't checked.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
