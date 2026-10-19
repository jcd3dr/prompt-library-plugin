# Image Prompt Library Plugin

Editorial and content operations plugin for [Image Prompt Library](https://prompts.jcdcruz.com), a public library where readers discover, learn, customize and reuse AI prompts.

- `plugin.json`: portable Agent Plugins 1.0 manifest and public identity.
- `mcp.json`: remote Image Prompt Library MCP at `https://prompts.jcdcruz.com/mcp` (streamable HTTP; authentication must be configured in the target runtime where required).
- `skills/ipl-prompt-publication/SKILL.md`: the **single authoritative image-template publication skill**, with supporting references for visual design, QA, educational Spanish metadata and MCP operation.

When publishing a newly designed img2image template, the skill builds its own fictional input fixture when no user image was commissioned, then generates and validates the result from the locked reusable prompt. Native GPT Image takes priority. A separate source fixture is not a second gallery variant.

The plugin's broader purpose is website content management; the publication skill handles the image-prompt publication workflow specifically. Other site operations should use the actual connected MCP capabilities with appropriate task scope and approval. The separate `DadeCore Visual Prompt Publisher` ChatGPT plugin is superseded by this repository skill.

## Instalación en ChatGPT.com desde un ZIP

Para una instalación personal en ChatGPT, incluida una cuenta Plus, descarga el paquete preparado del release:

**[Descargar prompt-library-plugin.zip](https://github.com/jcd3dr/prompt-library-plugin/releases/latest/download/prompt-library-plugin.zip)** · [Ver releases](https://github.com/jcd3dr/prompt-library-plugin/releases)

1. Desde tu teléfono o computadora, descarga `prompt-library-plugin.zip` en Archivos o Descargas. Si el navegador lo descomprime automáticamente, conserva o vuelve a descargar el ZIP original.
2. Abre ChatGPT.com, selecciona Plugin Creator y adjunta el archivo ZIP desde Archivos o Descargas.
3. Pide a Plugin Creator que instale el plugin del archivo adjunto en tu cuenta. Abre el enlace que devuelva y completa la instalación y la conexión MCP cuando se soliciten.
4. Inicia un chat nuevo, selecciona Image Prompt Library y comprueba que aparecen la skill `ipl-prompt-publication` y las herramientas del MCP antes de publicar contenido.

Usa el archivo **`prompt-library-plugin.zip` de Assets** del release. Los archivos automáticos **Source code (zip)** y **Code → Download ZIP** contienen el repositorio completo y no son el paquete preparado para instalar.

El ZIP incluye el manifiesto portable, el endpoint MCP, la skill con sus referencias y los iconos. No depende de IDs de apps privadas de otra cuenta. La creación del plugin y la conexión al servicio son pasos distintos; la disponibilidad final depende de las funciones y permisos de la cuenta.

### Codex CLI y Claude Code

Consulta [INSTALL.md](INSTALL.md) para instalar mediante marketplace en estos clientes y para los detalles de la instalación por ZIP en ChatGPT.

Marketplace: `dadecore-prompt-library`. Plugin: `prompt-library-plugin`.

Install the repository plugin using a compatible Agent Plugins host. Confirm the remote MCP transport and host-side authentication. The presence of `mcp.json` does not automatically authenticate a service or establish that it is reachable. Validate actual MCP tools from the host after installation.

Reference: https://developers.openai.com/plugins/build/plugins
