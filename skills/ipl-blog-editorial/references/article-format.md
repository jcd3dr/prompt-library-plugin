# Article format and SEO

## Structure

- **Title.** A concrete result or question, in Spanish, ideally 60 characters or fewer.
- **Opening.** The first paragraph gives the short answer, then says why it matters.
- **Body.** `##` sections, each solving one step. Use lists for steps, `>` for key rules, and `---` only between major parts.
- **Supporting prompts (optional).** `{{prompt:slug}}` alone on a line, right after the explanation it illustrates, introduced by one sentence on what to look at or change.
- **Closing.** One concrete next step. No generic summary.
- **Length.** Typically 600–1500 words. Shorter is fine when the answer is short.

## Markdown the site renders

- Image with caption: `![alt text](url "caption")`. `add_post_image(role: "inline")` returns it ready-made.
- Prompt card: `{{prompt:slug}}` alone on a line. The prompt must be published, or scheduled for a scheduled article.
- Quotes `>`, lists, `##`/`###` headings, `---`, and inline `code` for prompt fragments.
- Internal links as relative paths: `/prompts/<slug>`, `/categorias/<slug>`, `/blog/<slug>`.

## Metadata

| Field | Rule |
|---|---|
| `slug` | Short Spanish words, no accents, hyphenated. Never change it once published. |
| `description` | 1–2 sentences, at least 20 characters (required to publish). |
| `meta_title` | 60 characters or fewer, main search phrase near the start. Empty uses the title. |
| `meta_description` | 160 characters or fewer, states the result the reader gets. Empty uses the description. |
| `tags` | 2–5, reused, lowercase Spanish. |
| cover | `add_post_image(role: "cover")` with descriptive `alt`. Set `cover_alt` too. |
| `author` | Leave empty unless the owner names one. |
| `status` / `published_at` | Draft by default. For scheduled, use a future ISO 8601 date. Published only with authorization. |
| `canonical_url` | Only when the article was first published elsewhere. |
| `noindex` | false unless the owner wants it hidden. |

## Pre-publication checklist

- [ ] One reader problem, answered in the first paragraph.
- [ ] Went through outline, draft and a separate editing pass.
- [ ] Fits a content pillar and the voice rules; no hype, no filler.
- [ ] Every factual claim about a tool is sourced and dated, or removed.
- [ ] Any embedded prompt is published (or scheduled) and placed where it supports the explanation.
- [ ] Images are real outputs or owner-provided, with `alt` and the generating tool in the caption.
- [ ] No real brands, logos or people without stated rights.
- [ ] Metadata complete and within limits; tags reused.
- [ ] Internal links resolve to published items.
- [ ] Spelling and accents checked; prompt fragments in English inside code formatting.
