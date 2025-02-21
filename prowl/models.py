from ipaddress import IPv4Address, IPv6Address
from dataclasses import dataclass


class Protocol:
    ICMP = "icmp"
    ICMP6 = "icmp6"
    UDP = "udp"

@dataclass
class Probe:
    dst_addr: IPv4Address | IPv6Address
    src_port: int
    dst_port: int
    ttl: int
    protocol: Protocol

    def __str__(self):
        return f"{self.dst_addr},{self.src_port},{self.dst_port},{self.ttl},{self.protocol}"