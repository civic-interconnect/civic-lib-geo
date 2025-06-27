# DEVELOPER.md

## Setup for Libraries

1. Fork the repo.
2. Clone your fork and open it in VS Code.
3. Open a terminal (examples below use PowerShell on Windows).

```powershell
git clone https://github.com/civic-interconnect/civic-lib-geo.git
cd civic-lib-geo

py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel --prefer-binary
py -m pip install --upgrade -e .[dev]

civic-dev prep-code        # repeat if needed
civic-dev publish-api
mkdocs serve
```

Visit local API docs at: <http://localhost:8000>

## Releasing New Version

Before publishing a new version, delete .venv. and recreate and activate.
Run pre-release preparation, installing and upgrading without the -e editable flag.
Verify all tests pass. Run prep-code (twice if needed).
Verify the docs are generated and appear correctly.

```powershell
git pull
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel --prefer-binary
py -m pip install --upgrade .[dev]
pytest tests
civic-dev prep-code
civic-dev publish-api
mkdocs serve
```

After verifying changes:

```powershell
civic-dev bump-version 0.2.3 0.2.4
civic-dev release
```

## Publishing Library to PyPI

Requires a valid PyPI token set in your environment or `~/.pypirc`.

```powershell
py -m build
py -m twine upload dist/*
```
