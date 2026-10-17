"""Resolve where Dojo's coach mode keeps long-running subject folders.

Precedence:
  1. DOJO_LEARNING_DIR environment variable
  2. "learning_dir" in ~/.claude/dojo.json
  3. ~/Documents/Learning (default)

CLI: python dojo_config.py   -> prints the resolved folder.
"""
import json
import os
import sys
from pathlib import Path


def _expand(value: str, home: Path) -> Path:
    if value == "~" or value.startswith(("~/", "~\\")):
        return home / value[2:]
    return Path(value)


def learning_dir(env=None, home=None) -> Path:
    env = os.environ if env is None else env
    home = Path.home() if home is None else Path(home)
    if env.get("DOJO_LEARNING_DIR"):
        return _expand(env["DOJO_LEARNING_DIR"], home)
    config = home / ".claude" / "dojo.json"
    try:
        value = json.loads(config.read_text(encoding="utf-8")).get("learning_dir")
        if value:
            return _expand(value, home)
    except (OSError, ValueError, AttributeError):
        pass
    return home / "Documents" / "Learning"


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")
    print(learning_dir())
