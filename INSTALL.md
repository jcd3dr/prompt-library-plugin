# Instalación

## Codex CLI

En PowerShell o una terminal con Codex actualizado:

```sh
codex plugin marketplace add jcd3dr/prompt-library-plugin
codex plugin add prompt-library-plugin@dadecore-prompt-library
codex plugin list --json
```

Inicia una sesión nueva. Comprueba la skill `ipl-prompt-publication` y la conexión `image-prompt-library` antes de publicar.

## Claude Code

```sh
claude plugin marketplace add jcd3dr/prompt-library-plugin
claude plugin install prompt-library-plugin@dadecore-prompt-library
claude plugin list
```

Abre una sesión nueva y revisa `/mcp`. Invoca `/prompt-library-plugin:ipl-prompt-publication` para el flujo editorial. La generación depende de las herramientas reales del entorno: instalar el plugin no añade GPT Image a Claude Code. La skill requiere autorización explícita antes de cambiar de generador.

## ChatGPT web y móvil

La instalación personal se realiza guardando el paquete como plugin privado mediante Plugin Creator. Si ya existe «Image Prompt Library MCP», actualiza sus skills conservando su identidad y conexión; no crees otro MCP duplicado. Después abre el enlace del plugin y usa el botón de instalación si aún aparece disponible. Inicia un chat nuevo y selecciónalo con `@`.

El catálogo Git no equivale a una instalación personal en ChatGPT web. La importación de marketplaces GitHub para equipos corresponde a administradores de espacios compatibles. No requiere publicar este plugin en el directorio público.

## Conexión y comprobación

Endpoint: `https://prompts.jcdcruz.com/mcp`, HTTP transmisible. Completa la autenticación que solicite el host; nunca agregues credenciales al repositorio. Comprueba descubrimiento de herramientas y una llamada de lectura antes de publicar. Una instalación correcta no demuestra que el servidor esté accesible ni autenticado.

## Mantenimiento

La fuente editorial vive en `skills/` y los manifiestos portables en la raíz. Ejecuta `python scripts/build_distribution.py` después de editarla: genera los adaptadores y el paquete de marketplace en `plugins/prompt-library-plugin/`. No edites esa copia generada directamente. Confirma ambos catálogos y la igualdad de las skills antes de publicar cambios.

Documentación oficial: [OpenAI](https://developers.openai.com/plugins/build/plugins), [Codex CLI](https://developers.openai.com/codex/cli/reference), [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).
