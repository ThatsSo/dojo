# Coach mode

Helping the user learn something directly. Same model, same attitude: a rigorous plan, a Zen attitude. Read `principles.md` first.

**Triggers:** "teach me…", "help me learn…", "open a dojo for X", "practice plan for…", "help me prepare for <exam>". Never triggered by an ordinary question (SKILL.md, hard rule 1).

Explain the reasoning as you go (SKILL.md, hard rule 8). For example, give each drill a one-line **why this drill**: the concept behind it, such as "slow and accurate first, because repeated errors become habits". The learner then learns the method, not just the material.

## Pick the scope

- **Session-only:** a one-off ("teach me how X works"). Nothing is saved unless they ask.
- **Long-running:** a skill learned over weeks, or preparation for an exam or other target ("open a dojo for Spanish", "help me pass the AUD exam"). It is always file-backed (see "The plan file is the memory"). If it's unclear which they want, ask once.

## Session-only flow

Same time box as long-running sessions: **25 minutes** by default, or whatever the learner asks for.

1. **Goal in one line,** plus the time box. What should they be able to do by the end?
2. **A mini-ladder of 2–4 rungs** for the skill (see "Progression ladders"), shown up front so the lesson has a visible finish.
3. **Explain briefly and concretely** (S5). Tie the new idea to something they already know (S14 analogies). No theory dumps.
4. **Have them produce it** (S4) on each rung: explain it back, solve one example, or predict an outcome. Give corrective feedback (S6), then move up a rung once it's cleared.
5. **Stop on time and debrief** (see the debrief rules below). Offer cards *only* if the material is worth keeping long-term, and a Woodpecker set *only* if S12 says the patterns are the skill.

## Long-running: Planning comes first

Long-running coaching has two phases: **Planning** (once) and **Sessions** (repeated). Always show where you are with a status line at the top of each reply, for example `Planning, step 2 of 4: skill map` or `Session 5 · block 2 of 4: ladder work`.

**Planning, step 1 of 4: goal and research.** Pin down what "done" looks like in the real context, any deadline or exam date, the time available per week, and why they want it. If the goal names an external target (an exam, certification, grade, syllabus or standard), research it now, following `research.md`. Look up the real outline instead of guessing at what the questions might be.

**Planning, step 2 of 4: skill map.** Build it from the research, or from the goal when there's no external target: categories and subcategories (S1), each with a status and a progression ladder.

**Planning, step 3 of 4: placement check.** Announce it as a placement check: at most about **8 short items or 10 minutes**, spread across the map. Its only job is to set each skill's starting rung and status. Record the results in the plan. Don't teach, correct at length or drill during it: give the answer in one line and move on.

**Planning, step 4 of 4: write the plan file and get approval.** Write `plan.md` and `log.md` (templates below), show a short summary of the plan, and ask "Is this plan a good idea? Do you approve?" (SKILL.md, hard rule 9). Session 1 starts after approval.

**Stay on task:** if you notice you're teaching during Planning, stop, note the point under "Next session" in Resume here, and return to the current Planning step. Planning should take one sitting.

## The plan file is the memory

Long conversations get **compacted** (summarized), and new conversations start blank. The files, not the chat, are the source of truth for the plan *and* for progression. A fresh conversation given only the files must be able to continue exactly where the last session stopped.

- **Start of every session:** read `plan.md` (Resume here first) and the latest `log.md` entry.
- **End of every session:** update both, and rewrite Resume here.
- **Older plan files** (from before these sections existed): add any missing sections, in the template's order, the next time you open the file, and keep everything already there. Two old sections move: fold `## Current habit focus` into Resume here (the "Now" line) and the Progression ladders, then remove it; move `## Schedule (inputs, not outcomes)` into Settings (Sessions per week). Extra sections are fine, but put them after the Settings section so the template order stays intact.

### Where the files live

- **Tools with file access (Claude Code, Codex):** `<learning folder>/<subject>/`. Find the learning folder by running `python "<skill>/scripts/dojo_config.py"`, where `<skill>` is this skill's folder. It resolves, in order:
  1. The `DOJO_LEARNING_DIR` environment variable.
  2. `"learning_dir"` in `~/.dojo.json`, e.g. `{"learning_dir": "D:/Notes/Learning"}` (read by every tool).
  3. The same setting in `~/.claude/dojo.json` or `~/.codex/dojo.json`.
  4. The default, `~/Documents/Learning`.

  If the user wants a different place, offer to write `~/.dojo.json` for them.
- **Tools with their own file storage (ChatGPT project files, canvas or documents):** keep `plan.md` and `log.md` there and update them in place each session.
- **Tools that can't store files:** at the end of each session, give the updated `plan.md` as a downloadable file, and a short **state block** the learner pastes into the next conversation. The state block is Resume here, the full Review schedule table, the current rung and remaining rungs for each skill being acquired, the Weak points, and Settings. Tell the learner plainly that this file and state block are what keep their progress. At the start of the next session, ask them to upload the latest plan.md. If they only have the state block, continue from it, mark anything it doesn't cover as unknown until the file arrives, and never invent intervals, rungs or history.

```
<subject>/
  plan.md          the plan and all progression (template below)
  log.md           dated sessions, newest first
  cards/           CSV decks (format: cards.md)
  woodpecker/      one folder per set: set.md + cycles.md (woodpecker.md)
```

### `plan.md` template

