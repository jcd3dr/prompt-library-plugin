---
name: ipl-library-maintenance
description: Maintain and curate Image Prompt Library through the connected MCP - improve existing prompts, publish video prompts from supplied files, organize categories and tags, audit quality and SEO, and handle unpublish or delete requests safely.
---

# Image Prompt Library — Library maintenance and curation

Use this skill for every library task that is not creating a new image template (that is `ipl-prompt-publication`) or writing for the blog (`ipl-blog-editorial`). If `ipl-site-guide` is available, its house rules apply. Read `references/standards.md` before editing content: it defines what a good prompt record, category and tag look like.

## Improve an existing prompt

1. `get_prompt` and note `status`, `missing_to_publish`, media roles and IDs.
2. Change only what was asked or what the standards require. Metadata, education, SEO, fields and tags can be fixed without regenerating images.
3. Never edit the `prompt` text of a prompt with gallery images unless the images are regenerated from the new text: the gallery must remain the real output of the published prompt. If the owner wants a different prompt, propose a new template instead.
4. `update_prompt` sends the full `fields` and `tags` lists when changing them. A save that breaks a server rule moves a published prompt back to draft: check `status` in the response and report it.
5. Re-read with `get_prompt` and report what changed.

## Publish a video prompt (text2video / img2video)

Native video generation is usually not available in the host. Publish a video prompt only from files the owner supplies or explicitly authorizes (a public https URL or a file attached in the chat):
1. Preflight as for any prompt (`library_overview`, `list_prompts(status="all")`).
2. `create_prompt` with `type: "video"`, the matching mode, aspect ratio, English canonical prompt that produced the video, Spanish metadata and education following `references/standards.md`.
3. `add_image` with `role: "video"` (mp4/webm), `role: "poster"` (a frame of that same video), and for img2video `role: "input"`. Set `generator` to the tool the owner says made it; ask if unknown, never guess.
4. Watch the poster and, when the host can, the video before publishing; publish only when authorized and `missing_to_publish` is empty.

## Categories

- Prefer a few broad, reader-facing categories (what the reader wants to make), not one per prompt. Check `list_categories` before creating; `create_prompt`/`update_prompt` silently create a category from an unknown name, so match spelling exactly.
- `save_category` with a Spanish `name`, short `description` (shown as the category page intro) and optional thumbnail. A category page only appears when it has at least one published prompt.
- `delete_category` unpublishes every prompt in it. Before calling, list the affected prompts, propose where they should move, and get explicit confirmation.

## Tags

There is no rename or merge tool. To consolidate tags, update each affected prompt's full `tags` list with `update_prompt` (and posts with `save_post`). Use lowercase Spanish tags, 3–6 per prompt, reuse before creating.

## Audit the library

On request, read everything with `list_prompts(status="all")`, `get_prompt` per item and `list_posts`, then report in a table: drafts and what blocks each one (`missing_to_publish`), published prompts that miss the standards (education too thin, missing SEO fields, field values without examples, weak alt text, generic titles), near-duplicate prompts, categories with few or no published prompts, and orphan or near-duplicate tags. Propose fixes; apply only the ones the owner approves.

## Unpublish and delete

- Unpublish: `publish_prompt(publish: false)` when asked. Check `list_posts` first: a published article that embeds the prompt stops showing that card; tell the owner.
- Delete (`delete_prompt`, `delete_image`, `delete_category`, `delete_post`): irreversible. Only on an explicit request for that item. State what will be lost (files, embeds, unpublished prompts) and call with `confirm: true` only after the owner confirms.

## Boundaries

Do not regenerate images or change a published prompt's canonical text in this workflow. Do not bulk-edit or bulk-delete without a list the owner approved.
