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

Para instalar en tu cuenta personal de ChatGPT, incluida Plus, descarga el paquete ya construido. No necesitas terminal y puedes hacerlo desde el teléfono.

1. [Descarga prompt-library-plugin.zip](https://github.com/jcd3dr/prompt-library-plugin/releases/latest/download/prompt-library-plugin.zip). También está en **Assets** de [Releases](https://github.com/jcd3dr/prompt-library-plugin/releases).
2. Guarda el archivo ZIP en Archivos o Descargas. Si el teléfono lo descomprime automáticamente, conserva o vuelve a descargar el ZIP original.
3. Abre ChatGPT.com, selecciona Plugin Creator y adjunta el ZIP desde el selector de archivos.
4. Solicita la instalación del plugin adjunto en tu cuenta; abre el enlace que devuelve Plugin Creator y completa la instalación y cualquier conexión o autenticación solicitada.
5. Abre un chat nuevo, selecciona Image Prompt Library y verifica la skill `ipl-prompt-publication` y las herramientas MCP con una operación de lectura.

Descarga el asset **`prompt-library-plugin.zip`**, no **Source code (zip)** ni **Code → Download ZIP**: esos archivos automáticos contienen el repositorio completo.

Para construirlo como desarrollador, ejecuta `python scripts/build_distribution.py` y después `python scripts/validate_distribution.py`. El resultado es `dist/prompt-library-plugin.zip`, con `plugin.json`, `mcp.json`, `server.json`, las skills y los iconos. El workflow de release construye y valida este mismo archivo antes de publicarlo. La instalación en la cuenta y la disponibilidad de sus funciones se comprueban en ChatGPT después de subir el ZIP.

El paquete declara su propio endpoint remoto. No contiene `.app.json`, IDs de conectores registrados ni depende de «Image Prompt Library MCP» creado previamente en una cuenta. 

Los metadatos de presentación van en `plugin.json` → `extensions.com.openai.interface`: `displayName`, `shortDescription`, `longDescription`, `logo` y `composerIcon`. La conexión va en `mcp.json` → `mcpServers.image-prompt-library`. El paquete contiene ambos componentes. La autenticación que solicite el host sigue siendo necesaria.

El catálogo Git no equivale a una instalación personal en ChatGPT web. La importación de marketplaces GitHub para equipos corresponde a administradores de espacios compatibles. No requiere publicar este plugin en el directorio público.

## Conexión y comprobación

Endpoint: `https://prompts.jcdcruz.com/mcp`, HTTP transmisible. Completa la autenticación que solicite el host; nunca agregues credenciales al repositorio. Comprueba descubrimiento de herramientas y una llamada de lectura antes de publicar. Una instalación correcta no demuestra que el servidor esté accesible ni autenticado.

## Mantenimiento

La fuente editorial vive en `skills/` y los manifiestos portables en la raíz. Ejecuta `python scripts/build_distribution.py` después de editarla: genera los adaptadores y el paquete de marketplace en `plugins/prompt-library-plugin/`. No edites esa copia generada directamente. Confirma ambos catálogos y la igualdad de las skills antes de publicar cambios.

Documentación oficial: [OpenAI](https://developers.openai.com/plugins/build/plugins), [Codex CLI](https://developers.openai.com/codex/cli/reference), [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).

## Validación del paquete de distribución

La construcción comprueba metadatos obligatorios, iconos incluidos y contenidos dentro del paquete, ausencia de dependencias por ID de app y transporte remoto. Los adaptadores Codex y Claude se derivan de `mcp.json`; no mantienen otra URL independiente. El ZIP incluye solo un plugin y excluye marketplaces, credenciales y conexiones de cuentas personales. La validación estática del paquete se realiza antes de cualquier instalación.

## Metadatos del servidor: server.json

`server.json` usa el esquema oficial del MCP Registry, versión 2025-12-11. Describe identidad, nombre visible, descripción, versión, sitio web, icono HTTPS y endpoint remoto. Se incluye en el repositorio, la copia de marketplace y el ZIP de distribución. La construcción exige que versión y endpoint coincidan con los manifiestos del plugin.

El formato procede de https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/generic-server-json.md. vidIQ utiliza el mismo formato en https://github.com/vid-io/vidiq-mcp/blob/main/server.json.

Añadir el archivo no publica el servidor en MCP Registry. Su uso documentado es metadatos de registro, descubrimiento y gestión de paquetes. La lectura de este archivo para la ficha de Apps de ChatGPT se mantiene como hipótesis de prueba, no como una garantía documentada por OpenAI. No sustituye `mcp.json` ni los metadatos del plugin.
