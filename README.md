# Prowl

[![CICD Status](https://img.shields.io/github/actions/workflow/status/nxthdr/prowl/cicd.yml?logo=github&label=cicd)](https://github.com/nxthdr/prowl/actions/workflows/cicd.yml)
[![PyPI](https://img.shields.io/pypi/v/prowl?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/prowl/)

Library to generate [caracal](https://github.com/dioptra-io/caracal) / [caracat](https://github.com/maxmouchet/caracat) probes. Also intended to be used with [saimiris](https://github.com/nxthdr/saimiris).

To use it as a standalone library, you can install it without any extra:

```bash
pip install prowl
```

## CLI Usage

To be able to use the CLI app, you need to install it with the `cli` extra.

```bash
pip install prowl[cli]
```

The CLI generates probes based on a "targets" file. A target is defined as:

```
target,protocol,min_ttl,max_ttl,n_flows
```

where the target is a IPv4/IPv6 prefix or IPv4/IPv6 address. The prococol can be icmp, icmp6 or udp.


To use it, you can use the `prowl` command:

```bash
python -m prowl --help
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) as package and project manager.

### Setup

Install the project with all extras and the dev dependency group:

```bash
uv sync --all-extras --dev
```

This installs the library, the CLI extra (`typer`), and dev tools (`pytest`, `ruff`, `bump-my-version`).

### Running the CLI

```bash
uv run -m prowl --help
```

### Testing

```bash
uv run pytest
```

### Linting

```bash
uv run ruff check .
uv run ruff format .
```

### Dependency Groups

The project has two dependency groups:

- **test**: `pytest` and `ruff`. Used by CI to run tests without installing heavy dev tools.
- **dev**: includes `test` plus `bump-my-version` and `pydantic`. Used for local development and releasing.

CI runs `uv sync --all-extras --no-dev --group test` to avoid installing `bump-my-version` (which pulls `pydantic-core`, a native Rust extension). This keeps CI fast and avoids Python version compatibility issues with PyO3.

### Bumping a Version

Version bumping is handled by [bump-my-version](https://github.com/callowayproject/bump-my-version). It updates the version in `pyproject.toml` and `prowl/__init__.py`, creates a commit, and tags it.

```bash
# Patch release (e.g. 0.3.0 -> 0.3.1)
uv run bump-my-version bump patch

# Minor release (e.g. 0.3.0 -> 0.4.0)
uv run bump-my-version bump minor

# Major release (e.g. 0.3.0 -> 1.0.0)
uv run bump-my-version bump major
```

Then push the commit and tag:

```bash
git push && git push --tags
```

The configuration lives in `.bumpversion.toml`.

### Docker

Build the Docker image locally:

```bash
docker build -t prowl .
docker run prowl --help
```

### Updating the Lockfile

After changing dependencies in `pyproject.toml`, regenerate the lockfile:

```bash
uv lock
```

To upgrade all dependencies to their latest compatible versions:

```bash
uv lock --upgrade
```
