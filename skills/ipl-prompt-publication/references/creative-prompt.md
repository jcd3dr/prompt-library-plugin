# Reusable image-template design

Design for a real reader who will copy and adapt a prompt, not for a one-off commission. Specify exactly one visual artifact, subject, visual hierarchy, framing and aspect ratio, focal plane, optics/camera position for photographs, lighting source and direction, materials, environment and honest exclusions. Add only constraints that improve reproducibility.

## Text-to-image
Prepare a single canonical prompt for a single example image. Keep brand names fictional when a sample demands branding. Preserve exact required typography and check it visually.

## Image-to-image demonstration
When the user commissions a NEW public template without supplying a photo, autonomously design a generic, plausible fictional example product and use GPT Image to generate **one plain input photograph**. Its separate source-asset instruction should request a straightforward amateur or catalog photograph with stable visible geometry, color and markings, not an already polished advertisement. Capture the actual file ID. Lock the reusable canonical **editing** prompt separately and then execute it against that original image once. Require visual QA of both. If the user expressly requests editing their own image, use only that supplied image.

The source-asset prompt and the canonical template prompt are different artifacts with different purposes. One canonical prompt execution still produces exactly one gallery result. Do not use example images from searches, another prompt's gallery or a mock before/after composite as evidence.

## Customization
Use 2–5 meaningful changeable literal spans in the canonical English prompt. Each must have 2–6 replacement examples with valid grammar. The result is only demonstrably tested for the original values and supplied fixture, not every possible variation.
