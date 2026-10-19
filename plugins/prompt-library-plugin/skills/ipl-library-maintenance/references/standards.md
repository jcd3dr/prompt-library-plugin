# Library content standards

## A complete prompt record

| Field | Standard |
|---|---|
| `title` | Spanish, says what the reader gets ("Foto de producto en estudio con luz suave"), not the technique name alone. |
| `summary` | 1–2 Spanish sentences: the result and when to use it. Shown on cards. |
| `prompt` | One complete English instruction that produced the gallery; never edited after the fact. |
| `mode` / `mode_help` | Correct mode; `mode_help` explains in Spanish what the reader must supply (e.g. which photo to upload for img2image) and where to paste the prompt. |
| `fields` | 2–5 meaningful customizable spans whose `value` appears literally in `prompt`, each with 2–6 grammatical English examples; Spanish `label`. |
| `education` | Spanish Markdown: why it works (which fragments control what), how to adapt the fields, variations, known model limitations, checks before commercial use. No promises the gallery does not show. |
| `model` | The tool actually used for the gallery. |
| `category` | Existing reader-facing category. |
| `tags` | 3–6, lowercase Spanish, reused. |
| `access` | `free` unless the owner says premium. |
| `meta_title` / `meta_description` | ≤ 60 / ≤ 160 characters, Spanish, include the main search phrase. |
| gallery | 1–3 real outputs of this prompt, each with true `generator` and descriptive Spanish `alt`; first image is the cover. |
| input | For img2* modes, the exact source used; fictional fixtures must not be presented as a real customer product. |

## Voice for public text

Neutral Spanish, "tú", direct and practical, short paragraphs, no hype. Prompt text and fragments in English.

## Categories

Name: what the reader wants to make (e.g. "Producto", "Retrato", "Miniaturas", "Video para redes"). Description: one or two Spanish sentences used as the category page intro. Thumbnail: a representative real result, or the automatic one.

## Red flags to report in audits

- Gallery image whose generator or origin is unclear, or that looks like it came from another prompt.
- Real brand, logo or identifiable real person without stated rights.
- Education copied between prompts, or under ~3 short paragraphs.
- Title or SEO fields identical to another prompt's.
- Published prompt whose `missing_to_publish` is not empty (should not happen; report it).
