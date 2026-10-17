import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "dojo" / "scripts"))

from cards_csv import parse_csv, to_csv, validate, write_csv  # noqa: E402


def test_parse_quotes_commas_newlines():
    assert parse_csv('a,b\n"x, y","l1\nl2"\n') == [("a", "b"), ("x, y", "l1\nl2")]


def test_parse_escaped_quotes():
    assert parse_csv('"say ""hi""",b') == [('say "hi"', "b")]


def test_parse_crlf_matches_lf():
    assert parse_csv("a,b\r\nc,d\r\n") == parse_csv("a,b\nc,d\n") == [("a", "b"), ("c", "d")]


def test_parse_skips_headerish_first_row():
    assert parse_csv("Question,Answer\nq,a") == [("q", "a")]


def test_roundtrip_including_unicode_and_bold():
    rows = [("¿Qué es, ñ?", 'He said "hi"\n**bold**'), ("日本語", "a,b")]
    assert parse_csv(to_csv(rows)) == rows


def test_write_csv_utf8_no_bom(tmp_path):
    p = tmp_path / "d.csv"
    write_csv([("ñ", "x")], p)
    raw = p.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf") and "ñ".encode() in raw


def test_validate_flags_problems():
    assert any("header" in e for e in validate("Which question?,The answer\nq,a"))
    assert any("3 columns" in e for e in validate("a,b,c\n"))
    assert any("empty" in e for e in validate("a,\n"))
    assert any("duplicate" in e for e in validate("a,b\na,b\n"))
    assert validate("\n\n") == ["no cards"]
    assert validate("a,b\n") == []
