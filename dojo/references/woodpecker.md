# Woodpecker sets and benchmarks

Two tools for the Automate and Review stages: **Woodpecker sets** turn known patterns into instant recognition, and **benchmarks** measure skill without becoming the training.

## Woodpecker sets

### When to offer one (by name)
Apply the repetition-target rule (**S12**): offer a Woodpecker set **only when the patterns in the set *are* the skill**. Name it ("this is a good fit for a Woodpecker set"), and only inside a Dojo mode, never in reply to an ordinary question.

| Good fit (the patterns are the skill) | Poor fit (the set stands in for a general skill; vary it instead) |
|---|---|
| Chess tactics and motifs | Sight-reading new music |
| Chord shapes and inversions, intervals by ear | Aim against unpredictable targets |
| Grammar patterns, verb conjugation tables | Reading comprehension of new texts |
| Code idioms, keyboard shortcuts, regex patterns | Open-ended problem solving, writing |
| Mental-math tricks, standard proofs | Conversation |

### Building the set
- **Size:** big enough to hold the important patterns, small enough to cycle. In chess that's hundreds of problems; elsewhere 30–150 is typical.
- **Difficulty:** most items should be *solvable with effort* on the first cycle. If many are failed, the set is too hard and will be memorized instead of understood (S8).
- **Every item has a full solution:** the answer *and* why it works (the key idea, the main lines, the rule it follows).
- **Mix the patterns** across the set rather than grouping by type (interleaving), unless this is the very first introduction.

### The cycle schedule
1. **Cycle 1 (slow and careful, in the learning zone):** solve everything, working out the full solution. Check it, and study every miss until it's understood (S9: accuracy first).
2. **Rest** a day or two.
3. **Each later cycle:** the whole set again in about **half the time** of the previous cycle (halving), ideally down to 6–7 cycles. If halving is impossible, extend a little but keep the pressure on; compressing time is the point, **as long as accuracy holds** (T1, S9). If accuracy drops, repeat the cycle at the same time limit before halving again.
4. **Every re-solve must reproduce *why* the solution works,** not just recall the answer. Recalling "the answer was Nxf7" without seeing the idea doesn't count as solved.
5. After the last cycle, move the most-missed items into spaced review (cards, S7) to maintain them.

Shrinking intervals are deliberate: this builds speed and automaticity, not long-term retention. That's why maintenance happens afterwards through spacing.

### Files (in coach mode: `woodpecker/<set>/`)

`set.md`:

```markdown
# <Set name>
Patterns covered: <list>   Cycle 1 target: <time>

## 1
<problem>
**Solution:** <answer>
**Why:** <key idea / rule / main lines>

## 2
…
```

`cycles.md`:

```markdown
| Cycle | Started | Time limit | Time taken | Accuracy | Misses (item #s) |
|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | none (careful) | | | |
| 2 | | half of cycle 1 | | | |
```

Misses from each cycle are studied (learning zone) before the next cycle starts.

### In an app
- A "Woodpecker mode" over a fixed item pool, with a whole-set timer, a target that halves each cycle, and a per-item accuracy record.
- The target tightens only while accuracy holds (T1).
- Solutions show the *why*.
- Example: Piaano's Pattern Trainer chord pool; `study.html`'s Cycle mode plus a timer and a cycle log.

## Benchmarks

Benchmarks measure; they don't train (**S11**, T10).

- **A fixed, low-noise set per category** from the skill map: the same items every time, with randomness removed where possible, separate from the practice material.
- **Cadence:** **weekly** by default, never daily. Take it in a normal state (not exhausted, not right after a heavy drill of the same thing).
- **Several runs averaged** (3–10 depending on length). Record the average, the **worst day** or worst run, and the spread between best and worst.
- **Read results as information** (A6): the goal is to raise your worst day and narrow the spread. Results never decide self-worth, and never become the daily practice.
- **Progression:** passing a level's benchmark is what unlocks the next level's practice (S13), not time spent.
- **A plateau** across several benchmarks suggests a fundamentals problem (setup, technique, difficulty too high), not too little effort.

### Benchmark file (coach mode: inside `plan.md` under `## Benchmark`, results in `log.md`)

```markdown
| Date | Category | Runs | Average | Worst | Spread | Note |
|---|---|---|---|---|---|---|
```
