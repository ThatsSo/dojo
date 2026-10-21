import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def build(tmp_path):
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "package_chatgpt.py"), str(tmp_path)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    return tmp_path


def test_skill_zip_has_one_dojo_folder(tmp_path):
    out = build(tmp_path)
    names = zipfile.ZipFile(out / "dojo-skill.zip").namelist()
    assert {n.split("/")[0] for n in names} == {"dojo"}
    assert "dojo/SKILL.md" in names
    assert "dojo/references/principles.md" in names
    assert not any("__pycache__" in n or n.endswith(".pyc") for n in names)


def test_project_kit_fits_custom_gpt_limits(tmp_path):
    out = build(tmp_path)
    kit = out / "chatgpt-project"
    instructions = (kit / "instructions.md").read_text(encoding="utf-8")
    assert len(instructions) <= 8000
    knowledge = sorted(p.name for p in (kit / "knowledge").iterdir())
    assert "principles.md" in knowledge and "audit.md" in knowledge
    assert len(knowledge) <= 20
    for name in knowledge:
        assert name in instructions, name
