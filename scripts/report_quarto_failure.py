"""Publish a concise Quarto render error as a GitHub commit status."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen


def failure_description(log: str) -> str:
    """Extract the last rendered document and final useful error from a log."""
    documents = re.findall(r"\[\s*\d+/\d+\]\s+([^\r\n]+)", log)
    error_lines = re.findall(
        r"^(?:[A-Za-z_][\w.]*(?:Error|Exception): .+|ERROR: .+)$",
        log,
        flags=re.MULTILINE,
    )

    document = documents[-1].strip() if documents else "Quarto render"
    if error_lines:
        error = error_lines[-1].strip()
    else:
        nonempty_lines = [line.strip() for line in log.splitlines() if line.strip()]
        error = nonempty_lines[-1] if nonempty_lines else "failed without log output"

    description = f"{document}: {error}"
    return description[:140]


def main() -> None:
    log_path = Path(sys.argv[1])
    description = failure_description(log_path.read_text(encoding="utf-8", errors="replace"))

    repository = os.environ["GITHUB_REPOSITORY"]
    sha = os.environ["GITHUB_SHA"]
    run_id = os.environ["GITHUB_RUN_ID"]
    token = os.environ["GITHUB_TOKEN"]

    payload = json.dumps(
        {
            "state": "failure",
            "context": "quarto/render-error",
            "description": description,
            "target_url": f"https://github.com/{repository}/actions/runs/{run_id}",
        }
    ).encode()
    request = Request(
        f"https://api.github.com/repos/{repository}/statuses/{sha}",
        data=payload,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )
    with urlopen(request, timeout=30) as response:
        if response.status != 201:
            raise RuntimeError(f"GitHub returned HTTP {response.status}")

    print(f"Reported render failure: {description}")


if __name__ == "__main__":
    main()
