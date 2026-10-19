---
name: ipl-prompt-publication
description: Create, test, document and publish one reusable prompt template (image or video, any mode) for the public Image Prompt Library through the connected MCP. This is the site's core workflow.
---

# Image Prompt Library — Prompt template publication

Publishing prompts is what this site is for. Each published prompt is a **reusable teaching template**: a canonical English prompt anyone can copy, the real result it produced, customizable fields, and Spanish education that explains why it works and how to adapt it. The deliverable is never an editing service for the requester, a UI mockup, or a prompt card image.

Read all four references before editing content: `references/creative-prompt.md`, `references/visual-qa.md`, `references/page-content-seo.md`, and `references/mcp-execution.md`. Use the actual connected MCP tool schemas.

## Choose the template type

| Type / mode | The reader supplies | Demonstration media to publish |
|---|---|---|
| image · `text2image` | only the prompt | 1–3 gallery results |
| image · `img2image` | their own photo plus the prompt | input photo (`role: input`) + gallery result |
| video · `text2video` | only the prompt | video (`role: video`) + poster frame (`role: poster`) |
| video · `img2video` | their own image plus the prompt | input image + video + poster frame |

## One-template transaction

1. **Intake.** Infer the reader the template serves (see `references/page-content-seo.md`), the reproducible outcome, type, mode, format and identity constraints. An instruction to create and publish authorizes the complete transaction subject to QA. Ask for a source asset only when the task is about the owner's own asset. For a new img2* template with no supplied reference, **create a fictional source image autonomously as a demonstration fixture**. Do not invent real product branding or factual claims.
2. **Preflight.** Call `library_overview`, then `list_prompts(status="all", query=<topic>)` and `get_prompt` on matches to avoid duplicates. For an existing draft, use `update_prompt` without destroying prior media. Choose an existing reader-facing category, aspect ratio, free access by default, and 2–5 useful customizable fields.
3. **Lock the canonical prompt.** Write one complete English instruction that a reader can reuse (subject, hierarchy, camera, space, lighting, motion for video, prohibitions). Each field default must occur literally in the prompt. Keep the exact prompt as the visible pre-generation record. Never alter it after generating to make a failed result look correct.
4. **Prepare a fictional input where applicable.** For img2* without a user-supplied image, create exactly ONE neutral fictional source image with a **separate source-asset prompt**, inspect it, and keep its real file ID. Never regenerate a user-provided source.
5. **Execute exactly once.** Generate with the host's native generator (GPT Image in ChatGPT for images). One execution produces one identifiable output file, never a collage, prompt card, website mockup or set of candidates. If the host has no native generator for the type (common for video), use only files the owner supplies or a generator the owner explicitly authorizes, and record that tool truthfully. Never switch generators silently. Do not claim byte-for-byte transmission of the prompt unless verified.
6. **QA.** Inspect the actual result against the locked prompt following `references/visual-qa.md`. For img2* compare input and output explicitly. A hard mismatch, missing input or inaccessible output stops publishing. Do not retry or switch providers without permission.
7. **Publish the complete educational record.** Create or update the draft with Spanish title, summary, mode_help, education, alt text and SEO; the exact English canonical prompt; the true `model`; validated fields; 3–6 tags; the right category. Upload media with `add_image` and the real file (`file` in ChatGPT): `input`, then `gallery` (image) or `video` + `poster` (video), each with its true `generator`. Never upload search results, substitutes or screenshots of the prompt.
8. **Re-read and finalize.** `get_prompt` must confirm the exact canonical prompt, correct distinct media roles and IDs, metadata, category and `missing_to_publish=[]`. With publication authorized and QA passed, call `publish_prompt` once and re-read to verify `published`. Report real IDs, public and admin links, generator, media roles and limitations. Database publication does not prove page rendering or search indexing.

## Rules

Communicate with the owner in their language; prompts and field values in English; public educational text in Spanish. Do not delete content, replace existing media or republish an existing item without a targeted request. Successful database validation is not visual QA.
