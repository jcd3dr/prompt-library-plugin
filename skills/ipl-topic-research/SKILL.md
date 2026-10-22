---
name: ipl-topic-research
description: Find what to write or build next for Image Prompt Library and research a chosen topic - trends, what people search for, tool news, reliable sources - and keep the site's ideas bank up to date through the connected MCP.
---

# Image Prompt Library — Topic research and ideas bank

The site covers prompts, prompting techniques and everything around image and video generation. This workflow decides *what* to make and gathers the facts to make it well. It does not write the final article or build the prompt.

## Find topics (B1)

Use this when the owner asks for "a new article" or "new prompts" without a topic.

1. Read what exists:
   - `list_ideas(status="new")` and `list_ideas(status="approved")`, so you never propose a duplicate idea.
   - `list_posts(status="all")` and `list_prompts(status="all")`, so you never repeat covered ground.
2. Research outside the site with your web search:
   - Current trends in image and video generation.
   - What people ask and search for, such as forums, "how to" queries and social posts.
   - Recent tool releases and changes.
   - Gaps in the blog and the library.
3. Propose 3–5 topics. For each give:
   - The angle.
   - Who it helps.
   - Why now.
   - Whether it suits an article, a prompt or both.

   The owner picks, or you pick when they asked you to.
4. Save each proposal with `save_idea`:
   - `title`: one Spanish sentence.
   - `notes`: angle, audience, why now, and key facts with source and date.
   - `kind`: prompt, article or any.
   - `source`: URL or "pedido del dueño".
   - `status`: `new`.

   Only the owner approves or discards ideas. When an idea becomes content, set `status: done` and link `prompt` or `post`.

## Research a chosen topic (B2)

1. Study how the technique works and how today's tools respond to it. Also gather common mistakes and reliable sources: official documentation, the tool's own pages, and reputable guides.
2. Record every fact with its source URL and the date you checked it. A fact you cannot verify in this session stays out.
3. Note which published prompts already demonstrate the technique (`list_prompts(status="published", query=…)`). They are optional support for an article, never a requirement.
4. Deliver a short research brief: the key points, the facts with their sources, open questions, and the published prompts that could support it. Store the brief in the idea's `notes` when an idea exists.

## Boundaries

- Do not publish anything in this workflow.
- Do not present trends as data without a source.
- Do not invent search volumes or statistics.
- The MCP has no analytics or search-console data. Say so if a decision needs them.
