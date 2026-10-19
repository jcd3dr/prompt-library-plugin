# MCP tool map

Server rules enforced on every client (web panel, WebMCP, remote MCP). Live schemas win over this file if they differ; re-read them when a call fails validation.

## Library state (read-only)

| Tool | Use it to | Notes |
|---|---|---|
| `library_overview` | Start every session | Returns rules, categories, tags and generators in use. |
| `list_prompts` | Find duplicates, drafts, gaps | `status`: all / draft / published; optional `category` slug; `query` searches title, slug, summary, prompt, category and tags (accent-insensitive). |
| `get_prompt` | Read one prompt fully | Includes `missing_to_publish` (empty = server checks pass, not visual QA) and `embedded_in`: articles that embed it. |
| `list_categories` | Pick or audit categories | Includes published-prompt count per category. |
| `list_tags` | Reuse existing tags | Includes usage count. |
| `list_posts` | Find blog articles | Summaries without body: status, description, tags, link and embedded prompt slugs. Optional `status` and `query`. |
| `get_post` | Read one article fully | Body Markdown, SEO fields, cover and embeds. |

## Prompts

| Tool | Use it to | Risks and rules |
|---|---|---|
| `create_prompt` | Start a draft | Only `title` required. `category` by name creates it if new: check spelling against existing ones first. |
| `update_prompt` | Change fields | Sends only what changes, but `fields` and `tags` are replaced whole: send the complete list. Saving a published prompt that breaks a rule returns it to draft. |
| `publish_prompt` | Publish (`publish: true`) or unpublish (`false`) | Fails with the list of problems if incomplete. Publish only with authorization. |
| `delete_prompt` | Remove a prompt and all its files | Irreversible. Requires `confirm: true` and the owner's explicit request. |

Publication requirements (server): title, prompt ≥ 20 chars, `mode_help` ≥ 10 chars, a category, `img2*` modes need `role=input`, image prompts need ≥ 1 gallery image, video prompts need `role=video` plus a poster, every gallery image needs `generator`. Structural rules: `type=image` ↔ `*image` modes, `type=video` ↔ `*video` modes; `aspect_ratio` in 1:1, 9:16, 16:9, 4:5, 3:4; each `fields[].value` appears literally in `prompt`, with 2–6 examples.

## Prompt media

| Tool | Use it to | Risks and rules |
|---|---|---|
| `add_image` | Upload gallery, input, poster or video | Exactly one source. ChatGPT: `file` (attached or generated in chat). `url`: public https only. `base64`/`dataUrl` or no source (returns an upload URL): CLI clients only. Gallery max 3. Uploading input/poster/video replaces the previous one. Always set `generator` truthfully. |
| `update_image` | Fix caption (`generator`) or `alt` | Metadata only. |
| `delete_image` | Remove one media file | Can make a published prompt incomplete. |
| `reorder_gallery` | Set gallery order | First image is the cover on cards. |

## Categories

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_category` | Create (no `id`) or edit (with `id`); optional thumbnail | Thumbnail stored as WebP; `remove_image` restores the automatic one. |
| `delete_category` | Remove a category | Its prompts lose their category and are unpublished. Report how many (`prompts_unpublished`). Explicit request only. |

## Tags

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_tag` | Create (no `tag`) or rename (`tag` = id, slug or name) | Renaming to an existing name merges both tags. Applies to prompts only; article tags change with `save_post`. |
| `delete_tag` | Remove a tag from every prompt | Requires `confirm: true` and an explicit request. |

## Blog

| Tool | Use it to | Risks and rules |
|---|---|---|
| `save_post` | Create (no `post`) or edit (with `post`) an article | Markdown body. `status: published` publishes immediately: needs authorization, `description` ≥ 20 chars, and every `{{prompt:slug}}` embed must point to a published prompt. |
| `add_post_image` | Upload a cover (`role: cover`) or inline image | Inline returns ready-made Markdown to paste into `body`, then save with `save_post`. Stored as WebP. |
| `remove_post_cover` | Remove an article's cover and its file | Explicit request only. |
| `delete_post` | Remove an article and its images | Irreversible. Requires `confirm: true` and an explicit request. |

## Not available through the MCP

Visitor analytics, search-console data, comments, newsletter, user accounts, payments, deleting a single inline blog image (remove it from the body instead), and media generation (that depends on the host). Do not imply any of these were done; tell the owner when a task needs them.
