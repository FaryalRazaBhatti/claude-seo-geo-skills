---
name: structured-data
description: Check and write schema.org structured data (JSON-LD) that Google currently supports, matching what's visible on the page, and flag markup that's deprecated or won't produce rich results. Use for schema markup, JSON-LD, rich results, or structured data errors.
---

# Structured data

Structured data helps search engines understand a page and can make it eligible for rich results. This skill writes only markup that's accurate and currently supported, and it says plainly when markup won't change anything.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/structured-data/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** read a page, write JSON-LD that matches its content, review existing markup, and flag deprecated or misleading markup.
- **Can't:** guarantee rich results (Google decides whether to show them), or run Google's Rich Results Test itself. The user should test the markup there before publishing.

## Facts to keep in mind

Read `references/google-guidance.md`. In short:

- Structured data is **not required** for AI Overviews or AI Mode, and there's **no special AI markup**.
- **FAQ rich results stopped appearing in May 2026.** HowTo rich results went in 2023, and several other types were retired in 2025.
- Markup must describe content that's **visible on the page.**

Always check Google's search gallery for the current list of supported types before writing markup:
https://developers.google.com/search/docs/appearance/structured-data/search-gallery

## Step 1: Understand the page

Fetch the page, or ask the user to paste its HTML. Note what the page actually is (article, product, local business, event, recipe, video, organisation home page, and so on) and what visible information it contains: names, dates, prices, ratings, authors, addresses.

If you can't see the raw HTML, you can't check existing markup. Ask the user for the page source or a structured data export.

## Step 2: Review existing markup

Flag:

- **Errors:** missing required properties, invalid values, broken JSON
- **Mismatches:** markup that says something the page doesn't show (a rating that isn't displayed, a price that's different, an author who isn't named)
- **Deprecated types:** types that no longer produce rich results in Google. Explain that the markup is harmless and may still be read by other systems, so removing it is optional. Don't present it as a problem that needs urgent action.
- **Spammy markup:** reviews the business wrote about itself, hidden content, irrelevant types. These can lead to a manual action and should be removed.

## Step 3: Write the markup

Choose the types that fit the page and are listed in Google's search gallery. Common examples:

- **Organization** (home or about page): name, logo, URL, social profiles
- **Article / BlogPosting:** headline, author (with a link to an author page if there is one), datePublished, dateModified, image
- **BreadcrumbList:** the page's breadcrumb trail
- **Product** with offers and reviews, for product pages
- **LocalBusiness:** name, address, opening hours, phone, matching the Google Business Profile
- **Event, Recipe, VideoObject, JobPosting,** and others where the page genuinely is one

Rules:

- Use JSON-LD.
- Include only information that's visible on the page and true.
- Use `dateModified` only when the content has genuinely changed.
- Don't add types just because they exist; each one should describe the page.

## Output

1. **The JSON-LD,** ready to paste, with a note on where it goes (usually the page head, or the CMS's SEO or schema setting).
2. **Review notes:** errors, mismatches, deprecated or spammy markup, and what to do about each.
3. **What this will and won't do:** which rich results the page may become eligible for, if any, and a reminder that markup doesn't affect AI features specifically.
4. **Test it:** ask the user to check the markup with Google's Rich Results Test (https://search.google.com/test/rich-results) and the Schema Markup Validator (https://validator.schema.org/), then watch the Enhancements reports in Search Console.

## Limits to tell the user

- Valid markup makes a page eligible for rich results; it doesn't guarantee them.
- Supported types change. Check the search gallery before relying on a type.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