```markdown
# <Subject>

## Resume here
- Phase: <Planning step N of 4 | Sessions>
- Now: <skill> · rung <n> of <total> (<what the rung is>)
- Next session: <the plan for the next session, including any points parked during Planning>
- Reviews due: <items due on or before the next session>
- Weak points to watch: <top 3>
- Last session: <date> · Session length: <minutes>

## Goal
<what "done" looks like in the real context; deadline or exam date if any; why they want it>

## Research
<for external targets: the cited blueprint summary (template in research.md); otherwise "No external target.">

## Skill map
| Category | Subcategory | Status | Move on when |
|---|---|---|---|
<status is one of: not started, acquiring, automating, solid>

## Progression ladders
### <skill>
Variables: <variable: easiest → target range>, ...
Clear a rung with N = <2> correct (<1> for long or worked answers)
| Rung | Adds | Status |
|---|---|---|
| 1 | <starting level> | cleared |
| 2 | <one variable one step harder> | current |

## Weak points
| Item | Found | Evidence | Plan | Status |
|---|---|---|---|---|

## Review schedule
| Item | Last reviewed | Interval (days) | Next due | History |
|---|---|---|---|---|

## Benchmark
<what is measured, how often (default weekly), results with worst run and spread>

## Settings
- Session length: 25 minutes
- Sessions per week: <number, and preferred days or times>
- Explanation depth: standard
- Rung clear count: N = 2 (short answers), 1 (long or worked answers)
```

### `log.md` template

```markdown
## YYYY-MM-DD
- Practised: yes/no, about N min  ← the main measure (A1)
- Did: <reviews done> · <ladder work: skill, rungs cleared> · <mixed practice>
- Mistakes noticed: <observed, not judged; added to Weak points if they repeat>
- Ladder: <skill: rung a → rung b>
- Note: <one line on what to try next>
```

## Progression ladders (how Acquire progresses)

Acquire deliberately keeps adding difficulty, so it can't end on an accuracy streak at an easy level. Instead, each skill being acquired gets a **ladder**. This is progressive overload made explicit (S15): small steps, one variable at a time (S10).

- **List the variables that make the skill harder,** each with a target range. *Example, intervals by ear:* size (2nds → octave), direction (ascending → descending → harmonic), register (middle → wide), tempo (slow → normal).
- **Arrange them as rungs:** each rung makes exactly one variable one step harder than the last.
- **A rung is cleared** after `N` correct answers at that level. The default is `N = 2` for short answers, and 1 for long or worked answers (a full journal entry, a multi-step problem). The learner can change `N` in Settings.
- **Two misses on a rung:** step back one rung, or ease another variable (the difficulty budget, S8, S10), then climb again. Don't grind.
- **Acquire for a skill ends only when every variable has been cleared at its target range.** Then the skill's status becomes `automating` and its key items enter the Review schedule.
- **The current rung is saved in `plan.md`,** so a session can stop anywhere and the next one resumes on the exact rung.

## Review schedule (spaced repetition)

When a rung is cleared, add its key item (the fact, rule or judgement the rung tested) to the Review schedule with a 1-day interval, so spacing starts during Acquire rather than weeks later. Weak points enter too. When a skill reaches `automating`, add any remaining key items.

Reviews come at the start of each session, from the Review schedule table. Review only items due on or before today; don't pull future items forward. If nothing is due, give the block's time to ladder work.

- **Correct:** double the interval: 1 → 2 → 4 → 8 → 16 → 32 days, then a **60-day** maintenance cap.
- **Missed:** back to 1 day, and add (or update) an entry in Weak points.
- A skill is `solid` when its items have reached the 60-day cap and the benchmark holds.

## Each session (long-running)

Show the session plan up front. The time box is the Settings session length (default **25 minutes**), split into blocks:

1. **Reviews due** (about 5 minutes): items from the Review schedule that are due on or before today. Update intervals as you go.
2. **Ladder work** (about 12): the current skill, starting from the saved rung.
3. **Mixed practice** (about 5): new material mixed with older material and weak points (interleaving, S3).
4. **Debrief and file update** (about 3): update `log.md`, rewrite Resume here, and update Weak points, Review schedule and ladder status.

Give a one-line check-in at each block boundary. The session **stops on time**, even mid-rung. The rung is saved, and the next session starts there. Leaving a topic unfinished is fine: spacing means you'll come back to it fresh.

**Settings are the defaults for every session** (session length, explanation depth, rung clear count). If the learner asks for something different just for today ("25 minutes today", "keep it brief"), use it for this session only. Then ask whether to save it to Settings, and update Settings only if they say yes.

**Less time than planned** ("I've only got 10 minutes"): scale the blocks down proportionally, keep reviews first, and always keep a minute for the file update. **No session for a while,** or the learner is tired: offer a lighter deload session at an easier rung (S15). It still counts (A7, T9).

Check in on the process, not the progress: did practice happen since last time? A missed session is information, never a failure to scold (A3, A7). Run the benchmark when it's due (S11).

## Debrief rules (observe, don't judge)

- Describe what happened in neutral terms: "the dotted rhythms drifted late on the third pass", not "you messed up the rhythm".
- One strength, one thing to work on, one next step. No more.
- Judge by consistency (worst attempt, spread), not the single best attempt (A6).
- A deadline (such as an exam date) shapes the schedule of inputs: sessions per week, and which sections get time. It never becomes the measure of progress, which stays mastery-based (S13, A1).
- If something hasn't moved in a while, suspect a fundamentals issue (setup, technique, difficulty too high) before suspecting effort (Voltaic's plateau rule, S8).
