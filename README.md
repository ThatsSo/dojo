# Dojo

An [Agent Skill](https://agentskills.io) for Claude Code, Codex and ChatGPT, for designing, auditing and practising learning, built on one coherent pedagogy:

> **A rigorous plan, done with a Zen attitude.**

Modern learning research decides the *structure*: what to practise, when, and at what difficulty. Zen decides the *attitude*: how to be while practising. The idea that unifies them is an arc in which explicit knowledge becomes implicit skill: **Map → Acquire → Automate → Perform → Review**. Each stage has its own methods and its own right attitude.

## Modes

| Mode | Use it for |
|---|---|
| **Design** | Shaping a new learning app, feature, course or practice system |
| **Audit** | Judging an existing one *conceptually*, against the learner's goal, with ranked findings and fixes |
| **Lens** | Light, never-blocking checks during feature work in projects that opt in (`Dojo lens: on. Check learning-facing features against the dojo skill.` in `AGENTS.md`, `CLAUDE.md` or `HANDOFF.md`) |
| **Coach** | Learning something yourself, one session at a time or as a long-running subject with a plan, a log, decks and problem sets |

Plus three tools:
- **Card generation:** CSV, plus Anki `.apkg` export.
- **Woodpecker sets:** repeated problem sets with time limits that halve each cycle.
- **Benchmarks:** fixed tests that measure without becoming the training.

Dojo triggers on teaching and learning work, and on `/dojo` (Claude Code), `$dojo` (Codex), `@dojo` (ChatGPT) or "dojo this". It deliberately does **not** turn ordinary questions into lessons.

## Install

Clone the repo, then link the `dojo/` folder into each tool's skills folder. A link (rather than a copy) means every tool picks up edits to the repo straight away.

### Claude Code

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\dojo" -Target "<repo>\dojo"
```

macOS or Linux: `ln -s "<repo>/dojo" ~/.claude/skills/dojo`

### Codex (app and CLI)

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\skills\dojo" -Target "<repo>\dojo"
```

macOS or Linux: `ln -s "<repo>/dojo" ~/.codex/skills/dojo`. Restart Codex, then call it with `$dojo` or just describe the task. `dojo/agents/openai.yaml` gives it a name and starter prompt in Codex's skill list.

### ChatGPT

Build the upload files:

```bash
python tools/package_chatgpt.py
```

This writes `dist/dojo-skill.zip` and `dist/chatgpt-project/`.

- **If your ChatGPT has Skills** (Settings → Skills, or "Build me a skill…" in a chat): upload `dist/dojo-skill.zip` and turn it on. Use it with `@dojo`, or let ChatGPT pick it up automatically. Skills don't sync between products, so re-upload after changes.
- **Otherwise, use a Project or Custom GPT:** paste `dist/chatgpt-project/instructions.md` into the instructions, and upload every file in `dist/chatgpt-project/knowledge/` as a knowledge file.

ChatGPT can't see your files or run Dojo's scripts. It audits what you paste or upload, keeps coach plans in the chat or project, and writes flashcard CSVs directly.

## Configuration

Coach mode keeps long-running subjects in a learning folder, `~/Documents/Learning` by default. To use another place, set `DOJO_LEARNING_DIR`, or create `~/.dojo.json` (read by every tool; `~/.claude/dojo.json` and `~/.codex/dojo.json` also work):

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
  agents/openai.yaml       Codex display name and starter prompt
chatgpt/                   instructions for the ChatGPT Project / Custom GPT version
tools/package_chatgpt.py   builds the ChatGPT upload files into dist/
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
