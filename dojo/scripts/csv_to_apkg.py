"""Convert a Dojo flashcard CSV into an Anki package (.apkg).

CLI: python csv_to_apkg.py deck.csv "Deck Name" [--reverse] [-o out.apkg]

IDs come from a hash of the deck name, so re-importing the same deck
updates it instead of duplicating it. Needs `pip install genanki`.
"""
import argparse
import hashlib
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards_csv import parse_csv  # noqa: E402

CSS = ".card { font-family: system-ui, sans-serif; font-size: 22px; text-align: center; }"


def card_html(text: str) -> str:
    """Escape HTML, then render **bold** (single line only) and line breaks, like study.html."""
    h = html.escape(text, quote=True).replace("&#x27;", "&#39;")
    h = re.sub(r"\*\*([^*\n]+)\*\*", r"<b>\1</b>", h)
    return re.sub(r"\r\n|\r|\n", "<br>", h)


def stable_id(name: str) -> int:
    n = int.from_bytes(hashlib.sha1(name.encode("utf-8")).digest()[:8], "big")
    return (1 << 30) + n % (1 << 30)


def build_package(rows, deck_name: str, reverse: bool = False):
    import genanki

    templates = [{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
    }]
    kind = "basic"
    if reverse:
        kind = "basic-reversed"
        templates.append({
            "name": "Card 2",
            "qfmt": "{{Back}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Front}}",
        })
    model = genanki.Model(
        stable_id("dojo-model-" + kind),
        "Dojo Basic+Reversed" if reverse else "Dojo Basic",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=templates,
        css=CSS,
    )
    deck = genanki.Deck(stable_id(deck_name), deck_name)
    for front, back in rows:
        # GUID keyed on deck + front, so fixing a card's back updates it on re-import.
        deck.add_note(genanki.Note(model=model, fields=[card_html(front), card_html(back)],
                                   guid=genanki.guid_for(deck_name, front)))
    return genanki.Package(deck)


def main(argv=None) -> int:
    sys.stdout.reconfigure(errors="replace")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("csv")
    p.add_argument("deck_name")
    p.add_argument("--reverse", action="store_true", help="also make back-to-front cards")
    p.add_argument("-o", "--output", help="output path (default: <csv name>.apkg)")
    args = p.parse_args(argv)
    try:
        import genanki  # noqa: F401
    except ImportError:
        print("genanki is not installed. Run: pip install genanki")
        return 2
    rows = parse_csv(Path(args.csv).read_text(encoding="utf-8-sig"))
    if not rows:
        print("no cards")
        return 1
    out = Path(args.output) if args.output else Path(args.csv).with_suffix(".apkg")
    build_package(rows, args.deck_name, args.reverse).write_to_file(str(out))
    print(f"Wrote {len(rows)} notes to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
