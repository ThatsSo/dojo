"""Read, write and validate two-column flashcard CSVs.

The format matches the parser in James's study.html flashcard app:
UTF-8, front then back, no header row, standard CSV quoting. `**bold**` and
line breaks inside quoted fields are rendered by the app.

CLI: python cards_csv.py deck.csv   -> prints problems (exit 1) or "OK: N cards".
"""
import csv
import io
import re
import sys
from pathlib import Path


def _raw_rows(text: str) -> list[list[str]]:
    """Port of study.html's parseCSV state machine, keeping every field."""
    rows, row, field = [], [], ""
    in_quotes = False
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if in_quotes:
            if c == '"':
                if i + 1 < n and text[i + 1] == '"':
                    field += '"'
                    i += 2
                    continue
                in_quotes = False
            else:
                field += c
            i += 1
            continue
        if c == '"':
            in_quotes = True
        elif c == ",":
            row.append(field)
            field = ""
        elif c == "\n":
            row.append(field)
            field = ""
            rows.append(row)
            row = []
        elif c != "\r":
            field += c
        i += 1
    row.append(field)
    if len(row) > 1 or row[0].strip() != "":
        rows.append(row)
    return rows


def _is_headerish(front: str, back: str) -> bool:
    return bool(re.search("question", front, re.I) and re.search("answer", back, re.I))


def parse_csv(text: str) -> list[tuple[str, str]]:
    """Return the cards exactly as study.html would load them."""
    cleaned = []
    for r in _raw_rows(text):
        front = (r[0] if len(r) > 0 else "").strip()
        back = (r[1] if len(r) > 1 else "").strip()
        if front or back:
            cleaned.append((front, back))
    if cleaned and _is_headerish(*cleaned[0]):
        return cleaned[1:]
    return cleaned


def to_csv(rows: list[tuple[str, str]]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    for front, back in rows:
        writer.writerow([front, back])
    return buf.getvalue()


def write_csv(rows: list[tuple[str, str]], path) -> None:
    """Write UTF-8 without a BOM."""
    Path(path).write_text(to_csv(rows), encoding="utf-8", newline="")


def validate(text: str) -> list[str]:
    """Return a list of problems; an empty list means the deck is fine."""
    problems: list[str] = []
    seen: dict[tuple[str, str], int] = {}
    cards = 0
    for num, r in enumerate(_raw_rows(text), start=1):
        if all(f.strip() == "" for f in r):
            continue
        cards += 1
        if len(r) != 2:
            problems.append(f"row {num}: {len(r)} columns (expected 2)")
        front = r[0].strip()
        back = (r[1] if len(r) > 1 else "").strip()
        if not front:
            problems.append(f"row {num}: empty front")
        if not back:
            problems.append(f"row {num}: empty back")
        if cards == 1 and _is_headerish(front, back):
            problems.append(
                f"row {num}: front contains 'question' and back contains 'answer'; "
                "study.html will skip it as a header"
            )
        key = (front, back)
        if key in seen:
            problems.append(f"row {num}: duplicate of row {seen[key]}")
        else:
            seen[key] = num
    if cards == 0:
        return ["no cards"]
    return problems


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python cards_csv.py deck.csv")
        return 2
    text = Path(argv[1]).read_text(encoding="utf-8-sig")
    problems = validate(text)
    for p in problems:
        print(p)
    if problems:
        return 1
    print(f"OK: {len(parse_csv(text))} cards")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
