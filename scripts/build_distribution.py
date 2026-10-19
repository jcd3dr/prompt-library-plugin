"""Build deterministic host adapters and marketplace payload from root source."""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")

def build():
    manifest = json.loads((ROOT / "plugin.json").read_text())
    name = manifest["name"]
    base = {k: manifest[k] for k in ("name", "version", "description", "author", "homepage", "repository", "keywords")}
    legacy = {"mcpServers": {"image-prompt-library": {"type": "http", "url": "https://prompts.jcdcruz.com/mcp"}}}
    write(ROOT / ".mcp.json", legacy)
    write(ROOT / ".codex-plugin/plugin.json", {**base, "skills": "./skills/", "mcpServers": "./.mcp.json", "interface": manifest["extensions"]["com.openai"]["interface"]})
    write(ROOT / ".claude-plugin/plugin.json", base)
    payload = ROOT / "plugins" / name
    if payload.exists():
        shutil.rmtree(payload)
    payload.mkdir(parents=True)
    for entry in ("plugin.json", "mcp.json", ".mcp.json", ".codex-plugin", ".claude-plugin", "skills", "assets"):
        source = ROOT / entry
        if source.is_dir():
            shutil.copytree(source, payload / entry, ignore=shutil.ignore_patterns("marketplace.json"))
        else:
            shutil.copy2(source, payload / entry)
    write(ROOT / ".agents/plugins/marketplace.json", {
        "name": "dadecore-prompt-library",
        "interface": {"displayName": "DadeCore Prompt Library"},
        "plugins": [{"name": name, "source": {"source": "local", "path": "./plugins/" + name},
                     "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"}]})
    write(ROOT / ".claude-plugin/marketplace.json", {
        "name": "dadecore-prompt-library", "owner": {"name": "DadeCore"},
        "plugins": [{"name": name, "source": "./plugins/" + name, "description": manifest["description"]}]})

if __name__ == "__main__":
    build()
    archive = ROOT / "dist" / "prompt-library-plugin.zip"
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for entry in ("plugin.json", "mcp.json", "skills", "assets"):
            source = ROOT / entry
            for path in ([source] if source.is_file() else sorted(source.rglob("*"))):
                if path.is_file():
                    bundle.write(path, Path("prompt-library-plugin") / path.relative_to(ROOT))
    print(archive)
