# Dojo: a pedagogy skill for Claude

Design spec, 2026-10-16. Status: awaiting review.

## 1. Purpose

Dojo encodes one coherent pedagogy, James's, and applies it in four ways:

1. **Design**: shaping new learning apps and features.
2. **Audit**: judging existing learning apps.
3. **Lens**: quietly checking feature work in projects that opt in.
4. **Coach**: helping James learn directly.

Priority order: design and audit, then coach, then everything else.

**Success looks like:**
- Agents building apps like Piaano and `study.html` make choices that follow the pedagogy without being told each time.
- Audits judge whether a method is conceptually sound for the learner's goal, not whether it copies a named method.
- Ordinary questions are never turned into lessons.

**Non-goals:**
- Not a general tutor that activates on every question.
- Not a store of facts about the books.
- Not a replacement for the project's own decision records.

## 2. Sources and their weight

1. **Primary voice:** James's own writing, in the sections *Learning*, *Zen Buddhism*, *Flow state*, *Implicit vs Explicit learning* and *Conflicting ideas about learning*. Where the sources disagree, his synthesis wins.
2. **Supporting evidence:**
   - *Ultralearning* (Young).
   - *Zen in the Art of Archery* (Herrigel).
   - *Flow* (Csikszentmihalyi).
   - The spaced-repetition / Anki mindset (Ebbinghaus, Bjork, Woźniak, Nielsen).
   - The Woodpecker Method (Smith & Tikkanen; de la Maza's Seven Circles).
   - Voltaic's training philosophy (Fundamentals 2.5, Benchmarks guide, Aim Journey, FAQ).
3. **Evidence levels:** every principle is tagged:
   - **established:** replicated research.
   - **practitioner:** consistent expert or community practice.
   - **philosophy:** a stance, not an empirical claim.
   - **hypothesis:** plausible but unsettled.

   Known corrections that the skill states accurately:
   - Flow-as-meditation and transient hypofrontality are hypotheses.
   - Chicken sexing: Biederman & Shiffrar (1987) showed that one explicit cue helped novices a lot. This supports "you need both".
   - "10% wrong = 10% bad muscle memory" is a heuristic, not a measured ratio.
   - Herrigel's account is a disputed interpretation of kyūdō and Zen.
   - Woodpecker's evidence is anecdotal.
   - Voltaic's VDIM day split could not be verified.

## 3. The model (`references/principles.md`)

### 3.1 Thesis
**A rigorous plan, done with a Zen attitude.**
- **Structure** decides what to practise, when, and at what difficulty.
- **Attitude** decides how to be while practising.

They answer different questions, so they don't conflict.

### 3.2 The arc: explicit knowledge becoming implicit skill
The unifying idea. Learning moves a skill from conscious, explicit control to implicit, embodied control, and each stage has its own methods and its own right attitude.

1. **Map (explicit):** set a specific long-term goal. Decompose the skill into categories and subcategories, each isolating one technique, with hybrids that bridge them. Plan habits one at a time.
2. **Acquire (explicit, learning zone):**
   - Slow down to near-perfect accuracy.
   - Change one variable at a time, within a difficulty budget.
   - Pause and rewind on mistakes.
   - Understand before memorizing; don't overload with theory.
3. **Automate (the transition):**
   - Retrieval and generation: test, write, teach.
   - Spacing.
   - Overlearning.
   - Repetition, either Woodpecker-style or varied, by the repetition-target rule.
4. **Perform (implicit, performance zone):** flow. A movement happens rather than "you moving".
   - Focus plus relaxation.
   - "Feeling" over reacting or predicting.
   - No mid-action judgement.
   - Notice mistakes, log them, and keep going.
5. **Review (explicit again):**
   - Recordings and outside eyes for hidden mistakes.
   - Rare, low-noise benchmarks.
   - Then back to Map.

**Corollary:** great performers make poor coaches because their knowledge has finished becoming implicit. A teaching system has to deliberately support the stages a master no longer remembers.

### 3.3 Structure principles
Each is written as: **what it says / why / signals present / signals absent / common misapplications / evidence level**.

- **S1. Map and decompose.** Use categories and subcategories with hybrids. Coverage makes weaknesses visible.
- **S2. Directness and transfer.** Practise in the real context. Transfer from the trainer to real use is something to check, not assume. Spend substantial time in the real context.
- **S3. Bottleneck drills on top of all-round practice.** Every session covers all categories; issue-specific add-ons target diagnosed weaknesses. Confront the uncomfortable weakness.
- **S4. Retrieval and generation over review.** Test, write, teach, then quiz yourself on what you taught.
- **S5. Understanding before memorizing; no theory overload.**
- **S6. Fast, informative, non-punitive feedback.** Hidden mistakes need review tools and outside eyes.
- **S7. Spacing for retention; overlearning and repetition for automaticity.**
- **S8. Difficulty in the goldilocks zone.** Too easy is boring. Too hard creates anxiety *and teaches the wrong technique*, because the learner reshapes their play to survive the task.
- **S9. Accuracy first, then speed.** Speed rises only once accuracy is near-perfect.
- **S10. One variable at a time, within a difficulty budget.** When one dimension goes up, dial the others back.
- **S11. Measure separately from training.** Benchmarks are rare, fixed and averaged over runs; training is varied. Never train on the test; never exploit the task ("cheesing").
- **S12. The repetition-target rule.**
  - If the patterns in the set *are* the skill, repeat the same set (Woodpecker).
  - If the set stands in for a general skill, vary it so the learner doesn't memorize the material.
- **S13. Mastery-based progression.** Schedule the inputs, not the outcomes: fix when you practise, and move on when the habit is formed, not by a date.
- **S14. Implicit vs. explicit by decision speed.** Explicit knowledge suits slow, complex decisions; implicit skill suits fast execution. Analogies to skills already mastered speed up implicit learning, and how something is taught shapes what sticks.

### 3.4 Attitude principles
- **A1. Process over progress.** Practising is the success. Goals are ones you're in charge of, not ones in charge of you.
- **A2. Discipline over motivation.** Systems and small default actions that survive moods.
- **A3. Observe, don't judge.** Feedback is information, not punishment. Separate the learning zone from the performance zone.
- **A4. Dosed intensity.** Rigour only works if enjoyment survives it (survivorship bias).
- **A5. Focus plus relaxation.** The effort to relax is itself the obstacle. Breathing builds rhythm. Flow can only be set up, never forced.
- **A6. Consistency as the measure.** Raise your worst day and narrow the spread. Mastery is internal; assessments are information, not self-worth.
- **A7. Peace of mind.** Know your direction is right even when some steps go backward. When flow isn't available, slow conscious effort still counts; don't let the perfect be the enemy of the good.

### 3.5 Tensions table (`references/tensions.md`)
The ten resolutions agreed in conversation:
1. Speed vs. accuracy.
2. Stop vs. continue on a mistake.
3. Goals vs. detachment.
4. Intensity vs. no timeframes.
5. Repetition vs. variety.
6. React vs. predict.
7. Explicit vs. implicit.
8. Rigour vs. enjoyment.
9. Flow ideal vs. flow unavailable.
10. Measuring vs. clinging.

Each row gives the tension, the resolution, and where it applies in app design.

## 4. Modes

### 4.1 Design (`references/design.md`)
**Input:** a learning app or feature to design.

**Workflow:**
1. **State the learner's goal and the kind of knowledge.** A decision table maps each kind to methods and anti-patterns: fact, concept, procedure, perceptual pattern, motor skill, strategic judgement.
2. **Build the skill map** (S1).
3. **Place each component on the arc:** decide which stages the app supports and which it leaves to other tools.
4. **Design the loop:**
   - Learning zone vs. performance zone, and how logged mistakes from performance become drills.
   - Benchmark cadence.
   - Difficulty system and difficulty budget.
   - Progression gates (mastery-based).
   - Feedback tone.
   - Process-first metrics.
5. **Check the design against the tensions table.**

**Output:** design notes in the project's own docs style, and they must respect recorded user decisions.

### 4.2 Audit (`references/audit.md`)
**Input:** an existing app, file or feature.

**Workflow:**
1. Establish what the app is *for*: the learner, the goal and the time horizon. If that can't be inferred, ask before judging.
2. Read the project's decision records (`HANDOFF.md`, `DECISIONS.md`, `CLAUDE.md`, etc.) and treat them as constraints.
3. Rate each relevant principle as **Strong / Partial / Missing / Conflicts / N/A**, with `file:line` evidence and the reasoning, judged conceptually against the goal rather than against a named method.
4. List strengths, not only gaps.

**Output:** a ranked findings list, each with severity, the principle, evidence, why it matters for *this* goal, and a concrete fix. A finding that contradicts a recorded user decision is listed once under **"Tensions with recorded decisions"** and never re-argued. Long audits are saved to `docs/dojo-audit-YYYY-MM-DD.md` in the project; short ones stay in chat.

### 4.3 Lens (`references/lens.md`)
**Opt-in.** A project turns it on with a line in `CLAUDE.md` or `HANDOFF.md`:

> `Dojo lens: on. Check learning-facing features against the dojo skill.`

When on, an agent building any learner-facing feature runs a six-question checklist:
1. Which arc stage does this serve?
2. Does it keep difficulty in the goldilocks zone, and respect the difficulty budget?
3. Is feedback fast and non-punitive?
4. Are mistakes handled correctly for the zone (drill vs. performance)?
5. Does it measure without training on the test?
6. Do its metrics reward process over progress?

It reports only real concerns, in at most a few lines, and never blocks work or re-argues recorded decisions.

### 4.4 Coach (`references/coach.md`)
- **Session-only:** a plan for the session, drills, retrieval and generation checks (including "teach it back"), and a debrief that observes rather than judges.
- **Long-running:** a folder per subject at `Documents\Learning\<subject>\`:
  - `plan.md`: goal, skill map, current habit focus, benchmark definition and cadence.
  - `log.md`: dated sessions, a process-first check-in, logged mistakes, benchmark results and notes on consistency.
  - `cards/*.csv`: decks (format in §5.1).
  - `woodpecker/<set>/`: `set.md` (problems plus full solutions) and `cycles.md` (cycle log).
- **Each session:**
  1. Check in on whether practice happened.
  2. All-category practice plus a bottleneck add-on.
  3. Review logged mistakes.
  4. Debrief and schedule the next session.
- Coach never measures progress against deadlines (S13, A1).

## 5. Tools

### 5.1 Cards (`references/cards.md`)
**Card-writing rules:**
- One fact per card.
- Recall, not recognition.
- Context and connections on the card.
- Both directions only when useful.
- Cloze-style fronts allowed.
- Write cards only after the material is understood.

**Default format:** CSV matching `study.html`'s parser.
- UTF-8, exactly 2 columns (front, back), **no header row**.
- A field containing a comma, quote or newline is wrapped in double quotes, with inner quotes doubled.
- `**bold**` and line breaks inside quoted fields are rendered.
- Fields are trimmed.
- Edge case: the parser drops the first row if its front contains "question" *and* its back contains "answer", so the generator must avoid that combination on row 1.

### 5.2 Anki package (`scripts/csv_to_apkg.py`)
- **Input:** a CSV in the format above, a deck name, and an optional `--reverse` flag.
- **Output:** an `.apkg` built with `genanki`, using a Basic note type, or Basic-and-reversed with `--reverse`.
  - `**x**` becomes `<b>x</b>` and newlines become `<br>`, with other HTML escaped.
  - Deck and model IDs come from a stable hash of the deck name, so re-imports update instead of duplicating.
- **Dependency:** `pip install genanki` on first use. The script prints that instruction if the package is missing.

### 5.3 Woodpecker builder (`references/woodpecker.md`)
**When:** offered *by name* in design or coach contexts when S12 says the patterns are the skill (chess motifs, chord shapes, grammar patterns, code idioms).

**Produces:**
- A set of problems with full solutions. The first-cycle accuracy target is "solvable with effort".
- A cycle schedule that halves the time limit each cycle.
- A tracking sheet.

**Rule:** every re-solve must reproduce *why* the solution works, not just recall the answer.

### 5.4 Benchmark builder
- A fixed, low-noise test set per category.
- A cadence (default weekly), averaging several runs.
- Results recorded as information, with consistency (worst day, spread) next to the averages.

## 6. Triggering
- **Name:** `dojo`. Explicit use: `/dojo`, or phrases like "dojo this," "open a dojo for X," "dojo audit."
- **Auto-triggers (from the description):**
  - Designing or auditing anything meant to teach or train.
  - "Teach me," "help me learn," "make flashcards," "Woodpecker," "practice plan."
  - The lens line in a project's `CLAUDE.md` or `HANDOFF.md`.
- **Never** triggers on ordinary questions: no unprompted quizzes or offers.

## 7. Layout

```
dojo/
  SKILL.md               thesis, arc summary, triggers, mode routing (<200 lines)
  references/
    principles.md        §3.2–3.4 in full
    tensions.md          §3.5
    sources.md           condensed sources + evidence levels + corrections
    design.md            §4.1 + knowledge-type decision table
    audit.md             §4.2 + report template
    lens.md              §4.3
    coach.md             §4.4 + file templates
    cards.md             §5.1
    woodpecker.md        §5.3 + §5.4
  scripts/
    csv_to_apkg.py       §5.2
  README.md              for the GitHub repo (what it is, install)
```

## 8. Repository and install
- **Source:** a git repo at `C:\Users\James\Documents\Dojo\`, with this spec in `docs/specs/`.
- **Install:** a directory junction from `C:\Users\James\.claude\skills\dojo` to the repo's `dojo/` folder, so edits are live without copying. A junction needs no admin rights.
- **GitHub:** push at the end, after confirming the repo name and visibility with James and checking that `gh` is installed and signed in.

## 9. Build order
1. `principles.md`, `tensions.md` and `sources.md`. **James reviews these before anything else is built.**
2. `SKILL.md` (routing and triggers).
3. `audit.md` and `design.md`.
4. `lens.md` and `coach.md`.
5. `cards.md`, `csv_to_apkg.py` and `woodpecker.md`.
6. Evals.
7. README, install, GitHub push.

## 10. Testing
Use the skill-creator eval workflow. Test prompts and what each should show:
1. **Audit `study.html`:** asks for or infers the deck's goal before judging the fixed 1–3 day intervals; credits Mute, undo, both directions and Cycle mode.
2. **Design Piaano's Pattern Trainer scheduler:** applies S12 (chords call for repetition) and the drill/performance split, and respects HANDOFF decisions.
3. **A small Piaano feature request with lens on:** at most a few lines of concerns, no blocking.
4. **"Teach me the basics of X":** coach mode starts a map and a session.
5. **An ordinary factual question:** the skill does not trigger.
6. **"Make flashcards from these notes":** the CSV passes a parser check that mirrors `study.html`'s `parseCSV`, and `csv_to_apkg.py` produces a package that loads.
