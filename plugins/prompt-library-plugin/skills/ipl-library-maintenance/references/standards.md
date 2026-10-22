# Library content standards

## A complete prompt record

| Field | Standard |
|---|---|
| `title` | Spanish, says what the reader gets ("Foto de producto en estudio con luz suave"), not just the name of the technique. |
| `summary` | 1–2 Spanish sentences: the result and when to use it. Shown on cards. |
| `prompt` | One complete English instruction that produced the results; never edited after the fact. |
| `prompt_es` | A faithful Spanish translation that helps the reader understand the prompt; shown, never copied. |
| `mode` / `mode_help` | Correct mode. `mode_help` says in Spanish what the reader must supply. |
| `fields` | 2–5 parts, each controlling a different aspect. Each `value` appears literally in `prompt`, with 2–6 grammatical English examples and a Spanish `label`. |
| `education` | Spanish Markdown: why it works, how to adapt each part, variations, known limitations, and checks before commercial use. |
| `difficulty` | basico / intermedio / avanzado. |
| `model` | The tool actually used for the results. |
| `categories` | One or more reader-facing categories, primary first; never only «Sin categoría» when published. |
| `tags` | 3–6, lowercase Spanish, reused. |
| `access` | `free` unless the owner says premium. |
| `meta_title` / `meta_description` | At most 60 / 160 characters, Spanish, including the main search phrase. |
| gallery | 1–4 real outputs of this prompt. Each has its true `generator`, a descriptive Spanish `alt`, and an optional short `label`. The first image is the cover. |
| input | For img2* modes, the exact source used. Fictional inputs are never presented as a real customer product. |

## Voice for public text

Plain everyday Spanish for a general audience with no prompt knowledge, addressing the reader as "tú". Direct and practical, short paragraphs, technical terms explained the first time, no hype. Prompt text and fragments stay in English.

## Categories

- **Name:** what the reader wants to make, covering everyday and business goals ("Retratos personales", "Vender en marketplace", "Producto", "Miniaturas", "Invitaciones", "Video para redes").
- **Description:** 1–2 Spanish sentences, used as the intro of the category page.
- **Thumbnail:** a representative real result, or the automatic one.

## Red flags to report in audits

- A gallery image whose generator or origin is unclear, or that looks like it came from another prompt.
- A real brand, logo or identifiable real person without stated rights.
- Education copied between prompts, or shorter than about 3 short paragraphs.
- A title or SEO fields identical to another prompt's.
- A published prompt whose `missing_to_publish` is not empty. This should not happen; report it.
- A published prompt whose only category is «Sin categoría».
