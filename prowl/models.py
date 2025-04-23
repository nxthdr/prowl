from dataclasses import dataclass

from prowl.types import IPAddress, IPNetwork


class Protocol:
    """
    Enumeration of supported protocols.
    """

    ICMP = "ICMP"
    ICMP6 = "ICMPv6"
    UDP = "UDP"


@dataclass
class Probe:
    """
    A probe is a packet sent to a destination address, given a protocol at a given TTL.
    Also includes the source and destination ports.
    """

    dst_addr: IPAddress
    src_port: int
    dst_port: int
    ttl: int
    protocol: Protocol

    def __str__(self):
        return f"{self.dst_addr},{self.src_port},{self.dst_port},{self.ttl},{self.protocol}"


@dataclass
class Target:
    """
    A target is a network prefix, a protocol, and a range of TTLs.
    Also includes the number of flows to generate.
    """

    prefix: IPNetwork
    protocol: Protocol
    min_ttl: int
    max_ttl: int
    n_flows: int
