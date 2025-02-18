from pounce.models import Probe, Protocol
from ipaddress import ip_address

def test_probe_str():
    """
    Test that the __str__ method of the Probe class returns the expected string.
    """
    probe = Probe(ip_address("1.1.1.1"), 24000, 33434, 1, Protocol.ICMP)
    assert str(probe) == "1.1.1.1,24000,33434,1,icmp"

    probe = Probe(ip_address("2606:4700:4700::1111"), 24000, 33434, 1, Protocol.UDP)
    assert str(probe) == "2606:4700:4700::1111,24000,33434,1,udp"

    probe = Probe(ip_address("2606:4700:4700::1111"), 24000, 33434, 1, Protocol.ICMP6)
    assert str(probe) == "2606:4700:4700::1111,24000,33434,1,icmp6"