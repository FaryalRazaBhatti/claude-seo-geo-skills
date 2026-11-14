# Google guidance these skills follow

Checked: 14 November 2026. Google changes things often, so check the official pages below before relying on this, and update the date when you do.

Every skill in this repo follows this file. If a skill's advice ever conflicts with it, this file wins.

## The big picture

- **AEO and GEO are SEO, as far as Google is concerned.** Google says its AI features (AI Overviews and AI Mode) run on its core ranking and quality systems, and that optimising for them is still SEO.
- **No extra requirements for AI features.** To be shown as a supporting link, a page must be indexed and eligible to show with a snippet. There are no additional technical requirements.
- **Site-level control.** Search Console has a setting for whether a site appears in, and helps ground, Google's generative AI features. A site must be included there to be eligible.
- **Other AI tools may differ.** Google's guidance covers Google only. ChatGPT, Perplexity, Copilot and others may weigh things differently. Don't apply Google's rules to them as fact, and don't apply rumoured rules for them to Google.

## What Google recommends

- **Non-commodity content:** a unique point of view, first-hand experience and clear organisation, not generic advice anyone could write.
- **Technical basics:** crawlable pages, the Search technical requirements, sound JavaScript SEO, good page experience, and less duplicate content.
- **Images and video:** high-quality and relevant, following Google's image and video SEO guidance.
- **Local and ecommerce:** Google Business Profile and Merchant Center feeds help businesses and products appear in AI responses and other results.
- **AI-assisted content is fine** if it meets Search Essentials and the spam policies.
- **Agent-friendly sites (optional):** relevant only if AI agents need to complete tasks on the site, such as booking or comparing products.

## What Google says you can ignore (for Google Search)

The skills must never recommend these for Google:

- **llms.txt, AI text files or special Markdown versions.** Google Search doesn't use them. They neither help nor harm.
- **Chunking content** into small pieces for AI. There's no ideal page length.
- **Rewriting for AI** or covering every long-tail variation. Google understands synonyms and meaning.
- **Seeking inauthentic mentions** across the web. Spam systems block them.
- **Special AI schema.** No AI-specific structured data exists or is needed.

## Structured data

- Useful for rich result eligibility, but not required for AI features.
- **FAQ rich results stopped appearing on 7 May 2026.** HowTo rich results went in 2023, and several other types were retired in 2025. Never promise rich results for deprecated types.
- Markup must match what's visible on the page.

## Spam policies to design around

- **Scaled content abuse:** many pages made mainly to manipulate rankings, however they're produced. Skills must never mass-produce near-identical pages.
- **Site reputation abuse:** third-party content published on a site mainly to borrow its ranking strength.
- **Expired domain abuse, link spam, doorway pages, cloaking, hidden text, thin affiliation.**
- **Back button hijacking:** interfering with the browser back button. Enforced from 15 June 2026, including code from ad or third-party scripts.
- The spam policies apply to AI Overviews and AI Mode as well as normal results.

## Freshness

Don't change a page's date unless the content has meaningfully changed. Faking freshness is a pattern Google's helpful content guidance warns against.

## Measuring

- **Search Console Performance report:** clicks, impressions, CTR and position. AI Overviews and AI Mode traffic is included in the Web search type.
- **Generative AI performance report:** impressions only, from AI Overviews and AI Mode, by page, country, device and date. No queries and no clicks. Exports replace "~" and "-" with zeros, and tables stop at 1,000 rows.
- **Third-party tools can't see inside Google's ranking or AI systems.** Treat their scores as estimates.

## Core updates

- Google runs several a year (in 2026: March, May and November). They aren't penalties.
- Wait until the rollout is complete, then compare similar periods before and after. Check the Search Status Dashboard for dates.
- Recovery usually takes months and may not show until a later update. Don't buy links or add thin pages in response.

## Official sources

- AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Optimising for generative AI features: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Search Essentials: https://developers.google.com/search/docs/essentials
- Spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- Core updates: https://developers.google.com/search/docs/appearance/core-updates
- Structured data search gallery: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Generative AI performance report: https://support.google.com/webmasters/answer/16984139
- Search Status Dashboard: https://status.search.google.com/
