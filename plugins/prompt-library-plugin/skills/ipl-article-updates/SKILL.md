---
name: ipl-article-updates
description: Update a published Image Prompt Library blog article through the connected MCP - correct facts that changed, expand a section, or add a supporting prompt - without breaking its link and with a visible update date.
---

# Image Prompt Library — Update a published article

A published article has a link that people and search engines already use. Updates improve it in place.

## Update (B8)

1. Find the article with `list_posts(query=…)` and read it in full with `get_post`.
2. Confirm what must change:
   - A fact that changed. Re-verify it against a source checked today and record the date.
   - A section to expand.
   - A newly published prompt that supports a technique the article explains.
3. Edit only those parts, with the same voice and an editing pass over the changed text. Re-read the whole article for consistency.
4. When facts change, add a short dated line in the text, for example "Actualizado el 2 de noviembre de 2026: …". Do not silently change old claims.
5. Save with `save_post(post, …)`:
   - Keep the `slug`, because changing it breaks links.
   - Keep `published_at`, unless the owner wants a new date.
   - A new `{{prompt:slug}}` must point to a published prompt.
6. Re-read with `get_post` and report a short summary of what changed and what was verified.

## Boundaries

- Do not unpublish, delete or remove the cover in this workflow.
- If the owner wants a different article on the same topic, that is a new article, not an update.
