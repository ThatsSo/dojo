# Coach upgrades, progressive overload and deeper sources

Design spec, 2026-11-07. Status: awaiting review.

## Why

James's feedback from real use:
1. **Long-term planning drifted.** The coach started drilling his current knowledge and lost track of building the plan.
2. **Nothing was permanent.** The plan wasn't saved to a file, and nothing accounted for the conversation being compacted. Permanence matters for memory *and* for tracking progression.
3. **Exam prep lacked research.** For a specific exam, the coach guessed at what the questions might be instead of looking up the real ones.
4. **Short sessions had no end.** Acquire went on as if lessons were hours long, so in practice James lost focus before the material was done.
5. **The sources are thin:** about 5–10 bullets per book.
6. **Two new concepts:** progressive overload and chicken sexing.

Tools in use: ChatGPT for studying (with whatever file features his plan has), Claude for audits.

## 1. Long-term coaching gets a planning phase (fixes 1)

Long-running coaching has two phases, and the coach always shows which one it's in with a status line, for example `Planning, step 2 of 4: skill map`.

**Planning** (once, before any teaching):
1. **Goal and research:** the goal, deadline or exam date, and the research step (§3) when there's an external target.
2. **Skill map**, built from the research: categories and subcategories (S1), each with a progression ladder (§4).
3. **Placement check:** at most about 8 short items or 10 minutes, announced as a placement check. Its only purpose is to decide each skill's starting rung. Results go into the plan, not into a lesson, and the coach doesn't teach during it.
4. **Write the plan file (§2) and get approval.** The user approves the plan; then session 1 starts.

**Sessions:** see §4. The rule: if the coach notices it's teaching during Planning, it stops, notes the point for session 1, and goes back to the plan.

## 2. The plan file is the memory (fixes 2)

Long-running coaching is always file-backed. The file is the source of truth; the conversation is not.

**`plan.md`** sections, in this order:
1. **Resume here** (always first): current phase, skill and rung; what the next session does; reviews due; current weak points (top 3); last session date; session length.
2. **Goal:** what "done" looks like in the real context, the deadline or exam date, and why the learner wants it.
3. **Research:** for external targets, the blueprint summary with cited sources (§3).
4. **Skill map:** a table of category, subcategory, status (`not started` / `acquiring` / `automating` / `solid`) and the criterion for moving on.
5. **Progression ladders:** one per skill being acquired (§4).
6. **Weak points:** a table of item, when it was found, the evidence (what went wrong), the plan, and status. It feeds the bottleneck add-on (S3).
7. **Review schedule (spaced repetition):** a table of item, last reviewed, interval in days, next due, and result history.
   - Rule: correct → double the interval (1 → 2 → 4 → 8 → 16 → 32 days, then a 60-day maintenance cap); missed → back to 1 day and added to Weak points.
   - Items enter when they reach `automating`.
8. **Benchmark:** what is measured, how often, and the results (S11).
9. **Settings:** session length (default 25 minutes) and explanation depth (standard, deep or brief).

**`log.md`:** dated sessions, newest first: practised (yes/no, minutes), what was done, mistakes noticed, ladder movement, and the reviews done.

**The routine:** every session starts by reading `plan.md` (Resume here first) and the latest `log.md` entry. Every session ends by updating both, including rewriting Resume here. A fresh or compacted conversation must be able to continue from the files alone.

**Where the files live, by tool:**
- **Claude Code / Codex:** `<learning folder>/<subject>/` (existing `dojo_config.py`).
- **ChatGPT, or any tool with its own file storage** (project files, canvas, documents): keep `plan.md` and `log.md` there and update them in place each session.
- **Tools that can't store files:** at the end of each session, give the updated `plan.md` as a downloadable file, plus a short **state block** (Resume here, plus the reviews due) that the user pastes into the next conversation. Say plainly that this is what keeps the progress.

## 3. Research the target (fixes 3)

When the goal names an external target (an exam, certification, grade, syllabus, course, or a standard such as a CEFR level), research is a required Planning step:
- **Find official sources first**, then reputable secondary ones: the content outline and section weights, question formats, timing, scoring or pass mark, official sample or practice questions, recent changes, and recommended materials.
- **Cite every source** in the Research section with its date. Mark anything inferred rather than found.
- **Build the skill map from the blueprint:** weight practice time by section weight, and make Perform-stage practice match the real format (S2: practise in the real context; S11: benchmarks in exam conditions).
- **Ask the learner only for what can't be looked up:** their date, current level, materials, and constraints.
- **Without web access,** say so and ask the learner to paste the official outline instead of guessing.

## 4. Sessions are time-boxed, and Acquire follows a ladder (fixes 4)

