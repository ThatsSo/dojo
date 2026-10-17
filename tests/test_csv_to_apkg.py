import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "dojo" / "scripts"))

from csv_to_apkg import build_package, card_html, stable_id  # noqa: E402


def test_card_html():
    assert card_html("**hi** <b>\nx") == "<b>hi</b> &lt;b&gt;<br>x"
    assert card_html("**a\nb**") == "**a<br>b**"  # no bold across lines, like study.html


def test_stable_id():
    assert stable_id("Spanish") == stable_id("Spanish") != stable_id("French")
    assert (1 << 30) <= stable_id("Spanish") < (1 << 31)


def test_build_package_writes_loadable_zip(tmp_path):
    pkg = build_package([("q1", "a1"), ("q2", "a2")], "Test Deck", reverse=True)
    out = tmp_path / "t.apkg"
    pkg.write_to_file(out)
    assert zipfile.is_zipfile(out)
    deck = pkg.decks[0]
    assert len(deck.notes) == 2 and len(deck.notes[0].model.templates) == 2
