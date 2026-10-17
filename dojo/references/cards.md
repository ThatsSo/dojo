# Cards

Flashcards serve the **Automate** stage: retrieval (S4) plus spacing (S7). They keep understanding; they don't create it (S5).

## Before writing any cards

- The material is **understood**. If it isn't, explain it, have the learner try it or teach it back, then make the cards.
- The material is **worth remembering long-term**. A rule of thumb: card it if you'd otherwise spend more than about five minutes over your life looking it up.

## Card-writing rules

1. **One fact per card** (minimum information). Split lists and multi-part answers into separate cards, or use cloze-style fronts.
2. **Recall, not recognition.** Ask "What does X do?", not "Is X involved in Y?". No true/false or yes/no cards.
3. **Context on the card.** Include a short cue, an example sentence, or what it's for, so the card also works in real use (S2), not only in the deck.
4. **Both directions only when both are useful** (vocabulary: word → meaning *and* meaning → word). `study.html` has a Swap mode that keeps a separate schedule for each direction, so for that app write one direction and let Swap handle the other. For Anki, use `--reverse`.
5. **Cloze-style fronts** for facts that belong in a sentence: `The spacing effect: reviews spread out beat ___ reviews` → `massed (crammed)`.
6. **Keep the back short.** One line ideally, with a second line for an example or reason if needed.
7. **Wording is neutral and exact.** No trick questions. The card tests knowledge, not reading skill.

## The CSV format (James's `study.html` app)

- UTF-8, **no BOM**.
- Exactly **2 columns**: front, back, with no header row.
- Standard CSV quoting: a field containing a comma, double quote or line break is wrapped in `"…"`, with inner quotes doubled (`""`).
- `**bold**` renders as bold, but only within one line. Line breaks inside a quoted field render as line breaks.
- Fields are trimmed.
- **Quirk:** if the **first** row's front contains "question" and its back contains "answer" (any case), the app treats it as a header and skips it. Reword that card or move it down.

Example:

```
"What does the spacing effect say?","Reviews **spread out** over time beat the same reviews crammed together"
"¿Cómo se dice ""to practise""?",practicar
```

## Workflow

1. Write the cards as `(front, back)` pairs following the rules above.
2. Save the pairs as a JSON file (`rows.json`, a list of `[front, back]` pairs, written with your file-writing tool), then convert it. The helper does the CSV quoting and validates in the same step:

   ```bash
   python "<skill>/scripts/cards_csv.py" --from-json rows.json deck.csv
   ```

   Or write the CSV directly using the format above and validate it (step 3).
3. Validate until it prints `OK`:

   ```bash
   python "<skill>/scripts/cards_csv.py" deck.csv
   ```

   It reports wrong column counts, empty fields, the header quirk, duplicates and empty decks. Row numbers count CSV records, so a quoted multi-line card counts as one row.
4. Optional, for an Anki package:

   ```bash
   python "<skill>/scripts/csv_to_apkg.py" deck.csv "Deck Name" [--reverse] [-o deck.apkg]
   ```

   This needs `pip install genanki`; the script prints that instruction if it's missing.
   - **Re-importing:** deck IDs come from the deck name and note IDs from the deck name plus the card front. Re-importing an edited deck therefore updates cards whose *back* changed. A card whose *front* changed arrives as a new card; delete the old one in Anki.
   - **Pick `--reverse` once per deck:** switching it later changes the note type.

`<skill>` is this skill's folder, as an absolute path. On James's machine that's `C:\Users\James\.claude\skills\dojo`; elsewhere, expand `~/.claude/skills/dojo`.

## Where decks go

- **For an app:** the project's own card folder. Read the project's AGENTS.md or CLAUDE.md first. For James's website, the live Study app is `Website/site/study/`: decks go in `site/study/cards/`, and the deck index is rebuilt with `python tools/build_deck_index.py`. `Website/Neocities/` is a read-only archive; never write there.
- **For coach mode:** `Documents\Learning\<subject>\cards\`.

## When auditing a card system

Judge it against S4, S5, S7 and A1–A3 *for the learner's goal*. Fixed short intervals suit short-term exam prep and are wrong for lifelong retention. Retiring "mastered" cards forever trades away maintenance. A grading scale with no "forgot" option treats a complete blank and a slow recall the same. See `audit.md`.
