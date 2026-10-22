---
name: ipl-gallery-media
description: Improve the media of an Image Prompt Library prompt through the connected MCP - add results (up to 4), choose the cover, set labels, and fix "Generada con" captions and alt text, following the site's file policy.
---

# Image Prompt Library — Gallery and media

Every image on a prompt page is evidence. It must be a real execution of that exact prompt, shown with the tool that generated it.

## Add results (P5)

- A prompt holds up to **4** gallery results. Good reasons to add one:
  - The same prompt run in another tool, which shows how tools differ.
  - A second execution that shows natural variation.
  - The same prompt with a different option in one customizable part. Label it, for example "Fondo: ciudad de noche".
- Generate each result with the host's native generation tool by applying the published prompt exactly, or with a change in a single customizable part when the label says so.
- If the host has no native tool, tell the owner, list the alternatives you can actually use, and ask permission first.
- Never use search results, another prompt's images or composites.
- Visually inspect each result before uploading: right subject, no collage, no UI, no artifacts.
- Upload with `add_image(role:"gallery", file|url, generator, alt, label?)`:
  - `generator` is the tool that actually generated that file. The page shows it as "Generada con…".
  - `alt` is descriptive Spanish.
  - `label` is optional, at most 60 characters, and is shown over the image.

## Cover and order

The first gallery image is the cover on cards and the main image on the page. Use `reorder_gallery` with the full list of IDs to change it. Choose the cover that best shows what the reader will get.

## Fix captions, labels and alt text

Use `update_image(image_id, generator?, alt?, label?)`. It changes metadata only.

- If a caption names the wrong tool and you cannot confirm the right one, ask the owner.
- Never guess a generator.

## Inputs, posters and video

- Uploading `input`, `poster` or `video` replaces the previous file of that role.
- The input of an img2* prompt is the exact image the result was made from. Never swap it for a nicer one.
- The poster is a frame of the published video.

## File policy

- Static images are stored as WebP: 1600 px plus a 640 px thumbnail.
- For animation, prefer animated WebP or a short MP4/WebM loop over GIF, because GIF is much heavier. Animated WebP, GIF, AVIF and SVG are stored as they are.
- Removing media with `delete_image` deletes its file.
- Files left unreferenced, such as inline blog images removed from a body, are collected by the cleanup in the maintenance workflow.

## Boundaries

- `delete_image` can make a published prompt incomplete. Use it only on an explicit request, and say what the page loses.
- Re-read with `get_prompt` after every change. In clients with the in-chat view, that shows the owner the updated card.
