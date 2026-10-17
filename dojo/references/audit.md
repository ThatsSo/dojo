# Audit mode

Use this to judge or upgrade an existing learning app, feature or file. Read `principles.md` first.

**The core rule: judge methods conceptually, against the learner's goal.** Ask whether the method is sound for what the learner is trying to do, given how learning works. Don't ask whether it copies SM-2, Woodpecker or Voltaic. A homemade scheduler can be excellent; a textbook one can be wrong for the goal.

## Workflow

### 1. Establish what the app is for
Before judging anything, write down **what the app is for**: the learner, the skill or knowledge, the real context, and the time horizon (short-term exam prep, ongoing practice, lifelong retention). Look in the README, specs, HANDOFF.md, the app's own help text and how it's used. **If you can't infer it, ask the user before judging.** Many findings flip depending on the answer.

### 2. Read the decision records
Read HANDOFF.md, DECISIONS.md, CLAUDE.md, specs and code comments that explain choices. A recorded user decision is a constraint. A finding that contradicts one goes in **Tensions with recorded decisions**, stated once with the trade-off, and is never argued again.

### 3. Rate each relevant principle
For each of S1–S14 and A1–A7 that applies, give one rating:

- **Strong:** the app embodies it well. Say so and say where.
- **Partial:** present but incomplete or inconsistent.
- **Missing:** absent where the goal needs it.
- **Conflicts:** the app works *against* it.
- **N/A:** doesn't apply to this goal. Say why in a few words.

Each rating needs **evidence as `file:line`** (or a UI path), plus the reasoning tied to the goal from step 1. Also check the relevant rows of `tensions.md`; a design that takes one side of a tension for the wrong arc stage is a finding.

### 4. Credit what works
List **Strengths** first, and mean them. Audits that only list gaps get ignored, and strengths show what to build on.

### 5. Rank the findings
Severity is about the effect on the learner, given the goal:
- **High:** actively teaches the wrong thing, loses learning, or drives the learner away (for example, difficulty that forces bad technique, or progress that silently decays).
- **Medium:** leaves significant value on the table (for example, no retrieval where it's needed, or no benchmark).
- **Low:** polish (wording tone, a missing stat).

Each finding gets a **concrete fix** sized to the codebase: name the function or screen and the change, not "consider improving".

## Report template

```markdown
# Dojo audit: <app or feature> (<date>)

## Goal
<learner, skill, real context, time horizon; note if confirmed by the user or inferred>

## Strengths
- <principle ID> <what works> (`file:line`)

## Findings
1. **[High] <title>** (<principle IDs>)
   - Evidence: `file:line`, <what the code does>
   - Why it matters for this goal: <reasoning>
   - Fix: <specific change>
2. …

## Tensions with recorded decisions
- <decision, where recorded>: <how it conflicts with which principle, and the trade-off>. Stated once; not re-argued.

## Ratings
| Principle | Rating | Evidence |
|---|---|---|
| S1 Map and decompose | Partial | `file:line` |
| … | | |

## Summary
<3–5 sentences: overall shape, the top two fixes, what to leave alone>
```

**Where it goes:**
- **Long audits** (more than about 10 findings, or a whole app) are saved to `docs/dojo-audit-YYYY-MM-DD.md` in the audited project; use the project's docs folder if it has another name. Reply with a short summary and the path.
- **Short audits** (a single feature or file) can stay in chat.

## Worked mini-example: `study.html`'s review intervals

*Observed:*
- The "SM-2" mode uses fixed intervals of 1, 2 and 3 days for Hard, Medium and Easy (`REVIEW_DAYS`). A comment says they're kept short so nothing drifts far out.
- "Mastered" retires a card from reviews permanently.
- There's no grade for "I forgot".

*Conceptual judgement, depending on the goal:*

- **If the decks are for exam prep within a few weeks:** short fixed intervals are defensible (dense review close to the test). Rating: S7 **Partial**, with low severity. Suggest an "I forgot" grade that brings the card back in the same session.
- **If the decks are for lifelong knowledge** (philosophy, psychology, languages): intervals that never grow throw away the spacing effect. Review load never shrinks, and mature cards cost as much as new ones. Rating: S7 **Conflicts**, high severity.
  - Fix: grow the interval on success (for example, multiply it by an ease factor) and reset it on "forgot".
  - Keep a cap only if the user wants one.
  - Replace permanent retirement with a long maintenance interval.
- **Credit either way:** separate schedules per direction (S4, S7), undo, the due overview with Mute (A1: setting things aside without guilt), backup and restore, and Cycle mode (halfway to a Woodpecker mode, S12).

Ask which goal applies (or both, per deck) before rating.
