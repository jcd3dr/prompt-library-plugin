# Complete Image Prompt Library page: editorial, educational and SEO quality

## Reader value and publication contract
The page should teach a non-expert how to reproduce the real example, not merely dump a prompt. Check every component for honesty, clarity, utility and alignment with the demonstrated image.

- **Title (Spanish):** name the deliverable and distinctive result, in words readers would search; avoid fake rankings, clickbait and redundant product names. Different templates need distinct intent, not near-duplicate SEO headings.
- **Summary (Spanish):** 1–2 specific sentences explaining what the prompt produces and for whom. Do not promise automatic perfection or unsupported model portability.
- **Mode help (Spanish; minimum 10 chars):** explain exactly what input the user supplies, what changes and how to run text-to-image vs image-to-image; for edits, specify the required reference.
- **Category:** use an existing appropriate category from `library_overview` when possible; avoid creating a new category as a side effect without authorization.
- **Canonical prompt:** preserve original full English string byte-for-byte in MCP `prompt` field relative to the agreed record. Avoid changing it to fit generation failures.
- **Personalizable fields:** 2–5 (if meaningful), Spanish labels, each `value` a literal substring of the original prompt, with 2–6 realistic substitutions. Explain replacements will yield DIFFERENT results than the showcased original; do not present substitutions as tested unless truly tested.
- **Education (Spanish Markdown):** describe purpose and suitable audiences; basic technique behind the prompt (e.g., visual hierarchy, lens, composition, negative space); short copy/use instructions; customization examples; troubleshooting common generator errors; variations; limitations and honest rights/accessibility caveats relevant to the content.
- **Media:** exact generated example; truthful Spanish alt describing content, not keyword stuffing. Correct original source role for img2image, precise generator and actual readable media.
- **Tags:** 3–6 relevant taxonomy terms, prefer observed names in `library_overview`; omit misleading tags.
- **Metadata:** meta_title <= 60 Unicode characters, meta_description <= 160; precise summary with natural query terms, no keyword stuffing. Unique descriptive slug using URL-safe lowercase words and hyphens; verify collision using list/get.
- **Indexing/access:** `noindex=false` only if public and useful; noindex or draft if the user requests private/incomplete material. Never select premium access without authorization; default free when appropriate.

## QA against thin/repetitive pages
Ask: Would this page still be useful to a person who knows nothing about the prompt? Is it differentiated from existing templates? Does the explanation match what the generated image demonstrably achieves? Are user-customizable values real stable spans? Is the page indexable without duplicating others? Are title and description accurate? Are factual assertions and licensing/trademark implications carefully limited?

Do not invent business contacts, dates, offers, product specs or legal ownership; avoid claims that a raster output is an editable vector. Do not manufacture external citations or claim a real product was tested on generators that were not used.
