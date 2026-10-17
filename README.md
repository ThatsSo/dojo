# Dojo

A [Claude Code](https://claude.com/claude-code) skill for designing, auditing and practising learning, built on one coherent pedagogy:

> **A rigorous plan, done with a Zen attitude.**

Modern learning research decides the *structure*: what to practise, when, and at what difficulty. Zen decides the *attitude*: how to be while practising. The idea that unifies them is an arc in which explicit knowledge becomes implicit skill: **Map → Acquire → Automate → Perform → Review**. Each stage has its own methods and its own right attitude.

## Modes

| Mode | Use it for |
|---|---|
| **Design** | Shaping a new learning app, feature, course or practice system |
| **Audit** | Judging an existing one *conceptually*, against the learner's goal, with ranked findings and fixes |
| **Lens** | Light, never-blocking checks during feature work in projects that opt in (`Dojo lens: on. Check learning-facing features against the dojo skill.` in `CLAUDE.md` or `HANDOFF.md`) |
| **Coach** | Learning something yourself, one session at a time or as a long-running subject with a plan, a log, decks and problem sets |

Plus three tools:
- **Card generation:** CSV, plus Anki `.apkg` export.
- **Woodpecker sets:** repeated problem sets with time limits that halve each cycle.
- **Benchmarks:** fixed tests that measure without becoming the training.

Dojo triggers on teaching and learning work, and on `/dojo` or "dojo this". It deliberately does **not** turn ordinary questions into lessons.

## Install

Clone the repo, then link or copy the `dojo/` folder into your personal skills folder.

Windows (a junction, so edits are picked up live; no admin rights needed):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\dojo" -Target "<repo>\dojo"
```

macOS or Linux:

```bash
ln -s "<repo>/dojo" ~/.claude/skills/dojo
```

## Configuration

Coach mode keeps long-running subjects in a learning folder, `~/Documents/Learning` by default. To use another place, set `DOJO_LEARNING_DIR`, or create `~/.claude/dojo.json`:

```json
{"learning_dir": "D:/Notes/Learning"}
```

`python dojo/scripts/dojo_config.py` prints the folder Dojo will use.

## Card tooling

```bash
python dojo/scripts/cards_csv.py deck.csv                              # validate
python dojo/scripts/cards_csv.py --from-json rows.json deck.csv        # write + validate
python dojo/scripts/csv_to_apkg.py deck.csv "Deck Name" --reverse      # Anki package (pip install genanki)
```

Card CSVs are UTF-8 with two columns (front, back) and no header row, using standard quoting. `**bold**` and line breaks are allowed. See `dojo/references/cards.md`.

## What's inside

```
dojo/
  SKILL.md                 thesis, triggers, mode routing
  references/principles.md the model: arc, S1–S14 structure, A1–A7 attitude
  references/tensions.md   ten apparent conflicts and how they resolve
  references/sources.md    source summaries + evidence corrections
  references/design.md     design workflow + knowledge-type table
  references/audit.md      audit workflow + report template
  references/lens.md       six-question lens
  references/coach.md      coaching flow + subject-folder templates
  references/cards.md      card rules + format
  references/woodpecker.md Woodpecker sets + benchmarks
  scripts/                 cards_csv.py, csv_to_apkg.py, dojo_config.py
```

## Development

```bash
pip install -r requirements-dev.txt
python -m pytest tests -q
```

Behavioural evals are in `evals/` (`evals.json` holds the prompts and assertions; `results.md` holds the latest results).

## Sources

The primary voice is the author's (James, a.k.a. ThatsSo) own essays on learning, Zen, flow and implicit vs. explicit learning. Supporting sources:

- *Ultralearning* (Scott H. Young)
- *Zen in the Art of Archery* (Eugen Herrigel)
- *Flow* (Mihaly Csikszentmihalyi)
- Spaced-repetition research and the Anki mindset (Ebbinghaus, Bjork, Woźniak, Nielsen)
- *The Woodpecker Method* (Axel Smith & Hans Tikkanen)
- Voltaic's aim-training guides

Each principle carries an evidence level, and `sources.md` lists where popular claims overreach.
