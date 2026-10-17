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


def test_edited_back_keeps_same_note_guid():
    a = build_package([("q", "a")], "Deck").decks[0].notes[0].guid
    b = build_package([("q", "a2")], "Deck").decks[0].notes[0].guid
    assert a == b


def test_cli_survives_non_ascii_path_on_cp1252_stdout(tmp_path):
    import os
    import subprocess
    src = tmp_path / "日本.csv"
    src.write_text("犬,dog\n", encoding="utf-8")
    script = Path(__file__).resolve().parent.parent / "dojo" / "scripts" / "csv_to_apkg.py"
    env = dict(os.environ, PYTHONIOENCODING="cp1252")
    r = subprocess.run([sys.executable, str(script), str(src), "日本語"], env=env,
                       capture_output=True)
    assert r.returncode == 0, r.stderr.decode(errors="replace")
