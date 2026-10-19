# Crafting professional reusable image prompts

## Goal
Produce one portable, accurate, reusable English visual specification that guides an image model to create a particular useful deliverable, not a poster displaying the prompt, UI screenshot, contact sheet or tutorial illustration about how prompts work.

## Design procedure
1. State intended artifact and use (e.g., restaurant promotion flyer, clean hero product image, luxury monogram logo), required subject, target audience and focal hierarchy.
2. Specify composition and framing: foreground/background, subject placement, negative space, readable hierarchy, intended crop, aspect ratio and camera perspective where relevant.
3. Select coherent visual language: graphic vs photographic, materials/textures, color harmony, typography, contrast, lens/angle and lighting. Not every photographic constraint belongs in a vector-style logo.
4. Explicitly include exact required text, the brand/product identity, other non-negotiables, count (ONE composition) and realistic restrictions. Avoid competing aesthetics or unnecessary verbosity.
5. For an edit (`img2image`), state what may change and what must remain recognizable from the approved input (e.g., product shape/branding), recognizing model limits.
6. Design 2–5 meaningful variable spans. Each field default must appear VERBATIM in canonical prompt, and each has 2–6 plausible substitution examples; substitutions should not break grammar.
7. Test internal coherence: every variable, aspect ratio, style, text and negative constraint points to the same intended output.

## Domain-specific checks
- Logos: spelling, recognizability at small size, flat vs dimensional art, typography, negative space, no invented trademarks clearance. Vector-*style* raster does not equal editable SVG.
- Flyers/posters: event/business purpose, concise hierarchy, offer/CTA only if supplied, legible exact text, adequate whitespace, typography and brand identity; do not invent prices, dates or contact details.
- Product photography: product accurately depicted, packaging/markings preserved when referenced, scale, believable reflections, shadow/contact and intentional background.
- Portraits: identity preservation where editing, appropriate clothing and framing, consistent anatomy, no invented identity claims.
- Infographics: defined educational objective, accurate facts, correct labels, legibility; avoid cramming an encyclopedia into one image.
- Thumbnails/social: hierarchy and focal contrast that survive reduction, platform crop, exact headline and one clear story.

Do not over-specify irrelevant camera settings, quality buzzwords or redundant negatives. Use a brief natural prompt if it is sufficient; use detail only where each constraint improves testability.
