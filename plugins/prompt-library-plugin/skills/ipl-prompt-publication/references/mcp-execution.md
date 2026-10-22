# MCP execution and recovery

The repository-declared MCP server is `https://prompts.jcdcruz.com/mcp`. Prefer tools surfaced by the installed Image Prompt Library MCP and inspect their live schemas. The manifest configures transport and endpoint; it does not prove authentication or runtime tool availability.

Image sequence: `library_overview` → `list_prompts(status="all", query=<topic>)` → matching `get_prompt` if any → choose mode, unique slug and exact canonical prompt → (img2image with no supplied photo) generate and inspect ONE fictional input with the native tool and its own source-asset instruction → apply the canonical prompt with the native tool → visual QA → `create_prompt` (new) or `update_prompt` (matching draft) → `add_image(role:"input", file:<input file>)` for img2image → `add_image(role:"gallery", file:<result file>, generator:"<tool that generated this file>", alt, label?)` for each result (max 4) → `get_prompt` → `publish_prompt(publish:true)` or `publish_prompt(publish:true, publish_at:<ISO date>)` if authorized and QA passed → confirm status.

Video sequence: `create_prompt(type:"video", mode:"text2video"|"img2video")` → `add_image(role:"input")` for img2video → `add_image(role:"video")` with the mp4/webm → `add_image(role:"poster")` with a frame of that video → same re-read and publish steps. Uploading input, poster or video replaces the previous file of that role.

Use exact returned IDs and URLs. Never substitute an external image, URL or another generator without the owner's permission. If the host cannot pass the generated file to `add_image`, keep the prompt as a draft and tell the owner (the media rule in SKILL.md). A user-supplied source photo is never regenerated.

Before writing, check for a matching slug or draft. After an uncertain upload, re-read the record before retrying; after an uncertain publication, re-read the status before publishing again. A hard visual failure blocks publication and any automatic regeneration. Check `missing_to_publish=[]`, exact canonical text, fields, model, role assignments, distinct files and the returned status. Do not claim browser rendering or indexing without a separate verified inspection.
