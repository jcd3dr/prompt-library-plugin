# MCP choreography and recovery: publishing one image prompt

## Use connected schemas, not imagined tool calls
Inspect `library_overview`, `list_prompts({status:"all"})` and, where relevant, `get_prompt({prompt_id})` before any write. The MCP handles title/category/tags, media and publication. Categories/modes may change; the MCP's live response is authoritative.

## Canonical operational sequence
1. Complete user Intake: content, generator, approval scope and full English canonical prompt. No separate approval gate later for routine stages.
2. Preflight: `library_overview`, `list_prompts`, `get_prompt` for matching slug/draft. Distinguish a distinct requested variant from accidental duplicate.
3. Prepare metadata and validate that each `fields[].value` appears literally in canonical prompt.
4. Use native ChatGPT GPT Image FIRST, exactly once per distinct canonical prompt, producing exactly one separate image file. Check whether it is actually callable. If unavailable, quota-/rate-limited or blocked, STOP and request explicit authorization for a **named, verified** alternative generator; never fall back automatically. If approved, use that provider and correctly attribute `model` and `generator`. Capture exactly one actual result file ID (some hosts show results in chat).
5. Run visual QA; block entire publication workflow on hard mismatch and ask before retry. For img2image, preserve actual approved reference file ID for role=input.
6. For new page, `create_prompt({title,slug,summary,type:"image",mode,mode_help,category,aspect_ratio,prompt:canonical_prompt,model,education,access,tags,meta_title,meta_description,noindex,fields})`. Existing draft: `get_prompt` then `update_prompt` only intended fields; no silent overwrites. Creation starts as draft.
7. If `img2image`, `add_image({prompt_id,role:"input",file:<actual user-approved source>})`. Then `add_image({prompt_id,role:"gallery",file:<actual generated image attachment>,generator:<actual producer>,alt:<Spanish description>})`. Each call passes EXACTLY ONE source. Native ChatGPT uses `file`, not a fictitious sandbox URL; for a genuine public HTTPS image, `url` is an alternative. `base64`/`dataUrl` are CLI-oriented, not needed with ChatGPT attachment.
8. `get_prompt`: verify exact locked prompt, type/mode, fields, category, metadata, media roles, actual generator, gallery image and `missing_to_publish=[]`.
9. If publication pre-authorized: `publish_prompt({prompt_id,publish:true})`, followed by `get_prompt` to verify status published, gallery URL and no missing fields. If only draft authorized, leave draft.
10. Respond with grounded outcome and exact returned links, not a guess.

## Fixed constraints
- `type`: image; `mode`: `text2image` or `img2image`; ratios: `1:1`, `9:16`, `16:9`, `4:5`, `3:4`.
- `gallery`: 1 actual generated image by default, up to 3 allowed by MCP; `img2image` needs input separately. Video needs `video` + `poster` and is outside this skill.
- `mode_help` Spanish at least 10 characters, `meta_title` <=60, `meta_description` <=160, `fields[].examples` 2–6. Each `fields[].value` literal in `prompt`.
- `model` and image `generator` must label the producing generator truthfully. The MCP may display a model string found in its generator list.
- Do not conflate prompt exact text stored in record with unprovable internal forwarding by a host-native generator.

## Transactional recovery
- **Existing slug/draft:** `get_prompt` and resume; no new draft solely to bypass failure.
- **Native unavailable / quota exhausted / rate limited:** stop and ask permission before invoking any other generator; do not treat tool discovery as approval.
- **Generation failed/wrong image:** stop; never invent new prompts/media, change providers or retry image generation without user authorization or a previously approved retry policy.
- **Upload uncertainty:** `get_prompt` first to check gallery before another `add_image`, avoiding duplicates.
- **Publication uncertainty:** `get_prompt` before another `publish_prompt`.
- **Metadata failure:** fix metadata and repeat `get_prompt` without regenerating. Do not update canonical prompt after generation merely to fit the result.
- **Missing input/output file:** block, report the missing artifact identity; no substitution.
- **No publish authorization:** draft only; no assumption that install of an MCP grants blanket public publishing rights.
- **Deleting or changing an existing published page:** not part of creating a new template; request targeted approval, inspect target first.
