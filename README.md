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

This projects use [uv](https://github.com/astral-sh/uv) as package and project manager.

Once uv installed, you can run the CLI app:

```bash
uv run -m prowl
```
