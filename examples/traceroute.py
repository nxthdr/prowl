"""
Example of how to use the Traceroute tool to perform a traceroute to a target prefix.

---
Source Port: 24000
Destination Port: 33434
---
Mapper: Sequential
---
Prefix: 1.1.1.0/24
Protocol: ICMP
Min TTL: 1
Max TTL: 30
Number of initial flows: 6
"""

from ipaddress import ip_network

from prowl.mappers import SequentialFlowMapper
from prowl.models import Protocol, Target
from prowl.tools import traceroute

if __name__ == "__main__":

    src_port, dst_port = 24000, 33434
    mapper = SequentialFlowMapper()
    targets = [
        Target(
            prefix=ip_network("1.1.1.0/24"),
            protocol=Protocol.ICMP,
            min_ttl=1,
            max_ttl=30,
            n_intitial_flows=6,
        )
    ]

    probes = traceroute(targets, mapper, src_port, dst_port)
    for probe in probes:
        print(probe)
