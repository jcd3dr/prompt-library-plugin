---
name: ipl-prompt-customization
description: Design or fix the customizable parts of an Image Prompt Library prompt and their examples through the connected MCP, so readers can adapt the prompt on the page and copy it already personalized.
---

# Image Prompt Library — Customizable parts

On every prompt page the reader chooses an option for each highlighted part of the prompt. The prompt updates live, and "Copiar prompt" copies the personalized version. Each part controls a **different aspect** (subject, background, light, style, format, mood). The parts are not alternatives to each other: the reader combines one choice from each.

## Design the parts (P7)

1. Read the prompt with `get_prompt`. Identify 2–5 spans that a reader would plausibly change and that change the result in a visible, predictable way. Skip fragments that carry the technique: those are what makes the prompt work.
2. Each part (`fields[]` item) has:
   - `label`: Spanish name of the aspect ("Sujeto", "Fondo", "Luz").
   - `value`: the exact span as it appears in the prompt. It must occur literally, and only once if possible.
   - `examples`: 2–6 English replacements.
3. Write examples that:
   - Read grammatically when swapped into the sentence. Check that the article, number and preposition still fit.
   - Keep the technique intact, for example by not changing a portrait into a landscape.
   - Cover different everyday uses: personal, selling, social media.
   - Stay safe, with no real brands or people.
4. Test mentally by substituting every example into the full prompt and reading the whole sentence. Fix any example that breaks it.
5. Save with `update_prompt(fields=[…])`. The list is replaced whole, so send every field. The server rejects a `value` that does not appear in the prompt.

## Fix existing parts

The most common change request is better examples, not a new prompt. Improve labels and examples freely: they do not change the prompt text, so the media stays valid.

Changing which spans are customizable is also safe, as long as each `value` still appears literally in the prompt.

## What the results prove

The results only demonstrate the original values. Add a result that uses a different option only through the gallery workflow, labeled with the option it used.

## Show and report

Finish with `get_prompt`. In clients with the in-chat view, the owner can try the personalizer in the card. Report the final parts and anything you could not verify.
