from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Protocol


class FlowMapper(Protocol):
    """Protocol to which a flow mapper must conform."""

    def flow_id(self, addr_offset: int, port_offset: int, prefix: int) -> int:
        """Return the flow ID for a given address and port offset."""
        ...

    def offset(self, flow_id: int, prefix: int) -> tuple[int, int]:
        """Return the address and port offset for a given flow ID."""
        ...


IPNetwork = IPv4Network | IPv6Network
IPAddress = IPv4Address | IPv6Address
