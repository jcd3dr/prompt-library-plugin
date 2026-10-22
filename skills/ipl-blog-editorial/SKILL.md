---
name: ipl-blog-editorial
description: Write and publish a new Image Prompt Library blog article ("Aprende") through the connected MCP with a full editorial process - outline, draft, separate editing pass, optional supporting prompts, images, SEO, draft, review and publication or scheduling.
---

# Image Prompt Library — Write a blog article

The article is the product of this workflow. Every article is about prompts, prompting techniques or something closely related. Writing it is an editorial process with distinct steps, not "write a text and save it."

Read `references/editorial-line.md` (what to publish and how it should sound) and `references/article-format.md` (structure, Markdown, SEO, checklist) before writing.

## Editorial process

1. **Topic and angle.** Start from the owner's topic or an approved idea (`list_ideas`). Define one reader problem, one search intent and the promise of the article. Check `list_posts(query=…)`: if an article already covers it, propose updating that one instead.
2. **Research.** Every fact about tools must come from a source checked in this session, with its date. If you have a research brief, use it. Otherwise gather the sources first. What you cannot verify stays out.
3. **Outline (B3).** Write the title, the promise, the sections in order with the key point of each, the examples, and the images needed. Every section must earn its place.
4. **Draft (B4).** Write a complete draft in plain Spanish following the voice rules. Answer the question in the opening paragraph. Put prompt fragments in English inside code formatting.
5. **Editing pass (B4).** Do a separate pass that re-reads the draft as an editor:
   - Accuracy against the sources.
   - Clarity for someone with no knowledge.
   - Structure.
   - Repetition.
   - Spelling and accents.

   Cut what does not help the reader.
6. **Supporting prompts (B5, optional).** Do this only when the article explains a technique that a published prompt already demonstrates. Insert `{{prompt:slug}}` on its own line right after that explanation, with one sentence on what to look at. There is no minimum and no gap to report: an article with no embeds is complete.
7. **Images and SEO (B6).**
   - Upload the cover and inline images with `add_post_image`. Inline images return Markdown to paste into the body.
   - Images are real outputs or come from the owner. Each has a descriptive `alt` and a caption naming the tool that generated it.
   - Write the description, `meta_title`, `meta_description`, tags and `cover_alt`.
8. **Save as draft and review (B7).** Call `save_post` with `status: draft`. Then re-read it with `get_post` and run the checklist in `references/article-format.md`.
9. **Publish or schedule (B7).** Only when authorized:
   - Publish with `save_post(post, status: "published")`.
   - Or, if the owner gave a date, schedule with `status: "scheduled"` and a future `published_at`.

   If the server rejects an embed, publish that prompt first or remove the embed. Then report:
   - Post id and link (`/blog/<slug>`).
   - Status, and the date if scheduled.
   - Embeds used.
   - Images uploaded.
   - What was not verified.

   If the article came from an idea, `save_idea(idea, status: "done", post: <slug>)`.

## Boundaries

- Do not create, publish or delete library prompts while writing an article.
- Do not publish sponsored, affiliate or promotional content without a visible disclosure and the owner's request.
- Do not delete posts or covers in this workflow.
