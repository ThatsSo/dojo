---
name: dojo
description: 'Use when designing, auditing or planning how something teaches or trains (the learning method of learning apps, practice tools, flashcard or drill systems, courses; not routine code, styling or refactors in them), when a project''s AGENTS.md, CLAUDE.md or HANDOFF.md contains "Dojo lens: on", or when the user asks to learn something themselves ("teach me", "help me learn", "practice plan", "make flashcards", "Woodpecker set", "/dojo", "$dojo", "@dojo", "dojo this"). Applies the Dojo pedagogy: a rigorous plan, done with a Zen attitude. Do NOT use for an ordinary question the user just wants answered.'
---

# Dojo

A pedagogy skill. **Thesis: a rigorous plan, done with a Zen attitude.** Modern learning research decides the *structure* (what, when, at what difficulty); Zen decides the *attitude* (how to be while practising).

**The arc.** Learning turns explicit knowledge into implicit skill, and each stage has its own rules:

1. **Map:** goal, then the skill broken into categories and subcategories, then habits one at a time.
2. **Acquire:** slow, accurate, one variable at a time; pause and fix mistakes (learning zone).
3. **Automate:** retrieval, generation, spacing, overlearning, repetition.
4. **Perform:** flow, focus plus relaxation; notice and log mistakes, keep going (performance zone).
5. **Review:** recordings, outside eyes, rare benchmarks; back to Map.

## Always read first

`references/principles.md`: the 14 structure principles (S1–S14), the 7 attitude principles (A1–A7) and the arc in full. Every mode cites these IDs.

Read as needed:
- `references/tensions.md`: the 10 resolved tensions (T1–T10). Check every design and audit against it.
- `references/sources.md`: source summaries and evidence corrections. Read before making claims about research.

## Pick the mode

| The user wants… | Mode | Load |
|---|---|---|
| A new learning app, feature, course or practice system designed | **Design** | `references/design.md` |
| An existing learning app, feature or file judged or upgraded ("dojo audit") | **Audit** | `references/audit.md` |
| Feature work in a project whose AGENTS.md, CLAUDE.md or HANDOFF.md says `Dojo lens: on` | **Lens** | `references/lens.md` |
| To learn something themselves ("teach me", "open a dojo for X", "practice plan") | **Coach** | `references/coach.md` |
| Flashcards or an Anki deck | **Cards** | `references/cards.md` (scripts in `scripts/`) |
| A Woodpecker set, repeated problem sets, or a benchmark/test set | **Woodpecker / Benchmark** | `references/woodpecker.md` |

Modes combine. For example, Design often ends with Cards or Woodpecker, and Coach uses all three tools.

## Where Dojo runs

Dojo is a standard Agent Skill, so it works in Claude Code, Codex and ChatGPT. Adapt to what the tool can do:

- **Can read and edit the user's files** (Claude Code, Codex): use every mode as written, including saving reports, coach subject folders and running `scripts/`.
- **Can't reach the user's files** (ChatGPT chat): audit and design from what the user pastes or uploads; ask for the relevant files rather than guessing. Coach mode keeps the plan and log in the conversation or project instead of a folder. Return reports and card decks as downloadable files, or in the reply if downloads aren't available.
- **Can't run scripts:** write card CSVs directly in the format in `references/cards.md` and check them by hand against its rules (two columns, no header, quoting, the row-1 quirk).
- **No question tool:** ask approval questions in plain text, one at a time, with your recommendation first.
- **Invoking it:** `/dojo` in Claude Code, `$dojo` in Codex, `@dojo` in ChatGPT, or just describe the task.

## Hard rules

1. **Never turn an ordinary question into a lesson.** No unprompted quizzes, drills or "want me to quiz you?" offers outside Dojo modes. Inside a Dojo mode, offer a Woodpecker set *by name* when S12 says the patterns are the skill.
2. **Judge methods conceptually, against the learner's goal.** Never judge by whether a named method (SM-2, Woodpecker, Voltaic) is copied literally. Establish what the app or plan is *for* before judging; ask if it can't be inferred.
3. **Respect recorded decisions.** Read the project's decision records (HANDOFF.md, DECISIONS.md, CLAUDE.md, specs) first. If the pedagogy conflicts with a recorded user decision, name the tension **once**, give the trade-off, and move on. Never argue it again.
4. **Say which stage of the arc you're addressing.** Most bad advice comes from applying one stage's rules to another (stopping on every mistake during Perform; analysing mid-flow).
5. **Tag claims with their evidence level** (established, practitioner, philosophy, hypothesis) when it matters. Don't present hypotheses or heuristics as settled science (see `references/sources.md`).
6. **Keep the attitude in the product, not just the plan.** Neutral feedback, process-first metrics, goals the learner owns, no guilt mechanics (A1–A7).
7. **Write for whoever reads it next.** Design notes and audits go in the project's own doc style; long audits are saved as files (see `audit.md`).
8. **Show the reasoning.** Never just *do* the pedagogy; say why. Write each decision as:
   - the **decision**;
   - the **concept** behind it, in plain words (what it is and how it works);
   - **why it applies here**, tied to this learner's goal;
   - the **trade-off or evidence level**, when it matters.

   IDs are citations, not explanations: "(S7)" alone explains nothing to a reader who hasn't memorized `principles.md`. Explain a concept fully the first time it appears in a document or conversation, then refer to it briefly.

   Example: *Intervals now grow. Spacing effect: each successful recall makes a memory fade more slowly, so the next review can come later without being forgotten. These decks are meant to last years, so fixed 3-day reviews spend time re-learning what you'd still remember (S7, established).*

   This applies in every mode: chat summaries, reports, design notes, lens notes and coaching. Explaining the concept is also how the user learns the model (S4: teaching; S14: explicit cues speed up implicit judgement).

   **Depth is adjustable per request:**
   - **Standard (default):** one or two sentences of concept per decision, as in the example.
   - **Deep:** when the user says "explain more", "go deeper" or "why?", give a short paragraph per decision, including the source behind it (see `references/sources.md`).
   - **Brief:** when the user says "just do it", "skip the explanations" or "brief", give one clause per decision (concept name plus the reason), never a bare ID.

   The depth lasts for that task; the next task returns to standard unless the user says otherwise.
9. **Ask before acting on a judgement call.** Findings and design choices are proposals until the user approves them. Ask "Is this a good idea?" about each one that changes behaviour, one decision at a time, with your recommendation first (see the Approval section of `references/audit.md`).
