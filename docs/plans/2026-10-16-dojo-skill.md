# Dojo Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and install `dojo`, a Claude skill that applies James's pedagogy in four modes (design, audit, lens, coach), with card and Woodpecker tooling. Publish it to GitHub.

**Architecture:**
- A short `SKILL.md` routes to mode-specific reference files, which share one philosophy core (`principles.md`, `tensions.md`, `sources.md`).
- Two small Python scripts handle cards:
  - `cards_csv.py` parses, validates and writes CSV that matches `study.html`'s parser.
  - `csv_to_apkg.py` builds Anki packages.
- Pytest checks both the scripts and the structure of the content files.

**Tech Stack:** Markdown, Python 3.10, pytest, genanki, git, gh.

**Spec:** `docs/specs/2026-10-16-dojo-skill-design.md` (copied into the repo in Task 1). Read it first; §-references below point into it.

## Global Constraints

- **Skill:** name `dojo`; folder `dojo/` in the repo; `SKILL.md` under 200 lines.
- **Repo and install:**
  - Repo at `C:\Users\James\Documents\Dojo\`.
  - Installed by a directory junction `C:\Users\James\.claude\skills\dojo` → `C:\Users\James\Documents\Dojo\dojo`.
- **Card CSV:**
  - UTF-8 without a BOM, exactly 2 columns (front, back), no header row.
  - RFC 4180 quoting for any field containing a comma, quote or newline.
  - `**bold**` and newlines allowed in fields.
  - The first row must not have a front containing "question" *and* a back containing "answer" (case-insensitive).
- **Lens opt-in line, exact text:** `Dojo lens: on. Check learning-facing features against the dojo skill.`
- **Coach subject folders:** `C:\Users\James\Documents\Learning\<subject>\`.
- **Never triggers on ordinary questions;** no unprompted quizzes or offers.
- **Evidence levels used verbatim:** `established`, `practitioner`, `philosophy`, `hypothesis`.
- **Primary source voice is James's writing.** Where the books differ, his synthesis wins (§2).
- **Push to GitHub only after** James confirms the repo name and visibility.

## Review Focus

1. Non-ASCII card text (Spanish ñ, Japanese) must round-trip and be written as UTF-8 without a BOM. Pinned in Task 4.
2. Windows CRLF card files must parse the same as LF files. Pinned in Task 4.
3. Bold markers that span a line break must not render as bold, matching `study.html`'s regex `\*\*([^*\n]+)\*\*`. Pinned in Task 4.
4. Duplicate rows in a deck should produce a validation warning: `study.html` makes identical rows share one schedule, and Anki duplicates the note. Pinned in Task 4.
5. A file with no cards (empty, or only blank lines) should fail validation with "no cards". Pinned in Task 4.

---

### Task 1: Repo scaffold and structure tests

**Files:**
- Create: `C:\Users\James\Documents\Dojo\` (git repo), `docs/specs/2026-10-16-dojo-skill-design.md` and `docs/plans/2026-10-16-dojo-skill.md` (copied from the session folder), `.gitignore`, `requirements-dev.txt`, `tests/test_structure.py`, `dojo/references/.gitkeep`, `dojo/scripts/.gitkeep`

**Interfaces:**
- Produces: `tests/test_structure.py` with helpers `read(rel: str) -> str` (reads a file under `dojo/`) and `REQUIRED_REFERENCES = ["principles.md","tensions.md","sources.md","design.md","audit.md","lens.md","coach.md","cards.md","woodpecker.md"]`. Later tasks add their own test functions to this file.

- [ ] **Step 1:** `git init` the repo. Copy in the spec and this plan. Add `.gitignore` (`__pycache__/`, `.pytest_cache/`, `*.apkg`, `evals/workspace/`) and `requirements-dev.txt` (`pytest`, `genanki`).
- [ ] **Step 2:** `python -m pip install -r requirements-dev.txt`. Expected: both packages import.
- [ ] **Step 3:** Write `test_reference_files_exist` (each `REQUIRED_REFERENCES` file exists under `dojo/references/`) and `test_skill_md_exists` (`dojo/SKILL.md` exists).
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: FAIL (files missing). That's correct for now; later tasks turn these green.
- [ ] **Step 5:** Commit: `chore: scaffold dojo repo with spec, plan and structure tests`.

### Task 2: Philosophy core (`principles.md`, `tensions.md`, `sources.md`)

**Files:**
- Create: `dojo/references/principles.md`, `dojo/references/tensions.md`, `dojo/references/sources.md`
- Test: `tests/test_structure.py`

**Interfaces:**
- Produces:
  - Principle IDs `S1`–`S14` and `A1`–`A7` as level-3 headings in the form `### S8. Difficulty in the goldilocks zone`. Every later reference file cites principles by these IDs.
  - Tension IDs `T1`–`T10` as rows of `tensions.md`'s table.

