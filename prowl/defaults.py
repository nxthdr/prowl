DEFAULT_PREFIX_LEN_V4 = 24
"""Default prefix length for IPv4."""
DEFAULT_PREFIX_LEN_V6 = 64
"""Default prefix length for IPv6."""

DEFAULT_PREFIX_SIZE_V4 = 2 ** (32 - DEFAULT_PREFIX_LEN_V4)
"""Default prefix size (number of addresses) for IPv4."""
DEFAULT_PREFIX_SIZE_V6 = 2 ** (128 - DEFAULT_PREFIX_LEN_V6)
"""Default prefix size (number of addresses) for IPv6."""

DEFAULT_PROBE_SRC_PORT = 24000
"""Default probe source port. Encoded in the ICMP checksum field for ICMP probes."""
DEFAULT_PROBE_DST_PORT = 33434
"""Default probe destination port. Unused for ICMP probes."""
