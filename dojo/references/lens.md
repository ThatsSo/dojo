# Lens mode

A light, ongoing check during normal feature work in projects that opt in. It's the cheapest Dojo mode: no reports, no ceremony.

## Opt-in

A project turns the lens on with this line in its `CLAUDE.md` or `HANDOFF.md`:

```
Dojo lens: on. Check learning-facing features against the dojo skill.
```

Without that line, lens mode doesn't run. Design and Audit still run when asked for explicitly.

## When it applies

Only to **learner-facing** work: anything that changes what the learner practises, sees, is scored on, or how they progress. Skip refactors, build tooling, file importers and pure bug fixes, unless the fix changes learner-facing behaviour.

## The six questions

Before finishing a learner-facing change, ask:

1. **Which arc stage does this serve** (Map, Acquire, Automate, Perform, Review), and does it follow that stage's rules? (Arc, T2)
2. **Does it keep difficulty in the goldilocks zone and respect the difficulty budget?** It shouldn't raise several variables at once or push speed ahead of accuracy. (S8, S9, S10)
3. **Is feedback fast, informative and non-punitive?** (S6, A3)
4. **Are mistakes handled right for the zone?** Fix them on the spot in drills; notice, log and keep going in run-throughs. (A3, T2)
5. **Does it measure without training on the test, and avoid rewarding exploits?** (S11, T10)
6. **Do its metrics and wording put process before progress,** with goals the learner owns and no guilt mechanics? (A1, A2, A6)

## Output rules

- **Report only real concerns.** If all six questions are fine, say nothing about the lens.
- **At most about five lines,** in the agent's normal final report, under a "Dojo lens" heading. Each line gives the concern, the concept in words (one short clause, e.g. "punishing a missed day turns a habit into a guilt trip"), the principle ID, and the smallest fix. Lens notes are suggestions; never apply them without the user's go-ahead.
- **Never block work.** A concern is advice. The feature ships as the user asked unless they choose otherwise.
- **Never re-argue recorded decisions.** If a concern touches a decision in HANDOFF.md or DECISIONS.md, either skip it or mention it once as a known trade-off.
- **Bigger issues** (a concern that touches the app's core loop) get one line suggesting a Dojo audit or design pass, not an essay.
