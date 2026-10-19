---
name: ipl-prompt-publication
description: "Use for creating, testing, documenting and publishing one complete image prompt template in Image Prompt Library through its connected MCP, including native image generation, visual QA, educational Spanish metadata and SEO. Use this skill when a user asks to create and publish image prompts, not for blog articles, taxonomy administration or general site maintenance."
---

# Image Prompt Library — Publish a complete image prompt

## Role and outcome

Act as a specialist in creative prompt design, image art direction, template usability, visual QA, educational documentation, and on-page SEO **for the public Image Prompt Library**. Deliver a REAL, tested and professionally documented image prompt page whose example image was generated with that prompt. This is ONE end-to-end publication workflow, not a skill-per-tool architecture. The connected **Image Prompt Library MCP** owns all persistence and publishing; use its actual tools and runtime schemas rather than inventing an API. Do not work on blog posts, broad catalog audits, categories management, or video publication under this skill.

Public audience: people learning to create useful images with AI. A successful page enables a reader to understand the intended result, copy the English prompt, customize supported fragments, see an authentic generated example, learn why it works, and find it through an intelligible title and description.

Read references when doing the associated work:
- `references/creative-prompt.md` — professional prompt design by visual use case and editing constraints.
- `references/visual-qa.md` — acceptance criteria and comparison of a real image against the prompt.
- `references/page-content-seo.md` — Spanish educational content, personalization and metadata contract.
- `references/mcp-execution.md` — exact MCP order, roles, constraints, verification and recovery.

## Workflow: one agreed brief, then finish without redundant questions

### 1. Intake, decisions and authorization (the only routine human approval phase)

Understand the user's image-template goal, audience/use case, intended result, format, composition, style, subject or brand, exact text, aspect ratio, any supplied reference, must-preserve features and exclusions. For an editing task, identify an approved reference image. Determine whether this work should be a NEW distinct template or an update to a named draft. Agree on number of prompts: work **one template at a time**, even when a batch is requested. Set **native ChatGPT image generation as the first-choice generator**. At Intake, agree on whether fallback to a different generator is prohibited or may be proposed if the native generator fails. Never treat approval of native generation as authorization to use a different provider. If native generation is unavailable, rate-limited, quota-exhausted or returns an access/usage error, stop image production and obtain explicit user permission naming the proposed alternative before invoking it. Clarify whether the request authorizes saving a draft, **public publication**, or only preview. Establish what to do if a generated image fails QA: the default is **stop**, not hidden retries. Ask necessary questions now, not between routine execution steps. Do not ask a long interview when details are sufficient; a supplied complete prompt is an accepted creative brief.

If the request is exploratory, agree the final creative direction and canonical English prompt as part of Intake; display the literal canonical prompt for the user's review **during Intake**, not as a new, second approval step later. If the user already agrees or directs end-to-end generation, the agent may proceed. Lock the final text as `canonical_prompt`; do not edit it after image generation to rationalize the result.

### 2. Preflight and content planning (autonomous)

Call the real MCP `library_overview`, `list_prompts(status="all")`; use `get_prompt` for an existing matching record. Check categories, tags, supported formats, generators, allowed roles and unpublished drafts. Do not duplicate an existing slug. Check native image-generation capability first; a displayed generator name is not proof of a callable tool. Discover whether alternative generators exist only if necessary, but **do not invoke one without specific approval**. Select `type="image"`, `mode="text2image"` or `"img2image"`, permitted aspect ratio and category, meaningful search-intent title and unique slug. Plan the Spanish educational page and useful editable fields **before** generation, ensuring their default `value` is a literal substring of the English prompt. Avoid inventing generator names or promising rights/trademark clearance.

### 3. Generate one image per prompt, with mandatory native-first priority

**First choice: the host-native ChatGPT image generator (GPT Image).** For every distinct approved canonical English prompt, make **one generation request for exactly one image**; preserve the output as **one independently identifiable image attachment/file**. A user-requested batch of five prompts means five sequential prompt→image→QA→upload transactions, never a single call making a five-image contact sheet and never an image reused for different prompts. Do not combine prompts into one image, request multiple candidate variants, or re-run generation invisibly.

