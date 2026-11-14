---
name: seo-audit
description: Turn a crawl or SEO audit export (Screaming Frog, Sitebulb, Semrush, Ahrefs, Search Console) plus spot checks of key pages into a short list of fixes ranked by impact and effort, in plain English. Use for SEO audits, technical SEO checks, "why isn't my site ranking", or reviewing an audit report.
---

# SEO audit

Audit tools list hundreds of issues. Most don't matter. This skill finds the handful that do, explains them in plain English, and puts them in the order to fix them.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/seo-audit/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** read audit and crawl exports, read Search Console exports, check individual pages you name, and judge which issues matter.
- **Can't:** crawl a whole site by itself, see rankings or traffic it hasn't been given, or see inside Google's systems. Without an export, it audits a sample of pages only and says so.

## Before you start

1. Read the site profile and `references/google-guidance.md`. Follow the house rules.
2. Ask for whatever the user has. The more, the better, but none is required:
   - A crawl export (CSV) from any tool. Screaming Frog's free version crawls up to 500 URLs.
   - An audit report export from any SEO tool.
   - Search Console: Page indexing report, Core Web Vitals report, Manual actions and Security issues status, and a Performance export.
   - The 5 to 10 most important pages (home, top services or products, best content).
3. If they have none of these, offer a **spot-check audit** of their most important pages and say clearly it isn't a full site audit.

## Step 1: Check for the serious problems first

Look for anything that stops pages being found or shown at all. These come first, whatever else is wrong:

- **Manual actions or security issues** in Search Console
- **Indexing blocked by mistake:** `noindex` on important pages, `robots.txt` blocking key sections, or the whole site set to noindex
- **Wrong canonicals:** important pages pointing their canonical elsewhere
- **Server errors** (5xx) or important pages returning 404
- **Snippet controls** (`nosnippet`, `max-snippet:0`) on pages that should appear in AI features, since pages need to be snippet-eligible
- **Site excluded from AI features** in Search Console, if the user wants to appear there
- **Spam policy risks** from `references/google-guidance.md`: large numbers of near-identical pages, third-party content hosted to borrow the site's strength, hidden text, sneaky redirects, or scripts that hijack the back button

## Step 2: Check the fundamentals

From the export, Search Console and spot checks:

- **Crawling and indexing:** pages indexed vs submitted, the main reasons pages aren't indexed, orphan pages (no internal links), redirect chains, sitemap errors
- **Duplicates:** duplicate or near-duplicate pages, missing or self-conflicting canonicals, parameter or filter URLs being indexed
- **On-page basics:** missing, duplicate or misleading titles and H1s; missing meta descriptions on key pages
- **Content:** thin pages, pages with nothing a competitor doesn't already say (commodity content), outdated pages on topics that change
- **Page experience:** Core Web Vitals from Search Console field data, mobile usability, intrusive pop-ups
- **JavaScript:** important content or links that only appear after JavaScript runs, where the export or spot checks show this
- **Images:** missing alt text on meaningful images, very large files
- **Structured data:** errors in Search Console, markup that doesn't match the page, or deprecated types (see `structured-data` skill)
- **Internal links:** important pages buried deep, broken internal links (see `internal-linking` skill)

## Step 3: Spot-check key pages

For each important page, fetch it and check: indexable, canonical correct, title and H1 clear, main content visible as text, first-hand value present, and obvious problems such as broken links or empty sections.

If you can only see a processed version of the page (not the raw HTML), say so. Things like canonicals, meta robots and structured data need the raw HTML or a crawl export to confirm.

## Step 4: Rank the fixes

Score each real issue:

- **Impact (1 to 3):** how much it limits search visibility. Things that stop indexing or affect many important pages score 3. Cosmetic issues on minor pages score 1.
- **Effort (1 to 3):** 1 is a settings change or quick edit, 3 is development work or a large content project.

Order by impact first, then lowest effort. Group the same issue across many URLs into one fix.

Leave out issues that don't affect search, even if tools flag them (for example, meta descriptions slightly over a length limit, or warnings on unimportant pages). Say in one line that you've left them out on purpose.

**Never recommend** anything `references/google-guidance.md` says Google ignores, such as llms.txt or chunking content for AI.

## Output

**`seo-audit.md`**, kept short:

1. What was checked (data sources, number of pages, date) and what wasn't
2. **Serious problems**, if any, at the top
3. **Top 10 fixes**, each with:
   - What's wrong, in plain English
   - Why it matters
   - Which URLs (or how many, with an example)
   - How to fix it
   - Impact and effort scores
4. **Left out on purpose:** one line on the kinds of tool warnings ignored
5. **Recheck:** when to check again, and in which Search Console report

Also save **`seo-issues.csv`**: issue, URLs affected, impact, effort, fix.

## Limits to tell the user

- An audit finds problems; it doesn't predict ranking changes.
- Field data (Core Web Vitals) comes from Search Console, not from lab tests run here.
- During a core update rollout, don't judge changes until it's finished.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
