from prowl.typing import IPNetwork, IPAddress
from dataclasses import dataclass


class Protocol:
    ICMP = "icmp"
    ICMP6 = "icmp6"
    UDP = "udp"

@dataclass
class Probe:
    dst_addr: IPAddress
    src_port: int
    dst_port: int
    ttl: int
    protocol: Protocol

    def __str__(self):
        return f"{self.dst_addr},{self.src_port},{self.dst_port},{self.ttl},{self.protocol}"


@dataclass
class Target:
    prefix: IPNetwork
    protocol: Protocol
    min_ttl: int
    max_ttl: int
    n_intitial_flows: int