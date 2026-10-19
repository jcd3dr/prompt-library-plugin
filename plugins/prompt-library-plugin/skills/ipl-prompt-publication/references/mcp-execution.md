# MCP execution and recovery

The repository-declared MCP server is `https://prompts.jcdcruz.com/mcp`. Prefer tools surfaced by the installed Image Prompt Library MCP; inspect current live schemas. The manifest configures transport and endpoint; it does not itself prove authentication or runtime tool availability.

Sequence: `library_overview` → `list_prompts(status="all")` → matching `get_prompt` if any → choose mode, unique slug and exact canonical prompt → (for a new img2image fixture) generate and visually inspect ONE native GPT Image input file with its distinct source-asset instruction → execute the canonical editing prompt ONCE with that fixture → visually QA the result → `create_prompt` new / `update_prompt` matching draft → `add_image(role:"input",file:<real fixture id>)` for img2image → `add_image(role:"gallery",file:<real result id>,generator:"ChatGPT (GPT Image)")` → `get_prompt` → `publish_prompt(publish:true)` if authorized and QA passed → `get_prompt` confirmation.

Use exact returned IDs/URLs. Never substitute an external image, URL or another generator without explicit user authorization. Prefer native file IDs; if the host cannot pass them to add_image, stop accurately. A user-approved source photo is not to be regenerated.

Before write, check for matching slug/draft. For uncertain upload, re-read the record before retrying upload; for uncertain publication, re-read status before re-publishing. Hard visual failure blocks publication and any automatic regeneration. Metadata-only corrections may be updated without regenerating. Check `missing_to_publish=[]`, exact canonical text, fields, model, role assignments, correct distinct files, and returned status. Do not claim browser rendering or indexing without a separate verified inspection.