**The session plan is shown up front:** the time box comes from Settings (default 25 minutes), split into blocks:
1. Reviews due (about 5 minutes).
2. Ladder work on the current skill (about 12).
3. Mixed application of the new material with older material (about 5).
4. Debrief and file update (about 3).

There's a one-line check-in at each block boundary. The session **stops on time**, even mid-rung. The rung is saved, and "next session starts here" goes into Resume here. Leaving a topic unfinished is fine, because spacing means you'll return to it fresh.

**Progression ladder (Acquire):** for each skill, list the variables that make it harder, each with a target range, and arrange them as rungs that add one step at a time (S10, the difficulty budget).
- *Example (intervals by ear):* interval size (2nds → octave), direction (ascending → descending → harmonic), register (middle → wide), tempo (slow → normal).
- **A rung is cleared** after `N` correct answers at that level: default `N = 2` for short answers, `N = 1` for long or worked answers. The learner can change `N`.
- **Two misses on a rung** step back one rung, or ease another variable, rather than grinding (S8).
- **Acquire for a skill ends** only when every variable has been cleared at its target range. Then the skill becomes `automating` and its key items enter the Review schedule. It never ends early on an accuracy streak at an easy rung.
- The ladder and its current rung live in `plan.md`, so a session can stop anywhere and resume on the exact rung.

**Session-only coaching** gets the same time box (default 25 minutes, or the learner's choice) and a mini-ladder of 2–4 rungs, so a one-off lesson also has a clear finish.

## 5. Deeper sources (fixes 5, approved)

- New folder `dojo/references/sources/` with one file per source:
  - `james.md`, `ultralearning.md`, `zen-archery.md`, `flow.md`, `spaced-repetition.md`, `woodpecker.md`, `voltaic.md`, `progressive-overload.md`, `chicken-sexing.md`.
  - Each covers: core idea, key techniques with specifics, examples, how it fits James's synthesis, which principles it supports (by ID), and caveats.
- `sources.md` stays the short index, plus the evidence corrections, and points to the per-source files. Dojo reads a per-source file only in deep mode or when a claim needs it, so everyday context stays light.
- **This round:** create the folder, a template, and full files for the two new sources. The other files start from the current summaries and are expanded when James sends write-ups. James's write-ups become the primary content, and anything I add is marked as mine.

## 6. New concepts (fixes 6)

- **Progressive overload** becomes a new structure principle, **S15**:
  - Raise the load in small, measured steps (one variable, around 5–10% or one rung at a time).
  - Track it so each step is deliberate.
  - Plan recovery: a lighter "deload" session or week after several steps up, or when fatigue shows.
  - Evidence: established in exercise science; practitioner as a learning analogy. It connects S8, S10, the Woodpecker halving and Voltaic's tiers, and it also drives the §4 ladder.
- **Chicken sexing** gets its own source file and a richer **S14**:
  - Expert sexers learned by sorting real chicks and getting immediate correction from a master, not from written rules.
  - Biederman & Shiffrar (1987) found that one explicit cue from an expert sharply improved novices.
  - For app design: high-volume classification with instant feedback, expert-labelled examples, and a few explicit cues.
- `tensions.md` gains no new row, but T1 and T8 mention progressive overload.

## Files touched

- **`dojo/references/coach.md`:** rewritten around §1, §2, §4.
- **New `dojo/references/research.md`** for §3, linked from SKILL.md and coach.md.
- **`dojo/references/principles.md`:** S15 added, S14 enriched.
- **`dojo/references/sources.md`** and the new `dojo/references/sources/` folder (with template).
- **`dojo/references/tensions.md`:** T1 and T8 wording.
- **`dojo/SKILL.md`:** routing row for research; mention of the planning phase; principle count updated to S1–S15.
- **`chatgpt/project-instructions.md`:** the coach permanence and research rules, kept under 8,000 characters.
- **Tests:** principle IDs up to S15; coach sections; research file; sources folder; package kit.

## Testing

- **Unit and structure tests** for each item above.
- **Behaviour evals,** blind, in Claude and in Codex:
  1. "Help me prepare for the [real exam] over the next 8 weeks" → researches with citations, keeps placement capped, writes the plan file with every §2 section, and doesn't drift into teaching during Planning.
  2. "25-minute session on [skill]" using an existing `plan.md` → shows the session plan, works the ladder from the saved rung, stops on time, and updates Resume here, the Weak points and the Review schedule.
  3. A fresh conversation given only the files continues the right rung (the compaction test).
  4. An ordinary question still doesn't trigger Dojo.
- **The ChatGPT kit** is rebuilt, and the Project instructions stay under 8,000 characters.
