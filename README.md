# Claude SEO and GEO skills

Free Claude skills for SEO and AI visibility (GEO/AEO), built on Google's current guidance and on what Claude can really do.

Use any skill on its own, or install the full set and run the whole website through one system.

## The skills

| Skill | What it does |
|---|---|
| `seo-geo-system` | Runs the full workflow across a website and ends with one prioritised action plan |
| `seo-audit` | Turns a crawl or audit export, plus spot checks of key pages, into the top 10 fixes ranked by impact and effort |
| `search-console-analysis` | Finds quick wins, falling pages, CTR problems and cannibalisation in Search Console exports, reads the Generative AI report, and checks core update impact |
| `competitor-analysis` | Maps what competitors cover, finds thin and open topics, and decides what to own, update or skip |
| `geo-visibility` | Checks what ChatGPT, Gemini, Perplexity, Google AI features and others say about a brand, compared with competitors, and diagnoses why |
| `content-planner` | Turns topics, queries and keyword data into a plan where every piece has real demand and something original to say |
| `content-writer` | Writes one sourced article at a time in your voice, with no invented facts or experience |
| `content-refresh` | Diagnoses an underperforming page and decides whether to update, merge, remove or leave it |
| `internal-linking` | Plans and checks internal links, including for posts scheduled to publish later |
| `structured-data` | Writes and reviews schema markup that Google currently supports, and flags deprecated types |

## Use one skill, or the whole system

**On its own:** every skill folder is self-contained. It carries its own copy of the Google guidance and templates, and asks for anything it needs that it can't find.

**As a system:** all skills share a workspace folder in your project:

```
seo-workspace/
├── site-profile.md        your site, audience, competitors, questions and rules (filled in once)
├── voice.md               your writing voice, for planning and writing
├── seo-audit/             each skill saves its outputs in its own folder...
├── search-console-analysis/
├── competitor-analysis/
├── geo-visibility/
├── content-planner/
├── ...
└── action-plan.md         ...and seo-geo-system combines them into one plan
```

Each skill checks the workspace for other skills' outputs and builds on them. `seo-geo-system` runs them in order:

1. **Fix:** `seo-audit`
2. **Measure:** `search-console-analysis`
3. **Compare:** `competitor-analysis` and `geo-visibility`
4. **Plan:** `content-planner`
5. **Improve and write:** `content-refresh` and `content-writer`
6. **Publish properly:** `internal-linking` and `structured-data`

Then, each month, it reruns the measurement skills and updates the plan.

## Built on Google's guidance

`shared/google-guidance.md` summarises Google's current advice, with links to the official pages. Every skill follows it. In short:

- For Google, **AEO and GEO are SEO.** AI Overviews and AI Mode use Google's core ranking systems, and there are no extra requirements to appear in them.
- What matters: original, first-hand content; pages that are crawlable, indexed and snippet-eligible; and a good page experience.
- What these skills never recommend for Google: llms.txt files, chunking content for AI, rewriting for AI, special AI markup, or chasing fake mentions.
- Other AI tools don't publish equivalent guidance, which is why `geo-visibility` measures their answers directly instead of guessing.

The file has a "checked" date. Google's guidance changes, so review it against the official links before relying on it.

## What you need

- **Claude** with web access. Browser access helps `geo-visibility`, but isn't essential.
- **Google Search Console** for the site. It's free and the best data source you have.
- **Optional:** a crawler export (Screaming Frog's free version crawls up to 500 URLs) and keyword data from any tool.

## Install

Download the skills you want, or clone this repo.

**Full set:** [all-skills.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/all-skills.zip)

**Individual skills:**

- [seo-geo-system.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/seo-geo-system.zip)
- [seo-audit.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/seo-audit.zip)
- [search-console-analysis.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/search-console-analysis.zip)
- [competitor-analysis.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/competitor-analysis.zip)
- [geo-visibility.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/geo-visibility.zip)
- [content-planner.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/content-planner.zip)
- [content-writer.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/content-writer.zip)
- [content-refresh.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/content-refresh.zip)
- [internal-linking.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/internal-linking.zip)
- [structured-data.zip](https://github.com/FaryalRazaBhatti/claude-seo-geo-skills/raw/main/dist/structured-data.zip)

**Claude (web, desktop and mobile apps):** upload each skill's zip under Settings, Capabilities, Skills. For the full system, upload all of them.

**Claude Code:** copy the folders inside `skills/` into `~/.claude/skills/` (or your project's `.claude/skills/`).

Then ask Claude naturally, for example "run a full SEO and GEO review of my site", "audit my site from this crawl export" or "check what ChatGPT says about my brand".

## What these skills won't do

- Invent traffic, rankings, volumes or statistics
- Guarantee rankings, rich results or inclusion in AI answers
- Mass-produce pages or copy competitors' content
- Change your website without showing you the changes first

## Examples

`examples/apple-uk/` shows `competitor-analysis` and `geo-visibility` run on public pages as worked examples. They aren't affiliated with or endorsed by any brand mentioned.

## Contributing

Edit files in `shared/` or `skills/`, then run `python3 scripts/build.py` to copy the shared files into every skill and rebuild the zips in `dist/`. `python3 scripts/build.py --check` confirms everything is in sync.

## Credit

Created by [Faryal Raza Bhatti](https://www.faryalrazabhatti.co.uk). If you use or adapt these skills, a credit and a link back are appreciated.

## Licence

MIT