- [ ] **Step 1: Write the failing tests**

```python
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
    import re
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
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k "principles or tensions or sources or evidence"`. Expected: FAIL.
- [ ] **Step 3: Write `principles.md`.**
  - Thesis (§3.1).
  - Arc (§3.2), with stages as bold lead-ins `**Map (explicit)**`, etc., plus the "great players make poor coaches" corollary.
  - Structure principles S1–S14 (§3.3) and attitude principles A1–A7 (§3.4), each with the six fields.
  - **Why** cites the source(s) by short name (James, Ultralearning, Archery, Flow, SRS, Woodpecker, Voltaic).
  - Use James's wording where he has a strong phrase: "a movement happening", "goldilocks zone", "goals you are in charge of", "observe, don't judge", "peace of mind".
  - Write it for an agent reader: direct, no filler.
  - Use `###` headings **only** for the 21 principles; use `##` and bold lead-ins for everything else, because the field test splits on `\n### `.
- [ ] **Step 4: Write `tensions.md`.** A table with columns `| ID | Tension | Resolution | In app design |` and rows T1–T10 in the spec order (§3.5). Use the resolution wording agreed in conversation; for example, T4 is "Schedule the inputs, not the outcomes."
- [ ] **Step 5: Write `sources.md`.**
  - One condensed section per source (§2): the core mentality in 5–10 bullets, then how it fits with James's synthesis.
  - Then an **Evidence corrections** section with the six corrections listed in §2.
  - Paraphrase only; no quotes over 15 words, except James's own text.
- [ ] **Step 6:** Run the Step 2 command. Expected: PASS.
- [ ] **Step 7:** Commit: `feat: dojo philosophy core (principles, tensions, sources)`.
- [ ] **Step 8: Review gate.** Send James the three files and **stop until he approves** or asks for edits (spec §9). Apply any edits, re-run the tests and commit before Task 3.

### Task 3: `SKILL.md` (routing and triggers)

**Files:**
- Create: `dojo/SKILL.md`
- Test: `tests/test_structure.py`

