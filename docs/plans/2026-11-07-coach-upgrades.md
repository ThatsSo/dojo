# Coach Upgrades Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Dojo's coach mode plan, persist and pace long-term study properly. That means a planning phase, a file-backed plan with weak points and spaced repetition, exam research, time-boxed sessions with progression ladders, a new principle S15 (progressive overload), and per-source reference files.

**Architecture:** These are content changes to the skill's Markdown references. They're checked by structure tests in `tests/test_structure.py` and by blind behaviour evals.

**Tech Stack:** Markdown, Python 3.10, pytest, PyYAML.

**Spec:** `docs/specs/2026-11-07-coach-upgrades-design.md`

## Global Constraints

- Default session length: 25 minutes. Block split: reviews about 5, ladder about 12, mixed about 5, debrief about 3.
- Placement check: at most about 8 items or about 10 minutes.
- Rung cleared after `N` correct answers: `N = 2` for short answers, `N = 1` for long or worked answers; the user can adjust it. Two misses step back one rung.
- Review rule: correct doubles the interval (1 → 2 → 4 → 8 → 16 → 32 days, then a 60-day cap); missed resets to 1 day and adds a Weak points entry.
- Skill status values, exact: `not started`, `acquiring`, `automating`, `solid`.
- `plan.md` section headings, exact and in order: `## Resume here`, `## Goal`, `## Research`, `## Skill map`, `## Progression ladders`, `## Weak points`, `## Review schedule`, `## Benchmark`, `## Settings`.
- `SKILL.md` stays under 200 lines; frontmatter stays strict YAML.
- `chatgpt/project-instructions.md` stays at or under 8,000 characters.
- New principle heading, exact: `### S15. Progressive overload`, with all six fields; evidence tag `established`, with the learning-analogy caveat in parentheses.

## Review Focus

1. **A plan file from before this change** (old `plan.md` without the new sections): coach should add the missing sections on the next session, not break. Pinned in Task 2's coach text, checked by Task 6 eval 2.
2. **A subject with no external target** (e.g. "learn to juggle"): the research step must be skipped, not forced. Pinned in Task 3's `research.md` ("When to research").
3. **A session started with less time than planned** ("I've got 10 minutes"): the blocks scale down proportionally and reviews come first. Pinned in Task 2's coach text.
4. **Deep, brief and standard depth** still apply in coach mode: the setting is stored in `## Settings`. Pinned in Task 2.
5. **ChatGPT without file storage:** the state block must be self-sufficient. Pinned in Task 2's "Where the files live", checked in the Task 5 instructions test.

---

### Task 1: Principles (S15, S14) and tensions

**Files:** Modify `dojo/references/principles.md`, `dojo/references/tensions.md`, `dojo/SKILL.md`. Test: `tests/test_structure.py`.

**Interfaces:** Produces principle ID `S15`, which Tasks 2–4 cite.

- [ ] **Step 1: Update the failing tests.** In `test_principles_have_all_ids_and_fields`, `range(1, 15)` becomes `range(1, 16)`. In `test_evidence_levels_are_valid`, `len(levels) == 21` becomes `== 22`. Add:

```python
def test_s15_and_enriched_s14():
    text = read("references/principles.md")
    assert "### S15. Progressive overload" in text
    s15 = text.split("### S15.", 1)[1].split("\n### ", 1)[0]
    for s in ["deload", "small", "track"]:
        assert s in s15.lower(), s
    s14 = text.split("### S14.", 1)[1].split("\n### ", 1)[0]
    assert "Biederman" in s14 and "feedback" in s14
    t = read("references/tensions.md")
    assert t.count("progressive overload") >= 2
    assert "S1–S15" in read("SKILL.md")
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k "principles or evidence or s15"`. Expected: FAIL.
- [ ] **Step 3: Write S15** after S14 in `principles.md`, from spec §6. Add the chicken-sexing protocol and the one-explicit-cue finding to S14's **What it says** and **Why**. In `tensions.md`, add a "progressive overload" mention to T1 and T8. In `SKILL.md`, change "S1–S14" to "S1–S15" and "14 structure" to "15 structure".
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: all PASS.
- [ ] **Step 5:** Commit: `feat: S15 progressive overload, richer S14`.

