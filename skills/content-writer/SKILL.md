---
name: content-writer
description: Write a helpful, sourced article in the user's own voice, using only experience and facts they can stand behind, following Google's people-first content guidance. Use when someone asks for a blog post, article, guide or page copy written for search and AI visibility.
---

# Content writer

This skill writes one article at a time, properly. It does not mass-produce pages. Its job is to help the user publish something genuinely useful that they're happy to put their name to.

## Files this skill uses

This skill works on its own, or as part of the full set (see `seo-geo-system`).

- **Site profile:** `seo-workspace/site-profile.md` in the user's project or working folder. If it's missing, ask only for the essentials this skill needs (the fields are in `templates/site-profile.md`), and offer to save the answers there so other skills can reuse them.
- **Voice file:** `seo-workspace/voice.md`. If it's missing, ask the user for the essentials in `templates/voice.md` (especially their first-hand experience and anything that must stay private) and offer to save it there.
- **Google guidance:** `references/google-guidance.md`, bundled with this skill. Follow it. If anything here conflicts with it, the guidance file wins.
- **Outputs:** save to `seo-workspace/content-writer/`. Before starting, check `seo-workspace/` for outputs from other skills and use them where they help.
- **Other skills:** where this skill suggests passing work to another skill that isn't installed, tell the user the next step in plain words instead.

## Rules this skill never breaks

1. **No invented facts.** Every statistic, date, price or claim about a third party must come from a source you have actually opened, linked in the article. If you can't verify something, leave it out or mark it for the user to check.
2. **No invented experience.** Only use first-hand experience listed in the voice file or given by the user for this piece. Never write "in my experience" about something the user hasn't told you.
3. **No private information.** Respect the "never appear in public content" section of the voice file.
4. **No fake freshness.** Only add or change a "last updated" date when the content has meaningfully changed.
5. **One piece, written for people.** Don't produce batches of near-identical pages, or versions targeting tiny wording changes.

## Before you start

1. Read the site profile, the voice file and `references/google-guidance.md`. Follow the house rules.
2. Get a brief: ideally from `content-planner`, otherwise ask for the topic, main question, audience, and what the user wants readers to do.
3. Ask what the user knows or has done on this topic that others haven't. Wait for an answer. This is what makes the piece non-commodity. If they have nothing to add, say the piece will be hard to make stand out, and suggest another angle or topic.

## Step 1: Research

1. Search for the current, authoritative sources on the topic: official documentation, regulators, original research, primary data. Prefer original sources to articles that summarise them.
2. Read the top results for the main question, to see what's already said and where it falls short. Don't copy or closely paraphrase them.
3. Keep a source list with the exact facts each one supports.
4. If something has changed recently (prices, rules, product features), check the date of each source.

## Step 2: Outline

Show the user a short outline before writing:

- Title
- The direct answer to the main question, in one or two sentences
- Sections, as the questions a reader would ask next
- Where the user's own experience, examples or data will go
- Sources each section relies on

Wait for approval or changes.

## Step 3: Write

- **Answer first.** Give the direct answer early, then the detail.
- **Clear structure.** Descriptive headings, short paragraphs, lists where they genuinely help.
- **Write naturally,** in the user's voice. No keyword stuffing, no repeating phrases for search engines, no special formatting "for AI".
- **Show the experience.** Specific examples, what the user did and what they learned.
- **Cite as you go.** Link sources inline where the claim is made, and list them at the end.
- **Be honest about limits:** where things depend on circumstances, or evidence is mixed.
- **Who wrote it:** include an author line or short bio based on the voice file, if the site uses them.
- **Images:** suggest where an original image, diagram or screenshot would help, with alt text describing it.
- An FAQ section is fine when readers genuinely have follow-up questions. Don't add it for rich results; FAQ rich results no longer appear in Google.

## Step 4: Check before handing over

Go through this list and fix anything that fails:

- Every factual claim is linked to a source you opened
- All experience comes from the voice file or the user
- Nothing private is included
- The opening answers the main question
- The piece adds something the top results don't
- It reads like the voice samples, not like a template
- Title and URL follow house rules
- No claims about guaranteed rankings or results

## Output

1. The article in Markdown, ready to paste into the user's CMS
2. A suggested title tag (around 60 characters) and meta description (around 155 characters)
3. A list of sources used
4. **To check before publishing:** anything the user needs to confirm, such as figures you couldn't verify or experience details to fill in

Offer to pass the article to `internal-linking` and `structured-data`.

## Limits to tell the user

- The user is the author and should review everything before publishing.
- Good writing improves the chances of doing well; it can't guarantee rankings or inclusion in AI answers.

---

Part of [Claude SEO and GEO skills](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills) by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). MIT licence.
