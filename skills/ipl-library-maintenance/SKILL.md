---
name: ipl-library-maintenance
description: Maintain and curate Image Prompt Library through the connected MCP - improve existing prompts, organize categories and tags, audit quality and SEO, and handle unpublish or delete requests safely.
---

# Image Prompt Library — Library maintenance and curation

Use this skill to keep the existing library healthy as it grows. If `ipl-site-guide` is available, its house rules apply. Read `references/standards.md` before editing content: it defines what a good prompt record, category and tag look like.

## Improve an existing prompt

1. Find it with `list_prompts(query=…)`, then `get_prompt` and note `status`, `missing_to_publish`, media roles and IDs, and `embedded_in`.
2. Change only what was asked or what the standards require. Metadata, education, SEO, fields and tags can be fixed without regenerating images.
3. Never edit the `prompt` text of a prompt with gallery images unless the images are regenerated from the new text: the gallery must remain the real output of the published prompt. If the owner wants a different prompt, propose a new template instead.
4. `update_prompt` sends the full `fields` and `tags` lists when changing them. A save that breaks a server rule moves a published prompt back to draft: check `status` in the response and report it.
5. Re-read with `get_prompt` and report what changed.

## Categories

- Prefer a few broad, reader-facing categories (what the reader wants to make), not one per prompt. Check `list_categories` before creating; `create_prompt`/`update_prompt` silently create a category from an unknown name, so match spelling exactly.
- `save_category` with a Spanish `name`, short `description` (shown as the category page intro) and optional thumbnail. A category page only appears when it has at least one published prompt.
- `delete_category` unpublishes every prompt in it. Before calling, list the affected prompts, propose where they should move, and get explicit confirmation.

## Tags

Use lowercase Spanish tags, 3–6 per prompt, reuse before creating. `save_tag` renames a tag (`tag` = id, slug or name); renaming to an existing name merges both. `delete_tag` removes a tag from every prompt (explicit request, `confirm: true`). These affect prompts only: article tags change with `save_post`.

## Audit the library

On request, read everything with `list_prompts(status="all")`, `get_prompt` per item, `list_posts` and `get_post` where needed, then report in a table: drafts and what blocks each one (`missing_to_publish`), published prompts that miss the standards (education too thin, missing SEO fields, field values without examples, weak alt text, generic titles), near-duplicate prompts, categories with few or no published prompts, and orphan or near-duplicate tags. Propose fixes; apply only the ones the owner approves.

## Unpublish and delete

- Unpublish: `publish_prompt(publish: false)` when asked. Check `embedded_in` from `get_prompt` first: published articles that embed the prompt stop showing that card; tell the owner which ones.
- Delete (`delete_prompt`, `delete_image`, `delete_category`, `delete_tag`, `delete_post`, `remove_post_cover`): irreversible. Only on an explicit request for that item. State what will be lost (files, embeds, unpublished prompts) and call with `confirm: true` only after the owner confirms.

## Boundaries

Do not regenerate images or change a published prompt's canonical text in this workflow. Do not bulk-edit or bulk-delete without a list the owner approved.
