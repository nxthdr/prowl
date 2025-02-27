from prowl.models import Target, Protocol
from ipaddress import ip_network
from prowl.traceroutes import yarrp
from prowl.mappers import SequentialFlowMapper

if __name__ == "__main__":

    src_port, dst_port = 24000, 33434
    mapper = SequentialFlowMapper()
    targets = [
        Target(
            prefix=ip_network("1.1.1.0/24"),
            protocol=Protocol.ICMP,
            min_ttl=1,
            max_ttl=30,
            n_intitial_flows=6
        )
    ]

    probes = yarrp(targets, mapper, src_port, dst_port)
    for probe in probes:
        print(probe)