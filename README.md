# civic-lib-gis

> Shared gis library for Civic Interconnect

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/civic-interconnect/civic-lib-gis/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/civic-interconnect/civic-lib-gis/actions/workflows/tests.yml/badge.svg)](https://github.com/civic-interconnect/civic-lib-gis/actions/workflows/tests.yml)

## Local Development (of this library)

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel --prefer-binary
py -m pip install --upgrade -r requirements-dev.txt --timeout 100
pre-commit install
pytest tests
```

## Before Starting Changes

```shell
git pull
```

## After Tested Changes (New Version Release)

```powershell
.\.venv\Scripts\activate
ruff check . --fix
pytest tests
py bump_version.py 0.1.0 0.1.0
.\release.ps1 -Version v0.1.0
```

It will update these files to the new version:

1. VERSION file
2. pyproject.toml
3. setup.cfg
4. README.md (badges)

And then run the following:

```shell
pip uninstall civic-lib -y
pip install -e .
pytest
pre-commit autoupdate --repo https://github.com/pre-commit/pre-commit-hooks
ruff check . --fix
git add .
git commit -m "Release: v0.1.0"
git push origin main
git tag v0.1.0
git push origin v0.1.0
```


## Build and Publish to PyPi

The last command requires a PyPi API token to publish.

```powershell
py -m pip install --upgrade build twine
py -m build
py -m twine upload dist/*
```
