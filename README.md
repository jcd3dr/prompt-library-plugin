# Image Prompt Library Plugin

Editorial and content operations plugin for [Image Prompt Library](https://prompts.jcdcruz.com), a public library where readers discover, learn, customize and reuse AI prompts.

- `plugin.json`: portable Agent Plugins 1.0 manifest and public identity.
- `mcp.json`: remote Image Prompt Library MCP at `https://prompts.jcdcruz.com/mcp` (streamable HTTP; authentication must be configured in the target runtime where required).
- `skills/ipl-prompt-publication/SKILL.md`: the **single authoritative image-template publication skill**, with supporting references for visual design, QA, educational Spanish metadata and MCP operation.

When publishing a newly designed img2image template, the skill builds its own fictional input fixture when no user image was commissioned, then generates and validates the result from the locked reusable prompt. Native GPT Image takes priority. A separate source fixture is not a second gallery variant.

The plugin's broader purpose is website content management; the publication skill handles the image-prompt publication workflow specifically. Other site operations should use the actual connected MCP capabilities with appropriate task scope and approval. The separate `DadeCore Visual Prompt Publisher` ChatGPT plugin is superseded by this repository skill.

## Setup

Install the repository plugin using a compatible Agent Plugins host. Confirm the remote MCP transport and host-side authentication. The presence of `mcp.json` does not automatically authenticate a service or establish that it is reachable. Validate actual MCP tools from the host after installation.

Reference: https://developers.openai.com/plugins/build/plugins
