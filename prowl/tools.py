from ipaddress import ip_address
from typing import List

from prowl.defaults import DEFAULT_PROBE_DST_PORT, DEFAULT_PROBE_SRC_PORT
from prowl.models import Probe, Target
from prowl.types import FlowMapper


def ping(
    targets: List[Target],
    mapper: FlowMapper,
    probe_src_port: int = DEFAULT_PROBE_SRC_PORT,
    probe_dst_port: int = DEFAULT_PROBE_DST_PORT,
) -> List[Probe]:
    """
    Generates a list of probes for a set of targets using the given flow mapper.
    Replicates the behavior of the Traceroute tool.

    The `max_ttl` attribute of the target is used as the TTL for all probes.
    The `min_ttl` attribute is not used.

    Returns a list of probes.
    """
    probes = []
    for target in targets:
        dst_prefix_int = int(target.prefix.network_address)
        for flow_id in range(target.n_flows):
            addr_offset, port_offset = mapper.offset(flow_id, dst_prefix_int)
            dst_addr = dst_prefix_int + addr_offset
            src_port = probe_src_port + port_offset
            probes.append(
                Probe(
                    dst_addr=ip_address(dst_addr),
                    src_port=src_port,
                    dst_port=probe_dst_port,
                    ttl=target.max_ttl,
                    protocol=target.protocol,
                )
            )

    return probes


def traceroute(
    targets: List[Target],
    mapper: FlowMapper,
    probe_src_port: int = DEFAULT_PROBE_SRC_PORT,
    probe_dst_port: int = DEFAULT_PROBE_DST_PORT,
) -> List[Probe]:
    """
    Generates a list of probes for a set of targets using the given flow mapper.
    Replicates the behavior of the Traceroute tool.

    Returns a list of probes.
    """
    probes = []
    for target in targets:
        dst_prefix_int = int(target.prefix.network_address)
        for flow_id in range(target.n_flows):
            for ttl in range(target.min_ttl, target.max_ttl + 1):
                addr_offset, port_offset = mapper.offset(flow_id, dst_prefix_int)
                dst_addr = dst_prefix_int + addr_offset
                src_port = probe_src_port + port_offset
                probes.append(
                    Probe(
                        dst_addr=ip_address(dst_addr),
                        src_port=src_port,
                        dst_port=probe_dst_port,
                        ttl=ttl,
                        protocol=target.protocol,
                    )
                )

    return probes
