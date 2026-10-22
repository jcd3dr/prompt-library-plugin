---
name: ipl-prompt-editing
description: Change an existing Image Prompt Library prompt through the connected MCP - improve its texts and SEO, audit prompts the owner wrote by hand, change the prompt itself, create a variant, or switch free/premium access.
---

# Image Prompt Library — Edit an existing prompt

The gallery must always be the real output of the published prompt. That single rule decides what can change freely and what needs new media. Public text is in Spanish, prompts and examples in English, the owner is addressed in their language.

## Start

`library_overview`, then find the prompt with `list_prompts(query=…)` and read it with `get_prompt`. Note `status`, `missing_to_publish`, categories, media roles and IDs, and `embedded_in`.

## Change the texts (P3)

Title, summary, `mode_help`, education, `prompt_es`, difficulty, SEO fields, tags and categories can change without touching the prompt or the media.

1. Change only what was asked, or what the audit below found.
2. `update_prompt` with only the changed fields. `fields`, `tags` and `categories` are replaced whole: send the complete list.
3. A save that breaks a server rule sends a published or scheduled prompt back to draft. Check `status` in the response and report it.

**Auditing a hand-made prompt.** When the owner wrote a prompt manually, review it as an editor:
- Is the prompt complete and reusable: subject, framing, light, materials, exclusions?
- Does it do what its result shows?
- Is the Spanish text clear for someone with no prompt knowledge?
- Are the customizable parts meaningful?
- Is the SEO within limits?

Report the findings in a short table and apply only what the owner approves. If the prompt text itself is weak, follow P4.

## Change the prompt itself (P4)

This is rare. Usually the better move is a new prompt (P6), and most change requests are really about the customizable examples, which do not affect the prompt text. If the prompt text must change:

1. Explain to the owner that the results must be regenerated, because they must be the real output of the new text.
2. Generate the new media with the host's native generation tool and QA it. If that cannot happen now, change nothing on a published prompt: propose a new draft prompt instead.
3. Replace the media and update `prompt`, `fields` (each default must still appear literally) and `prompt_es` together. Re-read with `get_prompt`.

## Create a variant (P6)

A variant reuses a prompt that works for a different goal (the same portrait in another style, the same product shot for another item). It is a new prompt with its own media, built from scratch like any new template. Link it to the original through shared categories and tags. Mention the original in its education when that helps the reader.

## Change access (P8)

Switch between `free` and `premium` only when the owner decides. There is no paywall yet: premium prompts show a locked teaser on the site. Use `update_prompt(access=…)` and report the change.

## Show and report

In clients with the in-chat view, finish with `get_prompt` so the owner sees the card. Then report only what changed, the status, and anything that needs their decision.

## Boundaries

Do not edit the prompt text of a prompt with media without regenerating the media. Do not delete media or prompts in this workflow.
