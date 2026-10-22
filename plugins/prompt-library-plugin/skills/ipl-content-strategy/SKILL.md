---
name: ipl-content-strategy
description: Decide what Image Prompt Library should publish next through the connected MCP - content calendars, library gaps by category, site-wide SEO review, and thematic series that combine several prompts with an article - before any content is built.
---

# Image Prompt Library — Content strategy

These processes decide what to make before anything is made. Their output is a plan the owner approves. Building the content happens afterwards, one item at a time.

## Content calendar (E1)

1. Read the current state:
   - `list_prompts(status="all")` and `list_posts(status="all")`, including scheduled items and their dates.
   - `list_ideas`, using approved ideas first.
2. Research current trends and what people look for, citing sources with dates.
3. Propose a calendar for the coming weeks as a table with these columns:
   - date
   - type (prompt or article)
   - working title
   - category
   - why now
   - source idea
4. Once the owner approves:
   - Save new items as ideas with `save_idea`, using status `approved` only when the owner approved them.
   - Use dates as scheduling targets (`publish_at` / scheduled posts) when each piece is built.

## Library gaps (E2)

1. Compare what each category has (`list_categories`, `list_prompts(category=…)`) with what readers would want to make in that area.
2. Look for missing everyday goals, missing modes (img2image, video) and categories with too few prompts.
3. Deliver a prioritized list of new prompts, giving for each the reader goal, mode and category. Save the list as ideas when the owner wants.

## Site SEO review (E3)

Review titles, meta descriptions, slugs and internal links across prompts and articles.

Look for:
- Duplicates.
- Items competing for the same search phrase.
- Missing fields.
- Over-long fields.
- Articles that could link to related prompts or articles.

The MCP has no traffic or search-console data. Judge the content only, never claimed performance, and say so in the report. Propose concrete changes; apply only what the owner approves.

## Thematic series (E4)

A series covers one topic with several prompts in one category plus an article that teaches the technique and is supported by them.

Plan it as a set:
- The prompts, each with its goal and mode.
- The article's angle.
- The publication order, prompts before the article so the embeds are valid.
- Suggested dates.

Save the pieces as linked ideas. Each piece is then built through the normal prompt and article processes.

## Boundaries

- Strategy does not publish, edit or delete anything.
- Never invent search volumes, traffic or rankings.
