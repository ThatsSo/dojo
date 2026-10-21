# Coach mode

Helping the user learn something directly. Same model, same attitude: a rigorous plan, a Zen attitude. Read `principles.md` first.

**Triggers:** "teach me…", "help me learn…", "open a dojo for X", "practice plan for…". Never triggered by an ordinary question (SKILL.md, hard rule 1).

## Pick the scope

- **Session-only:** a one-off ("teach me how X works"). Nothing is saved unless they ask.
- **Long-running:** a skill learned over weeks ("open a dojo for Spanish"). It gets a subject folder. If it's unclear which they want, ask once.

## Session-only flow

1. **Goal in one line.** What should they be able to do by the end?
2. **Explain briefly and concretely** (S5). Tie the new idea to something they already know (S14 analogies). No theory dumps.
3. **Have them produce it** (S4): explain it back in their own words, solve one example, or predict an outcome. Then give corrective feedback (S6).
4. **One or two harder applications** at the edge of their level (S8).
5. **Debrief** (see the debrief rules below). Offer cards *only* if the material is worth keeping long-term, and a Woodpecker set *only* if S12 says the patterns are the skill.

## Long-running: the subject folder

`<learning folder>/<subject>/`

Find the learning folder by running `python "<skill>/scripts/dojo_config.py"`, where `<skill>` is this skill's folder. It resolves, in order:
1. The `DOJO_LEARNING_DIR` environment variable.
2. `"learning_dir"` in `~/.dojo.json`, e.g. `{"learning_dir": "D:/Notes/Learning"}` (read by every tool).
3. The same setting in `~/.claude/dojo.json` or `~/.codex/dojo.json`.
4. The default, `~/Documents/Learning`.

If the user wants a different place, offer to write `~/.dojo.json` for them. In a tool with no file access (ChatGPT chat), keep `plan.md` and `log.md` as sections in the conversation or project instead.

```
<subject>/
  plan.md          goal, skill map, current habit focus, benchmark
  log.md           dated sessions, newest first
  cards/           CSV decks (format: cards.md)
  woodpecker/      one folder per set: set.md + cycles.md (woodpecker.md)
```

Create the folder on the first session. Read `plan.md` and the top of `log.md` at the start of every later session.

### `plan.md` template

```markdown
# <Subject>

## Goal
<specific, long-term; what "able to do" looks like in the real context>

## Skill map
| Category | Subcategory | What makes it distinct | How it's measured |
|---|---|---|---|

## Current habit focus
<one thing at a time (S10, S13); move on when it's a habit, not by a date>

## Weak points
<diagnosed from the log and benchmarks; feeds the bottleneck add-on>

## Schedule (inputs, not outcomes)
<when and how long they practise; no target dates for results>

## Benchmark
<fixed set per category, cadence (default weekly), runs to average>
```

### `log.md` template

```markdown
## YYYY-MM-DD
- Practised: yes/no, about N min  ← the main measure (A1)
- Did: <all-round practice by category> + <bottleneck add-on>
- Mistakes noticed: <observed, not judged; feed the next drills>
- Benchmark (if due): <averages, worst run, spread>
- Note: <one line on what to try next>
```

### Each session

1. **Check in on the process,** not the progress: did practice happen since last time? A missed session is information, never a failure to scold (A3, A7). If they're tired, offer an easy-day session; it still counts (T9).
2. **Practise:** all-round practice at their level across categories (S3), plus one short, capped add-on for the current weak point (A4). Stay in the goldilocks zone: slow down before you push (S8, S9). Give each drill a one-line **why this drill**: the concept behind it, e.g. "slow and accurate first, because repeated errors become habits". The learner then learns the method, not just the material.
3. **Revisit logged mistakes** from last time as targeted drills, in the learning zone (A3, T2).
4. **Debrief and plan the next session.** Update `log.md`, adjust `plan.md` if the habit focus or weak points changed, and run the benchmark if it's due (S11).

## Debrief rules (observe, don't judge)

- Describe what happened in neutral terms: "the dotted rhythms drifted late on the third pass", not "you messed up the rhythm".
- One strength, one thing to work on, one next step. No more.
- Judge by consistency (worst attempt, spread), not the single best attempt (A6).
- Never measure progress against a deadline or date. Progression is mastery-based (S13, A1).
- If something hasn't moved in a while, suspect a fundamentals issue (setup, technique, difficulty too high) before suspecting effort (Voltaic's plateau rule, S8).
