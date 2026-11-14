---
name: internal-linking
description: Plan and check internal links across a site or a set of posts, including posts scheduled to publish later, so important pages are easy to reach and no link points to a page that isn't live. Use for internal linking, related posts, orphan pages, broken internal links, or link plans for new or scheduled content.
---

# Internal linking

Internal links help people and search engines find and understand pages. This skill suggests useful links between related pages and checks the links that already exist.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/internal-linking/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** read a sitemap, a crawl export or a list of pages; read individual pages; suggest links with anchor text; check links for problems; and order links correctly for scheduled posts.
- **Can't:** edit the website unless the user has connected their CMS. Otherwise it produces a list for the user to apply.

## Before you start

1. Read the site profile and follow its house rules.
2. Get a list of pages:
   - **Best:** a crawl export with internal links (for example, Screaming Frog's "All Inlinks" export)
   - **Good:** the sitemap, plus the content of the pages in scope
   - **For new content:** the draft, plus the list of live pages
3. If any posts are scheduled, get their publish dates.

## Step 1: Understand the site

- Group pages by topic (reuse `competitor-analysis` or `content-planner` output if available).
- Identify the most important pages: the ones the business most wants found, from the site profile or the user.
- If a crawl export is available, count incoming internal links per page and find **orphan pages** (no internal links pointing to them).

## Step 2: Check existing links

Flag:

- **Broken links:** internal links to pages that return 404 or other errors
- **Redirected links:** internal links that go through a redirect; link to the final URL instead
- **Nofollow on internal links:** usually a mistake, as it stops link value flowing within the site
- **Links to non-canonical or noindex pages**
- **Important pages with few incoming links,** or buried many clicks from the home page
- **Unhelpful anchor text:** "click here" or "read more" where a descriptive phrase would be clearer

## Step 3: Suggest new links

For each page in scope, suggest links **to** and **from** closely related pages:

- Link where it genuinely helps the reader take the next step, not to hit a number.
- **Anchor text:** a natural, descriptive phrase that tells the reader what they'll get. Vary it naturally; don't use the same exact keyword every time.
- Place links in the body text where the topic is discussed. A "related reading" list at the end is a useful extra, not a replacement.
- Aim for a handful of good links per page. Avoid adding so many that each one loses meaning.
- Prioritise links from strong, related pages to important pages that need help.

## Step 4: Scheduled posts

When posts are scheduled to publish on different dates:

1. Sort all pages by their live date (already live first, then by schedule).
2. A post may only link to pages that will be live **on or before** its own publish date.
3. For links a post can't have yet, list them as **add later**, with the date they become safe to add.
4. Also list links to add to older posts once each new post goes live.

## Output

1. **`link-plan.csv`:** source page, target page, suggested anchor text, where in the source page (section or sentence), reason, priority, and earliest date (for scheduled posts).
2. **`link-issues.csv`:** page, issue, link, fix.
3. **`link-summary.md`:** orphan pages, top fixes, and any links to add later, with dates.

If the user's CMS is connected and they ask you to apply the changes, show what will change on each page first and wait for approval.

## Limits to tell the user

- Without a crawl export, link counts and orphan pages can't be fully checked.
- Internal links help discovery and context; they don't make weak content rank.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
