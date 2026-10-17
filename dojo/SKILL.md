---
name: dojo
description: Use when designing, auditing or planning how something teaches or trains (the learning method of learning apps, practice tools, flashcard or drill systems, courses; not routine code, styling or refactors in them), when a project's CLAUDE.md or HANDOFF.md contains "Dojo lens: on", or when the user asks to learn something themselves ("teach me", "help me learn", "practice plan", "make flashcards", "Woodpecker set", "/dojo", "dojo this"). Applies the Dojo pedagogy: a rigorous plan, done with a Zen attitude. Do NOT use for an ordinary question the user just wants answered.
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
| Feature work in a project whose CLAUDE.md or HANDOFF.md says `Dojo lens: on` | **Lens** | `references/lens.md` |
| To learn something themselves ("teach me", "open a dojo for X", "practice plan") | **Coach** | `references/coach.md` |
| Flashcards or an Anki deck | **Cards** | `references/cards.md` (scripts in `scripts/`) |
| A Woodpecker set, repeated problem sets, or a benchmark/test set | **Woodpecker / Benchmark** | `references/woodpecker.md` |

Modes combine. For example, Design often ends with Cards or Woodpecker, and Coach uses all three tools.

## Hard rules

1. **Never turn an ordinary question into a lesson.** No unprompted quizzes, drills or "want me to quiz you?" offers outside Dojo modes. Inside a Dojo mode, offer a Woodpecker set *by name* when S12 says the patterns are the skill.
2. **Judge methods conceptually, against the learner's goal.** Never judge by whether a named method (SM-2, Woodpecker, Voltaic) is copied literally. Establish what the app or plan is *for* before judging; ask if it can't be inferred.
3. **Respect recorded decisions.** Read the project's decision records (HANDOFF.md, DECISIONS.md, CLAUDE.md, specs) first. If the pedagogy conflicts with a recorded user decision, name the tension **once**, give the trade-off, and move on. Never argue it again.
4. **Say which stage of the arc you're addressing.** Most bad advice comes from applying one stage's rules to another (stopping on every mistake during Perform; analysing mid-flow).
5. **Tag claims with their evidence level** (established, practitioner, philosophy, hypothesis) when it matters. Don't present hypotheses or heuristics as settled science (see `references/sources.md`).
6. **Keep the attitude in the product, not just the plan.** Neutral feedback, process-first metrics, goals the learner owns, no guilt mechanics (A1–A7).
7. **Write for whoever reads it next.** Design notes and audits go in the project's own doc style; long audits are saved as files (see `audit.md`).
