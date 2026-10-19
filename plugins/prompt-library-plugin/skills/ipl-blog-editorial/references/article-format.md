# Article format and SEO

## Structure

- **Title**: a concrete result or question the reader has, in Spanish, ideally ≤ 60 characters ("Cómo escribir un prompt de foto de producto que se vea profesional").
- **Opening** (first paragraph): the short answer. Then why it matters.
- **Body**: `##` sections, each solving one step. Lists for steps, `>` quotes for key rules, `---` only to separate major parts.
- **Embeds**: at least one `{{prompt:slug}}` on its own line, right after the explanation it illustrates. Introduce it with one sentence telling the reader what to change.
- **Closing**: one concrete next step (try a variation, open a category, read a related article). No generic summary.
- Typical length: 600–1500 words. Shorter is fine when the answer is short.

## Markdown cards the site renders

- Image with caption: `![alt text](url "caption")`. Get it ready-made from `add_post_image(role: "inline")`.
- Embedded prompt card: `{{prompt:slug}}` alone on a line. The prompt must be published before the article can be published.
- Quotes `>`, ordered and unordered lists, `##`/`###` headings, `---` separator, inline `code` for prompt fragments.
- Internal links as relative paths: `/prompts/<slug>`, `/categorias/<slug>`, `/blog/<slug>`.

## Metadata

| Field | Rule |
|---|---|
| `slug` | Short Spanish words, no accents, hyphenated. Never change it once published. |
| `description` | 1–2 sentences, ≥ 20 characters (required to publish). Shown on cards and as fallback meta description. |
| `meta_title` | ≤ 60 characters, main search phrase near the start. Empty = title. |
| `meta_description` | ≤ 160 characters, states the result the reader gets. Empty = description. |
| `tags` | 2–5, reuse existing tags from `library_overview` / `list_tags`; lowercase Spanish. |
| cover | `add_post_image(role: "cover")` with descriptive `alt`; set `cover_alt` too. Prefer a real result from an embedded prompt. |
| `author` | Leave empty (site name) unless the owner specifies an author. |
| `published_at` | Leave empty to use publication time; set ISO 8601 only for scheduled or backdated posts the owner requested. |
| `canonical_url` | Only when the article was first published elsewhere. |
| `noindex` | false unless the owner wants it hidden from search. |

## Pre-publication checklist

- [ ] One reader problem, answered in the first paragraph.
- [ ] Fits a content pillar and the voice rules; no hype, no filler.
- [ ] Every factual claim about a model is sourced and dated, or removed.
- [ ] At least one embedded prompt, already published, introduced with what to change.
- [ ] Images are real outputs or owner-provided, with `alt` and generator credit.
- [ ] No real brands, logos or people without stated rights.
- [ ] Metadata complete and within limits; tags reused.
- [ ] Internal links resolve to existing published items.
- [ ] Spelling and accents checked; prompt fragments in English inside code formatting.
