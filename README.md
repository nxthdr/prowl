# Prowl

[![Tests Status](https://img.shields.io/github/actions/workflow/status/nxthdr/prowl/tests.yml?logo=github&label=tests)](https://github.com/nxthdr/prowl/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/prowl?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/prowl/)

> [!WARNING]
> Currently in early-stage development.

Library to generate [caracal](https://github.com/dioptra-io/caracal) / [caracat](https://github.com/maxmouchet/caracat) probes. Also intended to be used with [saimiris](https://github.com/nxthdr/saimiris).

To use it as a standalone library, you can install it without any extra:

```bash
pip install prowl
```

## CLI Usage

To be able to use the CLI app, you need to install it with the `cli` extra:

```bash
pip install prowl[cli]
```

Then you can use the `prowl` command:

```bash
python -m prowl --help
```

## Development

This projects use [uv](https://github.com/astral-sh/uv) as package and project manager.

Once uv installed, you can run the CLI app:

```bash
uv run -m prowl
```
