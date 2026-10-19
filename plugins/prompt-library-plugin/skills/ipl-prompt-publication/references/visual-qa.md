# Visual QA and publication blockers

Inspect the actual source/output files before any draft is published. Check correct subject and mode, single image (no UI, mockup, collage or prompt card), exact visible text and labels, stable identity, composition/crop/aspect, scene plausibility, lighting direction, contact shadows, material detail and sharpness.

For img2image, explicitly compare the input fixture with the final output. Verify characteristic product silhouette, colors, closures and marks, and disclose any visible drift. Do not claim pixel-identical conservation or sell fictional proof as evidence of a real product.

**Stop and do not publish** when the resulting file cannot be accessed or inspected, source identity is materially altered, branding/text is incorrect, the requested image type is wrong, prominent artifact is present, required input is absent, or an output belongs to another generation. QA cannot be replaced by `missing_to_publish=[]`.

For video, check the poster is a frame of that video, motion matches the prompt, no warping of faces, hands, text or product shape, and the clip loops or ends cleanly when the prompt says so. If the host cannot play the video, say so and ask the owner to confirm it before publishing.

Minor stylistic differences that preserve all hard requirements can be documented. Do not retry a failed image without fresh authorization. Do not rewrite the canonical prompt post hoc.
