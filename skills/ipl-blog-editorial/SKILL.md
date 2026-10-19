---
name: ipl-blog-editorial
description: Plan, write, edit and publish articles for the Image Prompt Library blog ("Aprende") through the connected MCP, following the site's editorial line, format and SEO standards.
---

# Image Prompt Library — Blog editorial workflow

The blog teaches prompts and prompting to a general audience. Each article is a lesson, and the library's prompts embedded inside it are the live examples that show the lesson working. Read `references/editorial-line.md` (what to publish and how it should sound) and `references/article-format.md` (structure, Markdown cards, SEO) before writing. If `ipl-site-guide` is available, its house rules also apply.

## Article transaction

1. **Brief.** Infer from the request: one reader problem, one search intent, the pillar it belongs to, and the library prompts that solve it. If the topic falls outside the editorial line, say so and propose the closest in-scope angle.
2. **Preflight.** `library_overview`, then `list_posts(query=<topic>)` to avoid duplicating an existing article (read it with `get_post` and update it instead) and `list_prompts(status="published", query=<topic>)` to choose the prompts that demonstrate each point. An embedded prompt must already be published; if the ideal one does not exist, either embed the closest published one or flag the gap to the owner (creating it is the `ipl-prompt-publication` workflow).
3. **Research when facts are involved.** Model features, versions, prices, limits or dates must come from a primary source checked in this session, cited in the text and dated ("a octubre de 2026"). If you cannot verify a claim, remove it.
4. **Outline, then draft.** Title that promises a concrete result, an opening that answers the question in the first paragraph, `##` sections, at least one `{{prompt:slug}}` embed placed where the reader needs it, and a closing next step. Write in Spanish following the voice rules.
5. **Images.** Use real outputs (preferably from the embedded prompts) or images the owner provided. Upload with `add_post_image`: `role: cover` for the cover, `role: inline` returns Markdown to paste into the body. Every image gets a descriptive `alt`; captions credit the generator ("Generada con …"). Never use stock or search-result images without the owner's stated rights.
6. **Save as draft.** `save_post` with title, slug, description, body, tags, meta_title, meta_description, cover_alt, and `status: draft` unless publication was authorized. Re-read with `get_post` and check body rendering markers (embeds, image Markdown) survived.
7. **Self-review.** Run the checklist in `references/article-format.md`. Fix before publishing.
8. **Publish only when authorized.** `save_post` with `post` and `status: published`. If the server rejects embeds, publish the missing prompts first or replace the embed. Re-read and report: post id, public link (`/blog/<slug>`), status, embedded prompts, images uploaded, and what was not verified (rendering, indexing).

## Editing an existing article

Find it with `list_posts`, read it with `get_post`, change only what was asked, keep the slug of a published article (changing it breaks links), and preserve `published_at` unless the owner wants a new date. Report a short summary of what changed.

## Boundaries

Do not create, publish or delete library prompts while writing an article: report the missing example instead. Do not delete posts or remove covers (`remove_post_cover`) without an explicit request for that item. Do not publish sponsored, affiliate or promotional content without a visible disclosure and the owner's request.
