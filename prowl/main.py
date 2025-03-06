"""
Main App Entrypoint

Provides CLI interface for the prowl tool.
Requires installing prowl with extra "app" dependencies.
```
pip install prowl[app]
```
"""

import sys
from ipaddress import ip_network
from typing import Callable, Dict

import typer
from typing_extensions import Annotated

from prowl.mappers import (
    IntervalFlowMapper,
    RandomFlowMapper,
    ReverseByteFlowMapper,
    SequentialFlowMapper,
)
from prowl.tools import ping, traceroute
from prowl.types import FlowMapper

from .models import Target

TOOLS: Dict[str, Callable] = {
    "ping": ping,
    "traceroute": traceroute,
}

MAPPER: Dict[str, FlowMapper] = {
    "sequential": SequentialFlowMapper,
    "random": RandomFlowMapper,
    "reverse": ReverseByteFlowMapper,
    "interval": IntervalFlowMapper,
}


def main(
    file: Annotated[typer.FileText, typer.Argument()] = sys.stdin,
    tool: str = "traceroute",
    mapper: str = "sequential",
):
    # Parse the tool argument
    tool = tool.lower()
    if tool not in TOOLS:
        typer.echo(f"Invalid tool: {tool}", err=True)
        raise typer.Exit(code=1)
    tool = TOOLS[tool]

    # Parse the mapper argument
    mapper = mapper.lower()
    if mapper not in MAPPER:
        typer.echo(f"Invalid mapper: {mapper}", err=True)
        raise typer.Exit(code=1)
    mapper = MAPPER[mapper]()

    # Read the input from stdin
    # And format it as a list of Target objects
    targets = []
    for line in file:
        # Parse the input line
        line = line.strip()
        prefix, protocol, min_ttl, max_ttl, n_flows = line.split(",")
        prefix = ip_network(prefix.strip())
        protocol = protocol.strip()
        min_ttl = int(min_ttl.strip())
        max_ttl = int(max_ttl.strip())
        n_flows = int(n_flows.strip())

        target = Target(prefix, protocol, min_ttl, max_ttl, n_flows)
        targets.append(target)

    # Generate the probes using the ping tool
    probes = tool(targets, mapper)

    # Print the probes to stdout
    for probe in probes:
        print(probe)
