# Image Prompt Library Plugin

Plugin para crear y publicar **plantillas de prompts de imágenes** en [Image Prompt Library](https://prompts.jcdcruz.com).

## Componentes

- `plugin.json`: manifiesto portable Agent Plugins 1.0.
- `skills/ipl-prompt-publication/SKILL.md`: flujo integral de publicación.
- `skills/ipl-prompt-publication/references/`: ingeniería de prompts, ejecución MCP, contenido/SEO y control visual.

## Dependencia MCP: pendiente de completar

La skill utiliza el servidor remoto *Image Prompt Library*, con herramientas como `library_overview`, `create_prompt`, `add_image`, `get_prompt` y `publish_prompt`.

**Falta confirmar la URL real del endpoint, su transporte y su autenticación.** El ID de una aplicación registrada en ChatGPT no proporciona esos datos. No se declara una URL ficticia ni se publican credenciales.

Una vez verificados, se debe añadir `mcp.json` con el esquema `https://agent-plugins.org/schemas/1.0.0/mcp.schema.json` y la entrada `mcpServers` correspondiente. **Hasta entonces, el paquete no instala automáticamente la conexión MCP.**

## Comportamiento de la skill

Brief y autorización inicial; prompt canónico en inglés; generación nativa ChatGPT como primera opción; **una imagen y archivo por prompt**; control de calidad visual; ficha educativa en español; SEO; carga real al MCP; verificación de publicación. Los generadores alternativos requieren permiso explícito.

No gestiona artículos, videos ni administración general del catálogo.

## Estado

- Skill y cuatro referencias conservadas de v2.1.1.
- Manifiesto portable e identidad corregidos.
- Pendiente: `mcp.json` con endpoint y autenticación verificados y prueba de instalación.

Documentación: https://developers.openai.com/plugins/build/plugins