**Interfaces:**
- Consumes: the principle and tension IDs from Task 2, and the reference file names in `REQUIRED_REFERENCES`.

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k skill_`. Expected: FAIL.
- [ ] **Step 3: Write `SKILL.md`.**
  - Frontmatter `name: dojo`, with a one-line `description` that covers the auto-triggers and the non-trigger (§6).
  - Body:
    1. The thesis and a five-line arc summary.
    2. "Read first": `principles.md` for every mode.
    3. A mode-routing table: Design, Audit, Lens, Coach, Cards, Woodpecker/Benchmark. Each row names the trigger phrases and the reference file to load.
    4. Hard rules:
       - Respect recorded user decisions.
       - Never turn ordinary questions into lessons.
       - Judge methods conceptually against the learner's goal.
       - Tag claims with their evidence level.
- [ ] **Step 4:** Run the Step 2 command. Expected: PASS.
- [ ] **Step 5:** Commit: `feat: dojo SKILL.md routing and triggers`.

### Task 4: Card tooling (`cards_csv.py`, `csv_to_apkg.py`, `cards.md`)

**Files:**
- Create: `dojo/scripts/cards_csv.py`, `dojo/scripts/csv_to_apkg.py`, `dojo/references/cards.md`
- Test: `tests/test_cards_csv.py`, `tests/test_csv_to_apkg.py` (both put `dojo/scripts` on `sys.path`)

**Interfaces:**
- Produces:
  - `cards_csv.parse_csv(text: str) -> list[tuple[str, str]]`: a faithful port of `study.html`'s `parseCSV`. Copy its state machine as-is: it skips `\r`, trims fields, drops rows where both fields are empty, and skips the first row if its front matches /question/i and its back matches /answer/i.
  - `cards_csv.to_csv(rows: list[tuple[str, str]]) -> str`: the stdlib `csv` writer with `QUOTE_MINIMAL` and `lineterminator="\n"`.
  - `cards_csv.write_csv(rows, path) -> None`: UTF-8, no BOM.
  - `cards_csv.validate(text: str) -> list[str]`: a list of problems (empty means OK). CLI: `python cards_csv.py deck.csv` prints the problems and exits 1 if any, else prints `OK: N cards` and exits 0.
  - `csv_to_apkg.card_html(text: str) -> str`, `csv_to_apkg.stable_id(name: str) -> int`, and `csv_to_apkg.build_package(rows, deck_name: str, reverse: bool = False) -> genanki.Package`. CLI: `python csv_to_apkg.py deck.csv "Deck Name" [--reverse] [-o out.apkg]`. If genanki is missing, print `pip install genanki` and exit 2.

- [ ] **Step 1: Write the failing tests (`tests/test_cards_csv.py`)**

```python
def test_parse_quotes_commas_newlines():
    assert parse_csv('a,b\n"x, y","l1\nl2"\n') == [("a", "b"), ("x, y", "l1\nl2")]

def test_parse_escaped_quotes():
    assert parse_csv('"say ""hi""",b') == [('say "hi"', "b")]

def test_parse_crlf_matches_lf():
    assert parse_csv("a,b\r\nc,d\r\n") == parse_csv("a,b\nc,d\n") == [("a", "b"), ("c", "d")]

def test_parse_skips_headerish_first_row():
    assert parse_csv("Question,Answer\nq,a") == [("q", "a")]

def test_roundtrip_including_unicode_and_bold():
    rows = [("¿Qué es, ñ?", 'He said "hi"\n**bold**'), ("日本語", "a,b")]
    assert parse_csv(to_csv(rows)) == rows

def test_write_csv_utf8_no_bom(tmp_path):
    p = tmp_path / "d.csv"
    write_csv([("ñ", "x")], p)
    raw = p.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf") and "ñ".encode() in raw

def test_validate_flags_problems():
    assert any("header" in e for e in validate("Which question?,The answer\nq,a"))
    assert any("3 columns" in e for e in validate("a,b,c\n"))
    assert any("empty" in e for e in validate("a,\n"))
    assert any("duplicate" in e for e in validate("a,b\na,b\n"))
    assert validate("\n\n") == ["no cards"]
    assert validate("a,b\n") == []
```

- [ ] **Step 2: Write the failing tests (`tests/test_csv_to_apkg.py`)**

```python
def test_card_html():
    assert card_html("**hi** <b>\nx") == "<b>hi</b> &lt;b&gt;<br>x"
    assert card_html("**a\nb**") == "**a<br>b**"  # no bold across lines, like study.html

def test_stable_id():
    assert stable_id("Spanish") == stable_id("Spanish") != stable_id("French")
    assert (1 << 30) <= stable_id("Spanish") < (1 << 31)

def test_build_package_writes_loadable_zip(tmp_path):
    import zipfile
    pkg = build_package([("q1", "a1"), ("q2", "a2")], "Test Deck", reverse=True)
    out = tmp_path / "t.apkg"
    pkg.write_to_file(out)
    assert zipfile.is_zipfile(out)
    deck = pkg.decks[0]
    assert len(deck.notes) == 2 and len(deck.notes[0].model.templates) == 2
