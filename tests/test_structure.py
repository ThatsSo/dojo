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


FIELDS = ["**What it says:**", "**Why:**", "**Signals present:**",
          "**Signals absent:**", "**Misapplications:**", "**Evidence:**"]


def test_principles_have_all_ids_and_fields():
    text = read("references/principles.md")
    ids = [f"S{i}" for i in range(1, 15)] + [f"A{i}" for i in range(1, 8)]
    for pid in ids:
        assert f"### {pid}. " in text, pid
    for block in text.split("\n### ")[1:]:
        for f in FIELDS:
            assert f in block, (block[:20], f)


def test_evidence_levels_are_valid():
    levels = re.findall(r"\*\*Evidence:\*\* (\w+)", read("references/principles.md"))
    assert len(levels) == 21
    assert set(levels) <= {"established", "practitioner", "philosophy", "hypothesis"}


def test_principles_has_thesis_and_arc():
    text = read("references/principles.md")
    assert "A rigorous plan, done with a Zen attitude" in text
    for stage in ["Map", "Acquire", "Automate", "Perform", "Review"]:
        assert f"**{stage}" in text


def test_tensions_table_has_ten_rows():
    text = read("references/tensions.md")
    for i in range(1, 11):
        assert f"| T{i} |" in text


def test_sources_lists_corrections():
    text = read("references/sources.md")
    for s in ["Biederman", "hypofrontality", "heuristic", "Herrigel", "VDIM", "anecdotal"]:
        assert s in text


def test_skill_frontmatter_and_triggers():
    text = read("SKILL.md")
    assert text.startswith("---\nname: dojo\ndescription: ")
    desc = text.split("description: ", 1)[1].split("\n", 1)[0].lower()
    for t in ["teach", "learn", "flashcard", "woodpecker", "audit", "dojo lens"]:
        assert t in desc, t
    assert "ordinary question" in desc  # states the non-trigger
    assert len(text.splitlines()) < 200


def test_skill_links_every_reference():
    text = read("SKILL.md")
    for ref in REQUIRED_REFERENCES:
        assert f"references/{ref}" in text, ref


def test_cards_md_documents_format():
    text = read("references/cards.md")
    for s in ["no header", "cards_csv.py", "csv_to_apkg.py"]:
        assert s in text, s


def test_design_has_workflow_and_knowledge_table():
    text = read("references/design.md")
    for kind in ["Fact", "Concept", "Procedure", "Perceptual pattern",
                 "Motor skill", "Strategic judgement"]:
        assert f"| {kind} |" in text, kind
    for s in ["learner's goal", "skill map", "learning zone", "performance zone",
              "benchmark", "difficulty budget", "tensions.md"]:
        assert s in text, s


def test_audit_has_ratings_template_and_decision_rule():
    text = read("references/audit.md")
    for r in ["Strong", "Partial", "Missing", "Conflicts", "N/A"]:
        assert r in text
    for s in ["what the app is for", "HANDOFF.md", "Tensions with recorded decisions",
              "docs/dojo-audit-", "Strengths", "file:line"]:
        assert s in text, s


LENS_LINE = "Dojo lens: on. Check learning-facing features against the dojo skill."


def test_lens_optin_and_six_questions():
    text = read("references/lens.md")
    assert LENS_LINE in text
    assert len(re.findall(r"^\d\. ", text, re.M)) == 6
    assert "never block" in text.lower()


def test_coach_files_and_session_flow():
    text = read("references/coach.md")
    for s in [r"Documents\Learning", "plan.md", "log.md", "cards/", "woodpecker/",
              "Session-only", "Long-running", "deadline"]:
        assert s in text, s


def test_woodpecker_rule_cycles_and_benchmark():
    text = read("references/woodpecker.md")
    for s in ["S12", "why", "halv", "set.md", "cycles.md", "Benchmark", "weekly", "worst day"]:
        assert s in text, s
