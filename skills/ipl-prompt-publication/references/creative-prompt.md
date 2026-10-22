# Reusable prompt-template design

Design for a real reader who will copy and adapt a prompt, not for a one-off commission. Specify exactly one visual artifact, subject, visual hierarchy, framing and aspect ratio, focal plane, optics and camera position for photographs, lighting source and direction, materials, environment and honest exclusions. Add only constraints that improve reproducibility.

## Text-to-image
Prepare a single canonical prompt. Keep brand names fictional when a sample needs branding. Preserve exact required typography and check it visually.

## Image-to-image demonstration
When the owner commissions a NEW public template without supplying a photo, design a generic, plausible fictional subject and use the host's native image generation tool to create **one plain input photograph**. Its separate source-asset instruction asks for a straightforward amateur or catalog photo with stable visible geometry, color and markings, not an already polished advertisement. Keep the actual file. Lock the reusable canonical **editing** prompt separately and apply it to that input. Visually QA both. If the owner asks to edit their own image, use only that image.

The source-asset prompt and the canonical template prompt are different artifacts with different purposes. Do not use example images from searches, another prompt's gallery or a mock before/after composite as evidence.

## Video
Write one canonical English prompt for one clip: subject, action and its timing, camera movement, framing, lighting, duration feel and what must not change. For img2video, describe what moves and what stays identical to the input image. The poster is a real frame of the published video, never a separately generated image.

## Customizable parts
Choose 2–5 parts that each control a different aspect (subject, background, light, style, format). They are not alternatives to each other: the reader picks one option in each. Each default is a literal span of the canonical prompt with 2–6 English replacement examples that keep the sentence grammatical. The result is only demonstrated for the original values, not for every combination.