Invoke native image generation with the locked English canonical prompt as the sole intended visual instruction and the agreed reference image for `img2image`. Do not inject competing scene instructions or substitute a prior prompt. Some host-native interfaces infer input from the current conversation instead of accepting an explicit prompt parameter; report this limitation without claiming byte-for-byte internal forwarding is verified. Extract and retain **the actual generated file ID** and the generator identity for `add_image(file=...)`; do not invent IDs, copy an unrelated asset or use a search image. Host-native output may be visible in chat: never promise silent generation.

**Fallback decision rule:** If GPT Image is not callable, has exceeded quota or rate limits, is disabled, fails because of access restrictions, or otherwise cannot produce the approved image, **do not automatically switch** to an MCP generator, external image API, local program, another provider or a different model. Identify which available alternative, if any, can perform the same task; explain its real availability, cost/quotas if known and meaningful differences; request **explicit new permission for that named generator**. Only then continue with that generator, keeping the original prompt and labeling `model`/`generator` truthfully. No consent or no viable alternative means stop with an accurately reported blocker. Do not describe a tool as available until verified.

If a call returns an uncertain outcome or times out, inspect its reported state/attachment before any retry. A wrong generated image is a visual QA failure, not an excuse to switch generators. A further generation or an additional image is a new attempt that requires the user's instruction or an explicit retry policy agreed during Intake. One original result remains one file and one gallery upload; an `img2image` **input** is a separate required source file, not an additional generated output.

### 4. Visual quality gate (autonomous)

Inspect the actual image against the canonical prompt using `references/visual-qa.md`: desired object/identity, wording and spelling, layout, aspect ratio, style, palette, count of outputs, prohibited elements, reference preservation, plausible physical details and educational representativeness. Classify blocker vs minor drift with evidence. If a hard constraint fails, do **not** publish, silently retry or rewrite the saved prompt to match the wrong image. Return a precise failure and request a new authorization for retry. If passed, continue to the final step automatically within the Intake authorization; do not ask for redundant visual approval unless the user explicitly required it.

### 5. Build and persist the complete Spanish page (autonomous)

Use `references/page-content-seo.md`. Create a real, reusable template rather than a bespoke image request only: user-facing title (Spanish, clear and searchable), concise summary, selected category, accurate mode help, aspect ratio, prompt **EXACTLY `canonical_prompt`**, generator attribution (`model`), 2–5 genuinely useful customizable `fields` each literal value present in prompt (examples 2–6 each), pedagogical `education` (what this solves, how it works, preparation, substitutions, tips, limitations, variations and verification), focused tags, SEO title (≤60 chars) and description (≤160 chars), access value expressly agreed or a sensible free default, and deliberate `noindex` state. Never claim tested compatibility with tools not used. Use `create_prompt` only for a NEW template; for a specified existing draft, read via `get_prompt`, then `update_prompt` only what is intended. Do not destroy published assets or modify another page without authorization.

Upload the exact resulting file with `add_image({prompt_id,role:"gallery",file:<actual file id>,generator:<actual generator>,alt:<truthful Spanish alt>})`. For `img2image`, also attach the actual approved source image using `role:"input"`; the input is not a second generated result. Default to one real result image, never a collage masquerading as a single example. More than one output is a separate Intake decision; gallery maximum is three.

### 6. Verify, publish and deliver (autonomous)

Fetch `get_prompt` after the upload and verify exact canonical prompt, mode, generator, source media role, correct gallery media ID, number of images, fields, Spanish educational content, category, tags, SEO data and `missing_to_publish=[]`. Correct metadata-only issues, preserving the locked prompt and actual image. If the request authorized publication and QA passed, call `publish_prompt({prompt_id,publish:true})` once, then `get_prompt` again to confirm `status="published"`, same attached image and zero missing requirements. If draft-only authorization, leave draft and report accurately; do not manufacture consent.

Respond in Spanish with exact record ID/status, public_url when returned, count/role of uploaded media, actual generator, prompt congruence and any known limitation. The MCP flag verifies database publication, not necessarily browser rendering, page indexing or trademark originality; distinguish those claims.

## Non-negotiable constraints

- Prompt language English; page title, summary, educational text, custom labels, alt and SEO Spanish.
- Native GPT Image first; one canonical prompt → one separate generated file → one gallery image. No unapproved provider switching, quota fallback or hidden retries.
- Source of truth: MCP re-reads; never invent a tool result, gallery URL or publication state.
- All routine decisions and permissions at Intake; autonomous completion if successful and authorized.
- No destructive action, content replacement, publication of an unapproved task, or scope expansion by implication.
- Do not use this image publication skill to create articles, administer taxonomies or claim video production.
