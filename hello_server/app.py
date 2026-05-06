"""FastAPI application for the hello server."""

import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Final

from fastapi import FastAPI

_REPO_ROOT: Final[Path] = Path(__file__).resolve().parent.parent


def _resolve_commit_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:  # pragma: no cover
        return "unknown"

    commit = result.stdout.strip()
    if result.returncode != 0 or not commit:  # pragma: no cover
        return "unknown"

    return commit[:7]


_STARTED_AT: Final[str] = datetime.now(timezone.utc).isoformat()
_COMMIT_SHA: Final[str] = _resolve_commit_sha()

app = FastAPI(title="Hello Server")


@app.get("/hello")
def hello() -> str:
    """Return the hello response."""
    return "world"


@app.get("/v3-smoke")
def v3_smoke() -> dict[str, str]:
    """Return v3 deployment smoke-test metadata."""
    return {"v3": "ok", "started_at": _STARTED_AT, "commit": _COMMIT_SHA}
