# civic-lib-geo

> Shared gis library for Civic Interconnect

[![Version](https://img.shields.io/badge/version-0.2.1-blue)](https://github.com/civic-interconnect/civic-lib-geo/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/civic-interconnect/civic-lib-geo/actions/workflows/tests.yml/badge.svg)](https://github.com/civic-interconnect/civic-lib-geo/actions/workflows/tests.yml)

## Local Development

See [REF_DEV.md](./REF_DEV.md). Then:

```shell
py scripts/main.py
```


## Build and Publish to PyPi

The last command requires a PyPi API token to publish.

```powershell
py -m pip install --upgrade build twine
py -m build
py -m twine upload dist/*
```
