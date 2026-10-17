"""Structure checks for the dojo skill's content files."""
import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent / "dojo"

REQUIRED_REFERENCES = [
    "principles.md", "tensions.md", "sources.md", "design.md", "audit.md",
    "lens.md", "coach.md", "cards.md", "woodpecker.md",
]


def read(rel: str) -> str:
    return (SKILL_DIR / rel).read_text(encoding="utf-8")


def test_reference_files_exist():
    missing = [r for r in REQUIRED_REFERENCES if not (SKILL_DIR / "references" / r).is_file()]
    assert not missing, missing


def test_skill_md_exists():
    assert (SKILL_DIR / "SKILL.md").is_file()
