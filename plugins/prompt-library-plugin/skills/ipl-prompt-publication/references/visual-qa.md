# Visual QA and publication blockers

Inspect the actual input and output files before anything is published. Check correct subject and mode, a single image (no UI, mockup, collage or prompt card), exact visible text and labels, stable identity, composition, crop and aspect ratio, scene plausibility, lighting direction, contact shadows, material detail and sharpness.

For img2image, explicitly compare the input with the result. Verify the characteristic silhouette, colors, closures and marks, and disclose any visible drift. Do not claim pixel-identical preservation or present fictional proof as evidence about a real product.

**Stop and do not publish** when a result cannot be accessed or inspected, source identity is materially altered, branding or text is wrong, the image type is wrong, a prominent artifact is present, a required input is missing, or an output belongs to another generation. `missing_to_publish=[]` does not replace QA.

For video, check that the poster is a frame of that video, motion matches the prompt, faces, hands, text and product shape do not warp, and the clip loops or ends cleanly when the prompt says so. If the host cannot play the video, say so and ask the owner to confirm it before publishing.

Minor stylistic differences that keep every hard requirement can be documented. Do not retry a failed generation without fresh permission. Do not rewrite the canonical prompt after the fact.