```

- [ ] **Step 3:** Run `python -m pytest tests/test_cards_csv.py tests/test_csv_to_apkg.py -q`. Expected: FAIL (import errors).
- [ ] **Step 4: Implement `cards_csv.py`.**
  - `validate` messages must contain these substrings:
    - `header`: row 1 would be skipped by `study.html`.
    - `N columns`: a row has other than 2 fields; detect this with a raw field count before trimming to 2.
    - `empty`: a front or back is empty.
    - `duplicate`: identical front and back as an earlier row.
    - `no cards`: the deck is empty.
  - Each message also includes the row number.
- [ ] **Step 5: Implement `csv_to_apkg.py`.**
  - `card_html`: HTML-escape first, then apply `\*\*([^*\n]+)\*\*` → `<b>\1</b>`, then turn newlines into `<br>`.
  - `stable_id`: the first 8 bytes of sha1(name) as an int, mapped into [2^30, 2^31).
  - Models: "Dojo Basic", or "Dojo Basic+Reversed" with two templates when `reverse=True`. Model IDs come from `stable_id("dojo-model-" + kind)`.
- [ ] **Step 6:** Run the Step 3 command. Expected: PASS.
- [ ] **Step 7: Write `cards.md`.**
  - The card-writing rules (§5.1).
  - The exact CSV format with the parser quirk.
  - The workflow:
    1. Understand the material.
    2. Write the cards.
    3. `write_csv`, then run `python scripts/cards_csv.py deck.csv` until it prints OK.
    4. Optionally `csv_to_apkg.py`.
  - Where decks go: the project's `cards/` folder for apps, and `Learning\<subject>\cards\` for coach mode.
  - Add `test_cards_md_documents_format` to `test_structure.py`, asserting `cards.md` contains `no header`, `cards_csv.py` and `csv_to_apkg.py`.
- [ ] **Step 8:** Run `python -m pytest tests -q -k "cards or apkg"`. Expected: PASS.
- [ ] **Step 9:** Commit: `feat: dojo card tooling (CSV for study.html, Anki .apkg)`.

### Task 5: Design and audit modes

**Files:**
- Create: `dojo/references/design.md`, `dojo/references/audit.md`
- Test: `tests/test_structure.py`

**Interfaces:**
- Consumes: principle IDs `S1`–`S14`, `A1`–`A7` and tension IDs `T1`–`T10`.

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k "design or audit"`. Expected: FAIL.
- [ ] **Step 3: Write `design.md`** (§4.1).
  - The five-step workflow.
  - A knowledge-type decision table with columns `| Kind | Methods | Arc stages | Anti-patterns |` and the six rows.
  - A loop-design checklist; the final step is "check against `tensions.md`".
  - A worked mini-example: Piaano's Pattern Trainer scheduler, applying S12 (chords are pattern-is-skill, so Woodpecker plus spacing) and T2.
- [ ] **Step 4: Write `audit.md`** (§4.2).
  - The four-step workflow, with "establish what the app is for; ask if it can't be inferred" first.
  - The ratings scale.
  - The report template, with the headings `## Goal`, `## Strengths`, `## Findings` (ranked: severity, principle, evidence `file:line`, why for this goal, fix), `## Tensions with recorded decisions` and `## Summary`.
  - Save path rule: `docs/dojo-audit-YYYY-MM-DD.md` for long audits.
  - A worked mini-example: `study.html`'s fixed 1–3 day intervals, judged *conditionally* on the deck's goal (S7, S13).
- [ ] **Step 5:** Run the Step 2 command. Expected: PASS.
- [ ] **Step 6:** Commit: `feat: dojo design and audit modes`.

### Task 6: Lens and coach modes

**Files:**
- Create: `dojo/references/lens.md`, `dojo/references/coach.md`
- Test: `tests/test_structure.py`

- [ ] **Step 1: Write the failing tests**

