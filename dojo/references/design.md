# Design mode

Use this to shape a new learning app, feature, course or practice system, or to plan an upgrade. Read `principles.md` first.

## Before designing

- Read the project's decision records (HANDOFF.md, DECISIONS.md, CLAUDE.md, specs, design docs). Recorded user decisions are constraints. Don't re-open them; if the pedagogy strongly conflicts with one, name the tension once (see SKILL.md, hard rule 3).
- Look at what already exists. Most good designs extend what the app already does well.

## Workflow

### 1. State the learner's goal and the kinds of knowledge involved
Write one or two sentences covering **who** is learning, **what** they should be able to do, **in what real context**, and over **what time horizon** (exam next week vs. a lifelong skill). Then name which kinds of knowledge the skill involves, using the table below. Most real skills mix several.

| Kind | Methods | Arc stages | Anti-patterns |
|---|---|---|---|
| Fact | Retrieval cards, spaced (S4, S7); cloze in context | Automate | Rereading lists; recognition-only quizzes; cards before understanding |
| Concept | Explanation with examples, then teach-back / explain-it-simply, then questions that apply it (S4, S5) | Acquire → Automate | Memorizing definitions without being able to use them; theory dumps |
| Procedure | Worked example → guided practice → independent practice; accuracy before speed (S9); overlearn (S7) | Acquire → Automate | Speed targets from day one; steps never practised start to finish |
| Perceptual pattern | High-volume recognition with instant feedback; one explicit cue where it helps (S14); a fixed set when the patterns are the skill, varied material when they aren't (S12) | Automate → Perform | Verbal rules only; a tiny repeated set used for a general skill |
| Motor skill | Slow, near-perfect reps; one variable at a time inside a difficulty budget (S9, S10); drill vs. run-through modes (A3, T2); review of recordings (S6) | Acquire → Automate → Perform | Too fast too soon; changing several variables at once; stopping on every mistake during performance |
| Strategic judgement | Explicit frameworks, case review and post-mortems; decisions made slowly at first (S14) | Map, Review | Treating it as a reflex to drill; no review of past decisions |

### 2. Build the skill map (S1)
Break the skill into **categories** and **subcategories** that each isolate one technique, plus **hybrids** where real use blends them. For each subcategory, note what makes it distinct (what you'd train differently) and how you could measure it. If two subcategories would be trained the same way, merge them.

### 3. Place each part on the arc
For every feature, decide which stage(s) of the arc it serves: Map, Acquire, Automate, Perform or Review. Note which stages the app deliberately leaves to other tools, and say so. A good app needn't do everything, but it shouldn't pretend to.

### 4. Design the loop
Go through this checklist and write down a decision for each item:

- **Default session:** covers all categories at the learner's level (S3). How long is it (A4)? How quick is it to start (A2)?
- **Bottleneck add-on:** how the weakest subcategory is found and drilled in a short, capped block, then folded back in (S3, A4).
- **Learning zone vs. performance zone:** a drill mode (pause, rewind, correct) and a run-through mode (notice, log, keep going). **Mistakes logged in run-throughs feed the drills** (A3, T2).
- **Difficulty system:** adaptive or manual controls that keep the challenge in the goldilocks zone (S8). Give it a slow-down or timescale control.
- **Difficulty budget:** when one axis goes up (tempo, range, density, hands, distractors), others ease off, and new elements arrive one at a time (S10).
- **Accuracy gate:** speed or tempo rises only while accuracy holds, and falls back when it doesn't (S9, T1).
- **Repetition vs. variety:** fixed sets where the patterns are the skill; generated or rotating material where the set stands in for a general skill (S12, T5).
- **Retention:** spaced return of learned items, with maintenance for "mastered" items (S7).
- **Feedback:** per attempt, directional, fast, neutral in tone. Plus review tools: replay, history, recordings (S6, A3).
- **Benchmark:** a separate, fixed, low-noise benchmark per category, with a cadence (default weekly) and averages over several runs; never the same as practice (S11, T10).
- **Progression:** unlocks based on demonstrated skill, never on the calendar (S13, T4).
- **Metrics:** practice done comes first; consistency (worst session, spread) next; peak scores last (A1, A6).
- **Attitude in the UI:** neutral wording, goals the learner owns, an easy way to set things aside without guilt, a calm way into a session, no punishing streaks (A1–A5, T9).

### 5. Check against the tensions
Go row by row through `tensions.md` (T1–T10). For each row that applies, write one line saying how the design resolves it. If the design takes a side without naming the arc stage it serves, fix it.

## Output

Design notes in the project's own style: its doc folder, headings and voice. Include:
1. The goal statement.
2. The skill map.
3. Each feature mapped to its arc stage.
4. The loop decisions.
5. The tensions check.
6. Open questions for the user (only genuine decisions).

Keep principle IDs in parentheses so later agents can trace the reasoning.

## Worked mini-example: Piaano's Pattern Trainer scheduler

*Context:* Piaano's Pattern Trainer introduces chords and inversions in four steps (meet it, note by note, together with keys lit, together alone). Step 3, a scheduler, isn't built yet.

- **Goal:** instant recognition and playing of chord shapes from notation, for sight-reading real music.
- **Kind:** perceptual pattern plus motor skill.
- **S12:** chord shapes *are* the skill, so a fixed set is right. Each introduced chord joins a Woodpecker-style pool that is cycled with shrinking time targets, plus spaced return (S7) so old chords don't fade.
- **T1 / S9:** the time target tightens only while accuracy stays near-perfect; one miss eases it back.
- **T2:** the scheduler runs in Wait (the learning zone: the miss is corrected on the spot). Misses also feed a short drill pool at the end of the session.
- **S10:** while a new chord family is being introduced, hold tempo and range steady.
- **A6:** show per-chord consistency (slowest recent recognition), not only the best time.
- **Leave alone:** HANDOFF's recorded decisions, for example no free-form climb and no ranks.
