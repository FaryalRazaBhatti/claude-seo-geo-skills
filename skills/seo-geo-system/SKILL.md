---
name: seo-geo-system
description: Run the full SEO and GEO/AEO workflow across a whole website, from setup and audit to a prioritised action plan, by coordinating the other skills in this set and passing their outputs between them. Use when someone wants a complete SEO or AI visibility review of their site, a full strategy, a monthly SEO routine, or asks where to start.
---

# SEO and GEO system

This skill runs the whole set as one system. It sets the site up once, runs each skill in the right order, passes results between them, and ends with one prioritised action plan for the whole website.

It works best with all the skills in this set installed. If some are missing, it runs the ones that are there and tells the user what the others would add.

## Files this skill uses

- **Workspace:** `seo-workspace/` in the user's project or working folder. Every skill in the set reads from and saves to it.
- **Site profile:** `seo-workspace/site-profile.md` (template in `templates/site-profile.md`)
- **Voice file:** `seo-workspace/voice.md` (template in `templates/voice.md`), needed only for planning and writing
- **Google guidance:** `references/google-guidance.md`. Every step follows it.

## The skills it coordinates

| Stage | Skill | Uses | Produces |
|---|---|---|---|
| Fix | `seo-audit` | Crawl or audit export, Search Console | `seo-audit/` |
| Measure | `search-console-analysis` | Search Console exports | `search-console-analysis/` |
| Compare | `competitor-analysis` | Site profile, competitor sitemaps | `competitor-analysis/` |
| Measure AI | `geo-visibility` | Site profile, AI tool answers | `geo-visibility/` |
| Plan | `content-planner` | Outputs of the four above | `content-planner/` |
| Improve | `content-refresh` | Plan items marked improve | `content-refresh/` |
| Write | `content-writer` | Plan items marked new | `content-writer/` |
| Publish | `internal-linking`, `structured-data` | New and updated pages | `internal-linking/`, `structured-data/` |

To run a skill, follow its own SKILL.md. If a skill isn't installed, skip that stage, note it in the plan, and carry on.

## Step 1: Set up (once)

1. Check for `seo-workspace/site-profile.md`. If it's missing, fill it in with the user, using the template. Ask in small groups of questions, not all at once.
2. If the user wants content planned or written, do the same for `seo-workspace/voice.md`.
3. Ask what data they can provide, and explain why each helps:
   - **Search Console** (most important): Performance and Generative AI report exports, Page indexing report
   - **A crawl export** from any crawler
   - **Keyword data** from any tool (optional)
   - **Browser access** for checking AI tool answers (optional; otherwise they can paste answers)
4. Agree the scope: the whole site, or a section. For large sites, start with the most important section.

## Step 2: Run the diagnosis

Run these in order. Each can use the previous ones' outputs:

1. `seo-audit`: anything blocking indexing or posing a spam risk comes first. If there's a serious problem (manual action, site-wide noindex), stop and fix that before going further.
2. `search-console-analysis`: what's working, what's falling, what's close to page one, and how the site shows in Google's AI features.
3. `competitor-analysis`: which topics to own, update or skip.
4. `geo-visibility`: what AI tools say about the brand, and which sources they rely on.

Check in with the user after the diagnosis. Share the headline findings in a few lines before planning.

## Step 3: Plan

Run `content-planner`, feeding it:

- Content gaps and near page one pages from `search-console-analysis`
- Own and update topics from `competitor-analysis`
- Unanswered questions and missing sources from `geo-visibility`

## Step 4: Build the action plan

Combine everything into **`seo-workspace/action-plan.md`**:

1. **Summary:** where the site stands, in five lines or fewer
2. **Fix now:** serious technical or spam-risk issues
3. **Quick wins (next 30 days):** pages close to page one, title and CTR fixes, internal links, refreshes of strong pages
4. **Content (next 90 days):** the top items from the content plan, in order
5. **Beyond the website:** genuine PR, reviews, listings and Google Business Profile work suggested by `geo-visibility`
6. **Measure:** what to check, where, and when (Search Console monthly, a `geo-visibility` rerun monthly or quarterly)

Rank across all sources with one rule: **fix what blocks visibility first, then what's closest to paying off, then new work.** Don't list more than the user can realistically do; cut low-value items rather than padding.

Each item says which skill produced it and which file has the detail.

## Step 5: Do the work (only if asked)

Work through the plan one item at a time: `content-refresh` for updates, `content-writer` for new pieces, then `internal-linking` and `structured-data` for each page before it goes live. Never publish or change the website without showing the changes and getting the user's approval.

## Monthly routine

When the user comes back:

1. Ask for fresh Search Console exports.
2. Rerun `search-console-analysis`, and `geo-visibility` with the same question set.
3. Compare with last month's outputs in the workspace.
4. Update `action-plan.md`: mark what's done, add what's new, and drop what no longer matters.

If a Google core update was rolling out, wait until it's complete before judging the results.

## Limits to tell the user

- The system is only as good as the data it's given. Search Console data makes the biggest difference.
- No one can guarantee rankings or inclusion in AI answers. This system focuses effort where it's most likely to help.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
