---
name: ipl-library-maintenance
description: Organize and audit Image Prompt Library through the connected MCP - categories (including multiple categories per prompt and the «Sin categoría» fallback), tags, quality audits, old drafts, unused files, and safe unpublish or delete of prompts and articles.
---

# Image Prompt Library — Organization, audit and safe removal

With a large library, organization is what lets any visitor find what they want to make. Read `references/standards.md` before changing content: it defines what a good prompt record, category and tag look like.

## Categories (O1)

- Name categories after what the reader wants to make ("Retratos personales", "Vender en marketplace", "Invitaciones"), not after techniques.
- Check `list_categories` before creating one, and match spelling exactly. `create_prompt` and `update_prompt` create unknown names silently.
- Use `save_category` with:
  - A Spanish `name`.
  - A short `description`, shown as the page intro.
  - An optional thumbnail.
- A category page appears only when it has at least one published prompt.
- «Sin categoría» is the fallback. It has no public page, cannot be deleted, and is removed from a prompt automatically when that prompt gets another category.

## Reorganize (O2)

A prompt can belong to several categories; the first one is its primary category.

To restructure:
1. Propose the new structure as a table (category → prompts).
2. Apply only what the owner approves, with `update_prompt(categories=[…])`. Send the complete list each time.

Deleting a category:
1. Call `delete_category(category, confirm: false)` first. It returns which prompts would move to «Sin categoría» because it is their only category.
2. Show the owner that list and where you suggest moving each prompt.
3. Reassign the prompts if the owner agrees.
4. Call `delete_category(category, confirm: true)`.

Prompts never get unpublished by deleting a category.

## Tags (O3)

- Tags are lowercase Spanish, 3–6 per prompt. Reuse an existing tag before creating one.
- `save_tag` renames a tag. Renaming to an existing name merges the two tags ("retrato" + "retratos").
- `delete_tag(confirm: true)` removes a tag from every prompt. Use it only on an explicit request.
- Article tags change with `save_post`.

## Audit the library (O4)

On request:
1. Read everything: `list_prompts(status="all")`, `get_prompt` per item, and `list_posts` / `get_post` where needed.
2. Report in a table:
   - Drafts and what blocks each one (`missing_to_publish`).
   - Scheduled items and their dates.
   - Prompts below the standards.
   - Near-duplicate prompts.
   - Prompts left only in «Sin categoría».
   - Categories with few or no published prompts.
   - Duplicate tags.
   - Images with a missing or unclear generator, or weak alt text.
3. Propose fixes and apply only the ones the owner approves.

## Old drafts (O5)

1. List drafts with `list_prompts(status="draft")` and `list_posts(status="draft")`.
2. For each draft, say what it needs to be finished.
3. Decide with the owner which ones to finish and which to delete.
4. Delete only the drafts the owner names.

## Unused files

Removed inline blog images and replaced files can leave stored files that nothing uses.

1. Call `clean_orphan_files(confirm: false)` to list them. It only includes files older than 24 hours.
2. Show the owner the count and size.
3. Call `clean_orphan_files(confirm: true)` only after the owner approves. Deleting is irreversible.

## Unpublish and delete (P9, B9)

- **Unpublish a prompt** with `publish_prompt(publish: false)`. Check `embedded_in` from `get_prompt` first: published articles that embed the prompt stop showing that card. Tell the owner which articles are affected.
- **Delete anything** (`delete_prompt`, `delete_image`, `delete_category`, `delete_tag`, `delete_post`, `remove_post_cover`, `delete_idea`) only on an explicit request for that specific item. Deleting is irreversible.
  1. State what will be lost: files, embeds, links.
  2. Call with `confirm: true` only after the owner confirms.

## Boundaries

- Do not regenerate media or change a prompt's text in this workflow.
- Do not bulk-edit or bulk-delete without a list the owner approved.
