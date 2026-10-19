# Editorial line

## Mission

Teach anyone to write and use good image and video prompts. Every article is a lesson about prompts or prompting, and inside the lesson the reader finds real prompts from the library that demonstrate exactly what is being explained, with their results in view. The reader learns the idea and, in the same place, copies a working example. Every article should leave the reader able to do something new today.

## Reader

The general public: anyone who wants to use image or video prompts but does not know how to write good ones. An individual who wants photos of themselves in different styles, someone selling their car or a phone on a marketplace, a street vendor, a parent preparing an invitation, as well as creators, marketers, small sellers and designers. Most have no prior knowledge. They want practical outcomes, not theory. They read on mobile, skim first, and copy prompts.

## Content pillars

1. **Técnica de prompting** — how a prompt is built and what each part controls: subject, composition, light, lens and camera, materials, style, motion for video, what to exclude. Explained through before/after examples.
2. **Casos de uso** — complete recipes for everyday and business goals: selling something on a marketplace, personal portraits in different styles, product photos, thumbnails, invitations, social posts, short video clips. Each covers what the AI must guarantee for that goal (for example, that a product for sale is shown honestly).
3. **Modos y herramientas** — text-to-image vs image-to-image, text/image-to-video, and how different generators respond. Only verified, dated comparisons.
4. **Flujo de trabajo** — iterating one change at a time, adapting the library's customizable fields, keeping a consistent look, checking an image before commercial use (rights, text, artifacts, likeness).

Everything related to prompts and prompting is in scope. Off-line by default: AI news without a practical takeaway, opinion or hype pieces, general AI ethics debates, tutorials for tools unrelated to image or video generation, clickbait lists.

## Voice

- Plain everyday Spanish, neutral and international, for a general audience; address the reader as "tú". Explain every technical term in one phrase the first time. Avoid regionalisms and anglicisms with a common Spanish equivalent (keep accepted terms such as "prompt").
- Direct, practical, warm. Like an experienced colleague showing their method, not a guru.
- Short paragraphs (2–4 lines), concrete examples over abstractions, one idea per section.
- No hype words ("revolucionario", "increíble", "el secreto que nadie te cuenta"), no filler intros, no promises of guaranteed results.
- Prompt text and prompt fragments in English inside code formatting; explain what each fragment does in Spanish.

## Standards of truth

- Show real outputs of the prompts discussed; never present an image from another prompt or tool as the result.
- Facts about models (features, versions, limits, prices) need a primary source checked in the session and a date. If unverifiable, leave it out.
- No invented statistics, testimonials or case studies. No real brands, logos or people's likeness without stated rights; use fictional examples.
- Correct a published error openly when the owner asks for a fix; do not silently change claims of fact on an old article without noting the update date in the text.

## Relationship with the library

The blog and the library are one teaching system: the article is the lesson, the embedded prompt is the worked example. Each article embeds at least one published prompt with `{{prompt:slug}}` right where it demonstrates the point being taught, and tells the reader what to look at and what to change. Use `list_prompts(status="published", query=…)` to find them. When no prompt demonstrates a key point, flag the gap so a new template can be published first. Premium content, when it exists, may be mentioned as a next step, never as a requirement to understand the article.
