import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "dojo" / "scripts"))

from dojo_config import learning_dir  # noqa: E402


def test_default_is_documents_learning(tmp_path):
    assert learning_dir(env={}, home=tmp_path) == tmp_path / "Documents" / "Learning"


def test_config_file_overrides_default(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "dojo.json").write_text(
        json.dumps({"learning_dir": str(tmp_path / "Study")}), encoding="utf-8")
    assert learning_dir(env={}, home=tmp_path) == tmp_path / "Study"


def test_env_var_overrides_config_file(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "dojo.json").write_text('{"learning_dir": "x"}', encoding="utf-8")
    env = {"DOJO_LEARNING_DIR": str(tmp_path / "Env")}
    assert learning_dir(env=env, home=tmp_path) == tmp_path / "Env"


def test_bad_config_file_falls_back_to_default(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "dojo.json").write_text("not json", encoding="utf-8")
    assert learning_dir(env={}, home=tmp_path) == tmp_path / "Documents" / "Learning"


def test_tilde_is_expanded(tmp_path):
    env = {"DOJO_LEARNING_DIR": "~/Notes"}
    assert learning_dir(env=env, home=tmp_path) == tmp_path / "Notes"


def test_neutral_config_file_preferred_over_claude_one(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "dojo.json").write_text('{"learning_dir": "' + str(tmp_path / "Old").replace("\\", "/") + '"}', encoding="utf-8")
    (tmp_path / ".dojo.json").write_text('{"learning_dir": "' + str(tmp_path / "New").replace("\\", "/") + '"}', encoding="utf-8")
    assert learning_dir(env={}, home=tmp_path) == tmp_path / "New"


def test_codex_config_file_is_read(tmp_path):
    (tmp_path / ".codex").mkdir()
    (tmp_path / ".codex" / "dojo.json").write_text('{"learning_dir": "' + str(tmp_path / "Cx").replace("\\", "/") + '"}', encoding="utf-8")
    assert learning_dir(env={}, home=tmp_path) == tmp_path / "Cx"