### Task 2: Coach mode rewrite

**Files:** Rewrite `dojo/references/coach.md`. Test: `tests/test_structure.py` (`test_coach_files_and_session_flow` is replaced).

**Interfaces:** Consumes S15 and `research.md` (Task 3) by name.

- [ ] **Step 1: Write the failing test.** Replace `test_coach_files_and_session_flow` with:

```python
PLAN_SECTIONS = ["## Resume here", "## Goal", "## Research", "## Skill map",
                 "## Progression ladders", "## Weak points", "## Review schedule",
                 "## Benchmark", "## Settings"]

def test_coach_planning_persistence_and_sessions():
    text = read("references/coach.md")
    pos = [text.index(s) for s in PLAN_SECTIONS]   # template in order
    assert pos == sorted(pos)
    for s in ["Planning, step", "placement check", "research.md", "dojo_config.py",
              "DOJO_LEARNING_DIR", "~/.dojo.json", "log.md", "cards/", "woodpecker/",
              "Session-only", "Long-running", "deadline", "25 minutes", "stops on time",
              "rung", "N = 2", "60-day", "not started", "acquiring", "automating", "solid",
              "state block", "why this drill", "compact"]:
        assert s in text, s
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k coach`. Expected: FAIL.
- [ ] **Step 3: Rewrite `coach.md`** following spec §1, §2 and §4. Keep the existing learning-folder resolution, the debrief rules and the "why this drill" line. Add:
  - the `plan.md` template with the exact headings, in order;
  - the review rule;
  - the ladder rules;
  - the session block split, and scaling it when there's less time (Review Focus 3);
  - adding missing sections to an older plan file (Review Focus 1);
  - storing the depth setting in `## Settings` (Review Focus 4);
  - "where the files live", per tool, including the state-block contents (Review Focus 5);
  - the "notice you're teaching during Planning → park it" rule;
  - the compaction rule (the files are the memory).
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: all PASS.
- [ ] **Step 5:** Commit: `feat: coach planning phase, file-backed plan, ladders, time-boxed sessions`.

### Task 3: Research reference

**Files:** Create `dojo/references/research.md`. Modify `dojo/SKILL.md` (routing row) and `tests/test_structure.py` (`REQUIRED_REFERENCES` gains `research.md`).

- [ ] **Step 1: Write the failing test.** Add `"research.md"` to `REQUIRED_REFERENCES`, and add:

```python
def test_research_reference():
    text = read("references/research.md")
    for s in ["## When to research", "official", "weights", "format", "pass mark",
              "sample", "cite", "Without web access", "skill map"]:
        assert s in text, s
    assert "references/research.md" in read("SKILL.md")
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k "research or reference_files or links_every"`. Expected: FAIL.
- [ ] **Step 3: Write `research.md`** from spec §3. Include a "When to research" section that skips research for subjects with no external target (Review Focus 2), and a cited-Research-section template. Add a SKILL.md routing row: "Prepare for a specific exam, certification or syllabus → **Research** (inside Coach or Design) → `references/research.md`".
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: all PASS.
- [ ] **Step 5:** Commit: `feat: research step for external targets`.

### Task 4: Per-source files

**Files:** Create `dojo/references/sources/_template.md` and nine source files: `james.md`, `ultralearning.md`, `zen-archery.md`, `flow.md`, `spaced-repetition.md`, `woodpecker.md`, `voltaic.md`, `progressive-overload.md`, `chicken-sexing.md`. Modify `dojo/references/sources.md` (index plus links).

- [ ] **Step 1: Write the failing test.**

