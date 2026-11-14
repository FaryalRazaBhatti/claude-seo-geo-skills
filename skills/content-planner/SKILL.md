---
name: content-planner
description: Turn topics, Search Console queries, keyword exports and competitor findings into a realistic content plan, where every piece has a clear purpose and something original to say. Use for content plans, keyword strategy, editorial calendars, topic clusters, or "what should I write next".
---

# Content planner

A content plan is only as good as what each piece adds. This skill plans fewer, better pieces: each one answers real questions, has a reason to exist, and offers something the reader can't get from every other result.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Voice file:** `seo-workspace/voice.md`. If it's missing, ask the user for the essentials in `templates/voice.md` (especially their first-hand experience and anything that must stay private) and offer to save it there.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/content-planner/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## What this skill can and can't do

- **Can:** group keywords and questions by intent, map them to existing or new pages, spot overlap, and suggest angles based on the user's own experience.
- **Can't:** invent search volumes or difficulty scores. It uses the numbers in the data provided, or says there are none.

## Before you start

1. Read the site profile, the experience section of the voice file, and `references/google-guidance.md`. Follow the house rules, including any rules for titles and URLs.
2. Gather inputs. Use whatever exists:
   - Topics from the site profile
   - `competitor-analysis` output (topics to own or update)
   - `search-console-analysis` output (content gaps, pages close to page one)
   - Keyword exports from any tool
   - A list of the site's existing content (sitemap or export)
3. If there's no keyword or Search Console data, plan from topics and real questions (from customers, sales calls, forums, "People also ask"), and say the plan has no volume data.

## Step 1: Group by intent

Group keywords and questions into clusters that would be answered by **one page**. Two queries belong on the same page if a good answer to one would satisfy the other.

Label each cluster's intent: learn, compare, choose, do (how-to), buy, or find locally.

Don't create a separate page for every wording of the same question. Google understands synonyms, and many near-identical pages risk the scaled content abuse policy.

## Step 2: Map to existing content first

For each cluster:

- **Existing page already covers it:** mark it **improve** and pass it to `content-refresh`.
- **Two existing pages compete for it:** mark it **merge**.
- **Nothing covers it:** mark it **new**.

## Step 3: Check each new piece is worth writing

A new piece goes on the plan only if you can answer yes to both:

1. **Is there real demand?** Search Console impressions, keyword data, or real questions from the audience.
2. **Is there something original to add?** First-hand experience from the voice file, original data, a clear opinion, a useful tool or template, or a better explanation than what currently exists.

If the second answer is no, say so. Either find an angle from the user's experience, or drop the piece. Commodity content is unlikely to do well in search or AI features.

Also note where search results for a topic are dominated by answers on the results page itself. These pieces may get visibility but few clicks, which is fine for awareness but worth knowing.

## Step 4: Shape each piece

For every item on the plan:

- **Working title:** clear and specific, following house rules
- **Main question it answers,** plus the follow-up questions a reader will have
- **Intent and format:** guide, comparison, checklist, template, opinion, case study, tool
- **Original angle:** what makes it worth reading
- **Evidence needed:** sources, data or examples to gather before writing
- **Internal links:** existing pages it should link to and from
- **URL suggestion:** following house rules
- **Priority:** high, medium or low, based on demand, business relevance and effort

## Step 5: Order the plan

Put first: improvements to pages close to page one, then new pieces with clear demand and a strong angle, then the rest. Spread publishing over a realistic pace for the user. Don't suggest volumes they can't keep up while maintaining quality.

## Output

1. **`content-plan.md`:** a short summary of the approach, then the top 10 items with their reasoning.
2. **`content-plan.csv`:** cluster, keywords or questions, intent, action (new, improve, merge), working title, original angle, evidence needed, internal links, URL, priority, data source.

End by offering to brief the first piece for `content-writer`.

## Limits to tell the user

- Keyword volumes from tools are estimates and often differ between tools.
- A plan doesn't guarantee rankings; quality and originality of each piece decide that.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