```python
LENS_LINE = "Dojo lens: on. Check learning-facing features against the dojo skill."

def test_lens_optin_and_six_questions():
    text = read("references/lens.md")
    assert LENS_LINE in text
    import re
    assert len(re.findall(r"^\d\. ", text, re.M)) == 6
    assert "never block" in text.lower()

def test_coach_files_and_session_flow():
    text = read("references/coach.md")
    for s in [r"Documents\Learning", "plan.md", "log.md", "cards/", "woodpecker/",
              "Session-only", "Long-running", "deadline"]:
        assert s in text, s
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k "lens or coach"`. Expected: FAIL.
- [ ] **Step 3: Write `lens.md`** (§4.3).
  - The opt-in line, verbatim.
  - The six numbered questions, each citing its principle IDs.
  - Output rule: only real concerns, at most about 5 lines, never block work, never re-argue recorded decisions.
- [ ] **Step 4: Write `coach.md`** (§4.4).
  - The session-only flow and the long-running flow.
  - Markdown templates for `plan.md` and `log.md` as fenced blocks.
  - The four-step session ritual.
  - The rule that progress is never measured against deadlines (S13, A1).
  - Debrief phrasing guidance for "observe, don't judge" (A3).
- [ ] **Step 5:** Run the Step 2 command. Expected: PASS.
- [ ] **Step 6:** Commit: `feat: dojo lens and coach modes`.

### Task 7: Woodpecker and benchmark builders

**Files:**
- Create: `dojo/references/woodpecker.md`
- Test: `tests/test_structure.py`

- [ ] **Step 1: Write the failing test**

```python
def test_woodpecker_rule_cycles_and_benchmark():
    text = read("references/woodpecker.md")
    for s in ["S12", "why", "halv", "set.md", "cycles.md", "Benchmark", "weekly", "worst day"]:
        assert s in text, s
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k woodpecker`. Expected: FAIL.
- [ ] **Step 3: Write `woodpecker.md`** (§5.3–5.4).
  - When to offer it by name (S12 test), with examples.
  - Set construction: problems plus full solutions; first-cycle difficulty "solvable with effort".
  - The cycle schedule, halving the time each cycle.
  - Templates for `set.md` and `cycles.md`.
  - The rule that every re-solve reproduces *why* the solution works.
  - A Benchmark section: a fixed low-noise set per category, a weekly cadence, averaging several runs, and recording worst day and spread.
- [ ] **Step 4:** Run the Step 2 command, then `python -m pytest tests -q` (the full suite). Expected: all PASS.
- [ ] **Step 5:** Commit: `feat: dojo woodpecker and benchmark builders`.

### Task 8: Install and behavioural evals

**Files:**
- Create: junction `C:\Users\James\.claude\skills\dojo` → `C:\Users\James\Documents\Dojo\dojo`; `evals/evals.json`; `evals/results.md`

- [ ] **Step 1: Install.** In PowerShell, run `New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\dojo" -Target "C:\Users\James\Documents\Dojo\dojo"`. Verify that `Test-Path "$env:USERPROFILE\.claude\skills\dojo\SKILL.md"` returns True.
- [ ] **Step 2: Write `evals/evals.json`** with the six prompts from spec §10, each with the expected behaviours as assertions.
- [ ] **Step 3: Run the evals** following the skill-creator workflow: a subagent per prompt, with the skill available. Grade each against its assertions. For eval 6, run `cards_csv.py` on the produced CSV.
- [ ] **Step 4:** Record the pass/fail results with notes in `evals/results.md`. Fix any failing behaviour in the relevant reference file, then re-run that eval.
- [ ] **Step 5:** Commit: `test: dojo behavioural evals`.

### Task 9: README and GitHub

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`.**
  - What Dojo is: the thesis and the four modes.
  - Install: the junction command, or copying `dojo/` into `~/.claude/skills/`.
  - Card tooling usage.
  - Running the tests.
  - Credits to the sources (§2).
- [ ] **Step 2:** Commit: `docs: README`.
- [ ] **Step 3: Confirm with James** the repo name (suggested `dojo`) and visibility. Then run `gh auth status`. Expected: logged in.
- [ ] **Step 4: Publish.** Run `gh repo create <name> --<visibility> --source . --push`. Verify that `git status -sb` shows the branch tracking `origin`.