```python
SOURCE_FILES = ["james", "ultralearning", "zen-archery", "flow", "spaced-repetition",
                "woodpecker", "voltaic", "progressive-overload", "chicken-sexing"]
SOURCE_HEADINGS = ["## Core idea", "## Key techniques", "## Examples",
                   "## Fit with James's synthesis", "## Principles supported", "## Caveats"]

def test_source_files():
    index = read("references/sources.md")
    for name in SOURCE_FILES:
        text = read(f"references/sources/{name}.md")
        for h in SOURCE_HEADINGS:
            assert h in text, (name, h)
        assert f"sources/{name}.md" in index, name
    po = read("references/sources/progressive-overload.md")
    assert "deload" in po and "S15" in po
    cs = read("references/sources/chicken-sexing.md")
    assert "Biederman" in cs and "S14" in cs
```

- [ ] **Step 2:** Run `python -m pytest tests -q -k source_files`. Expected: FAIL.
- [ ] **Step 3: Write the files.**
  - `_template.md` holds the six headings.
  - The seven existing sources are seeded from the current `sources.md` summaries, each with a line under `## Core idea`: "Seed version; to be expanded from James's write-ups."
  - `progressive-overload.md` and `chicken-sexing.md` are full versions, written from spec §6 and marked as Claude-written, pending James's write-ups.
  - `sources.md` keeps its summaries and corrections and adds a "Deeper files" list linking each file, with the rule "read only in deep mode or when a claim needs it".
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: all PASS.
- [ ] **Step 5:** Commit: `feat: per-source reference files (+ progressive overload, chicken sexing)`.

### Task 5: ChatGPT instructions and kit

**Files:** Modify `chatgpt/project-instructions.md` and `tests/test_package.py`.

- [ ] **Step 1: Write the failing test.** Add to `test_project_kit_fits_custom_gpt_limits`: `for s in ["research.md", "plan.md", "Resume here", "state block", "25 minutes"]: assert s in instructions`. Add `"research.md"` to the knowledge-file checks.
- [ ] **Step 2:** Run `python -m pytest tests/test_package.py -q`. Expected: FAIL.
- [ ] **Step 3: Update the instructions.**
  - Add `research.md` to the knowledge list.
  - Add a "Long-term study" section: a planning phase; `plan.md` with Resume here kept in project files or canvas, updated every session, otherwise a downloadable file plus a state block; 25-minute sessions that stop on time.
  - Keep it at or under 8,000 characters.
  - The packager already copies every `references/*.md`. It doesn't copy `references/sources/`; add those as knowledge files only if the total stays at or under 20 (it will be 10 + 9 = 19).
- [ ] **Step 4:** Run `python -m pytest tests -q`. Expected: all PASS. Then run `python tools/package_chatgpt.py` and confirm `dist/chatgpt-project/knowledge` holds 19 files.
- [ ] **Step 5:** Commit: `feat: ChatGPT instructions for long-term study`.

### Task 6: Behaviour evals, then publish

**Files:** Modify `evals/results.md`.

- [ ] **Step 1: Run blind subagents in Claude.**
  - **Eval 1:** "Help me prepare for the CPA AUD exam over the next 8 weeks" with file access in `evals/workspace/aud/`, and `DOJO_LEARNING_DIR` pointed there by giving the subagent the path. Assert: web research with cited official sources (AICPA blueprint); placement capped; `plan.md` written with all nine sections in order; no teaching during Planning.
  - **Eval 2:** a fresh subagent given only the eval-1 files and "Start my 25-minute session". Assert: reads Resume here; shows the block plan; works from the saved rung; updates Resume here, Weak points, Review schedule and `log.md`.
  - **Eval 4:** an ordinary question doesn't trigger Dojo.
- [ ] **Step 2: Run eval 1 in Codex** with `codex.exe exec -s workspace-write -C evals/workspace/aud-codex`. Same assertions.
- [ ] **Step 3:** Record the results in `evals/results.md`. Fix any failing behaviour in the reference text, then re-run that eval.
- [ ] **Step 4: Final review** by a fresh reviewer subagent on the most capable model over `3c68c53..HEAD`. One fix pass for Critical and Important findings, each with a failing test first.
- [ ] **Step 5: Publish.** Run `git push origin main` and rebuild `dist/`.
