# andrew_utils
python utils

## Install

```
pip install andrew-utils --index-url https://andrewtheguy.github.io/andrew_utils/simple/
```

## Develop

```
uv sync --group test
uv run pytest
```

## Release

Bump `version` in `pyproject.toml`, commit to `main`, then run the **Release** workflow via `Actions` → `Release` → `Run workflow`. It tags the version, builds the wheel + sdist, creates a GitHub Release, and refreshes the PEP 503 index at the URL above.
