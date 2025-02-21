from prowl.models import Probe, Protocol
from ipaddress import ip_address

if __name__ == "__main__":

    dst_addr = ip_address("2606:4700:4700::1111")
    src_port, dst_port = 24000, 33434
    protocol = Protocol.ICMP6

    for ttl in range(1, 30):
        probe = Probe(dst_addr, src_port, dst_port, ttl, protocol)
        print(probe)