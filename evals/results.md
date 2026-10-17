# Dojo eval results: 2026-10-16

Run as fresh subagents with the skill installed. Outputs were kept locally in `evals/workspace/` (git-ignored).

| # | Eval | Result | Notes |
|---|---|---|---|
| 1 | Audit `study.html` | **Pass** | Wrote the goal question first and showed how each finding changes for exam prep, lifelong decks or a mix. Credited Mute, undo, per-direction schedules and backup. Treated the fixed intervals as a recorded decision, raised once as a tension with a middle path (intervals that grow up to a per-group cap). Flagged permanent Mastered and the missing "forgot" grade with fixes. Offered a Woodpecker set by name for pattern decks. Found on its own that `Neocities/` is a read-only archive and targeted the live `site/study/`. |
| 2 | Design Piaano Pattern Trainer step 3 | **Pass** | Found that step 3 was already built and switched to a list of improvements. Respected every recorded decision. Applied S12, S1 (separate clefs) and A6. Found 11 pairs of identically written chord items by running the real code. **Exposed a stale worked example in `design.md`** (fixed: see below). |
| 3 | Lens on a streak feature | **Pass** | Planned the feature exactly as asked, with no blocking. Added a short Dojo lens note: the hard reset is a guilt mechanic (A1/T3/T9), and the fix is to also show total days practised, with neutral wording. |
| 4 | "Teach me the basics of musical intervals" | **Pass** | Session-only coach: a one-line goal, a brief concrete explanation, exercises before answers, a teach-back prompt. Asked whether he wants a long-running dojo; no folder created. |
| 5 | Ordinary question (major vs. minor third) | **Pass** | The skill wasn't invoked. A plain answer, with no quiz, cards or offers. |
| 6 | Flashcards from notes | **Pass** | 9 atomic recall cards (cloze plus questions, no true/false); `cards_csv.py` prints `OK: 9 cards`; row 1 avoids the header quirk; one direction only (the app's Swap mode covers the reverse). |

## Fixes made from the evals

- `design.md`: the worked example assumed Piaano's scheduler was unbuilt and suggested shrinking time targets, which conflicts with the user's target-time setting. It's rewritten to be general, tells the agent to check what exists first, keeps existing target-time rules, and adds the "one item = what the learner sees" and per-clef lessons from eval 2.
- `cards.md` and `audit.md`: they pointed at the Neocities archive. They now point at the live `Website/site/study/` (decks in `site/study/cards/`, index via `tools/build_deck_index.py`) and note that the archive is read-only.
