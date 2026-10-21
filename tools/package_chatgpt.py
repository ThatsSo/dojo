"""Build the ChatGPT versions of Dojo.

Usage: python tools/package_chatgpt.py [OUT_DIR]   (default: dist/)

Writes:
  dojo-skill.zip        the skill folder, for ChatGPT's Skills upload (one top-level `dojo/`)
  chatgpt-project/      instructions.md + knowledge/ files, for a ChatGPT Project or Custom GPT
"""
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "dojo"
SKIP = {"__pycache__"}


def skill_files():
    for p in sorted(SKILL.rglob("*")):
        if p.is_file() and not (SKIP & set(p.parts)) and p.suffix != ".pyc":
            yield p


def build(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out / "dojo-skill.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in skill_files():
            z.write(p, "dojo/" + p.relative_to(SKILL).as_posix())

    kit = out / "chatgpt-project"
    if kit.exists():
        shutil.rmtree(kit)
    (kit / "knowledge").mkdir(parents=True)
    shutil.copy(ROOT / "chatgpt" / "project-instructions.md", kit / "instructions.md")
    for ref in sorted((SKILL / "references").glob("*.md")):
        shutil.copy(ref, kit / "knowledge" / ref.name)


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    build(target)
    print(f"Wrote {target / 'dojo-skill.zip'} and {target / 'chatgpt-project'}")
