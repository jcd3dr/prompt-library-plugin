# MCP tool map

Server rules enforced on every client (web panel, WebMCP, remote MCP). Live schemas win over this file if they differ; re-read them when a call fails validation.

## Library state (read-only)

| Tool | Use it to | Notes |
|---|---|---|
| `library_overview` | Start every session | Returns rules, categories (the fallback one is flagged), tags and generators in use. |
| `list_prompts` | Find duplicates, drafts, gaps | `status`: all / draft / scheduled / published; optional `category` slug; `query` searches title, slug, summary, prompt, categories and tags (accent-insensitive). Renders the in-chat list view. |
| `get_prompt` | Read one prompt fully | Includes `missing_to_publish` (empty = server checks pass, not visual QA), `embedded_in` (articles that embed it) and `segments`. Renders the in-chat prompt card. |
| `list_categories` | Pick or audit categories | Includes published-prompt count per category. |
| `list_tags` | Reuse existing tags | Includes usage count. |
| `list_posts` | Find blog articles | Summaries without body. Optional `status` (all / draft / scheduled / published) and `query`. |
| `get_post` | Read one article fully | Body Markdown, SEO fields, cover and embeds. |
| `list_ideas` | Read the ideas bank | Filter by `status` (new / approved / discarded / done) and `kind` (prompt / article / any). |

## Prompts

| Tool | Use it to | Risks and rules |
|---|---|---|
| `create_prompt` | Start a draft | Only `title` required. `categories` (list of names or slugs; the first is the primary) creates unknown names: check spelling first. Optional `difficulty` (basico / intermedio / avanzado) and `prompt_es` (Spanish translation shown to the reader, never copied). |
| `update_prompt` | Change fields | Sends only what changes, but `fields`, `tags` and `categories` are replaced whole: send the complete list. Saving a published or scheduled prompt that breaks a rule returns it to draft. |
| `publish_prompt` | Publish (`publish: true`), schedule (`publish_at` future ISO 8601) or unpublish (`false`) | Fails with the list of problems if incomplete. Scheduled prompts publish automatically within about 15 minutes of the time. Renders the in-chat status card. |
| `delete_prompt` | Remove a prompt and all its files | Irreversible. `confirm: true` and an explicit request. |

Publication requirements (server): title, prompt ≥ 20 chars, `mode_help` ≥ 10 chars, at least one category, `img2*` modes need `role=input`, image prompts need ≥ 1 gallery image, video prompts need `role=video` plus a poster, every gallery image needs `generator`. Structural rules: `type=image` ↔ `*image` modes, `type=video` ↔ `*video` modes; `aspect_ratio` in 1:1, 9:16, 16:9, 4:5, 3:4; each `fields[].value` appears literally in `prompt`, with 2–6 examples.

## Prompt media

| Tool | Use it to | Risks and rules |
|---|---|---|
| `add_image` | Upload gallery, input, poster or video | Exactly one source. ChatGPT: `file` (attached or generated in chat). `url`: public https only. `base64`/`dataUrl` or no source (returns an upload URL): CLI clients only. Gallery max 4. Uploading input/poster/video replaces the previous one. `generator` = the tool that made that file, shown as "Generada con…". Optional `label` (≤ 60 chars) shown over the image. |
| `update_image` | Fix `generator`, `alt` or `label` | Metadata only. |
| `delete_image` | Remove one media file | Can make a published prompt incomplete. |
| `reorder_gallery` | Set gallery order | First image is the cover on cards. |

Static images are stored as WebP (1600 px plus a 640 px thumbnail). Animated WebP, GIF, AVIF and SVG are stored as they are; prefer animated WebP or a short MP4/WebM loop over GIF.

## Categories

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_category` | Create (no `id`) or edit (with `id`); optional thumbnail | Thumbnail stored as WebP; `remove_image` restores the automatic one. The fallback category «Sin categoría» cannot change its slug. |
| `delete_category` | Remove a category (`category` = id, slug or name) | `confirm: false` returns the impact: which prompts move to «Sin categoría» because it was their only category. `confirm: true` deletes. Prompts keep their status. The fallback cannot be deleted. |

## Tags

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_tag` | Create (no `tag`) or rename (`tag` = id, slug or name) | Renaming to an existing name merges both tags. Prompts only; article tags change with `save_post`. |
| `delete_tag` | Remove a tag from every prompt | `confirm: true` and an explicit request. |

## Blog

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_post` | Create (no `post`) or edit (with `post`) an article | Markdown body. `status`: draft, scheduled (needs a future `published_at`) or published (needs authorization, `description` ≥ 20 chars, and every `{{prompt:slug}}` embed must point to a published prompt, or a scheduled one for scheduled posts). |
| `add_post_image` | Upload a cover (`role: cover`) or inline image | Inline returns ready-made Markdown to paste into `body`. Stored as WebP. |
| `remove_post_cover` | Remove an article's cover and its file | Explicit request only. |
| `delete_post` | Remove an article and its images | Irreversible. `confirm: true` and an explicit request. |

## Ideas and files

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_idea` | Add (no `idea`) or update (with `idea` id): title, notes, kind, source, status, linked `prompt` or `post` | Agents propose with status `new`; only the owner approves or discards. |
| `delete_idea` | Remove an idea (`idea` id) | `confirm: true` and an explicit request. |
| `clean_orphan_files` | List (`confirm: false`) or delete (`true`) stored files nothing references, older than 24 h | Irreversible. Always show the list first. |

## Not available through the MCP

Visitor analytics, search-console data, comments, newsletter, user accounts, saving prompts for visitors, payments, deleting a single inline blog image (remove it from the body; cleanup collects the file later), and media generation (that depends on the host). Do not imply any of these were done; tell the owner when a task needs them.
