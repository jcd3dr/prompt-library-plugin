"""Inspect the built plugin ZIP before attaching it to a GitHub release."""
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
archive = ROOT / "dist" / "prompt-library-plugin.zip"
source_manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
prefix = source_manifest["name"] + "/"

with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None, "Corrupt ZIP member"
    names = bundle.namelist()
    assert len(names) == len(set(names)), "Duplicate ZIP members"
    assert all(n.startswith(prefix) for n in names), "Expected exactly one plugin directory"
    assert all(".." not in PurePosixPath(n).parts for n in names), "Unsafe archive path"
    expected = set()
    for entry in ("plugin.json", "mcp.json", "server.json", "skills", "assets"):
        source = ROOT / entry
        for path in ([source] if source.is_file() else source.rglob("*")):
            if path.is_file():
                member = prefix + path.relative_to(ROOT).as_posix()
                expected.add(member)
                assert bundle.read(member) == path.read_bytes(), f"Stale archive member: {member}"
    assert set(names) == expected, "Unexpected or missing package files"
    manifest = json.loads(bundle.read(prefix + "plugin.json"))
    assert manifest == source_manifest
    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Expected release SemVer"
    extension = manifest["extensions"]["com.openai"]
    assert extension.get("requires_local_executor") is False, "Explicit cloud execution support required"
    assert not extension.get("hooks"), "Desktop lifecycle hooks are not web compatible"
    assert not extension.get("apps"), "Private app dependency in standalone ZIP"
    interface = extension["interface"]
    assert 0 < len(interface["shortDescription"]) <= 30
    for key in ("logo", "composerIcon"):
        member = prefix + interface[key].removeprefix("./")
        assert member in names, f"Missing icon: {member}"
    mcp = json.loads(bundle.read(prefix + "mcp.json"))
    assert mcp["$schema"] == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
    assert mcp["mcpServers"], "No MCP server packaged"
    for server in mcp["mcpServers"].values():
        assert server["type"] == "streamable-http"
        assert server["url"].startswith("https://")
    skills = [n for n in names if n.startswith(prefix + "skills/") and n.endswith("/SKILL.md")]
    assert skills, "No skill packaged"
    for member in skills:
        text = bundle.read(member).decode("utf-8")
        assert text.startswith("---\n"), "Missing skill frontmatter"
        header = text.split("---\n", 2)[1]
        skill_name = PurePosixPath(member).parent.name
        assert f"name: {skill_name}\n" in header
        assert re.search(r"^description: .+", header, re.MULTILINE)
        for reference in re.findall(r"`(references/[^`]+\.md)`", text):
            assert str(PurePosixPath(member).parent / reference) in names, reference
print(f"Validated {archive.name}: {manifest['version']}, {len(names)} files, {len(skills)} skill(s)")

