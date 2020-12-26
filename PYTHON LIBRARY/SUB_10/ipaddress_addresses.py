# The ipaddress module includes classes for working with IPv4 and IPv6 network addresses.
# The classes support validation, finding addresses and hosts on a network, and other common
# operations.

# The most basic object represents the network address itself. Pass a string, integer, or byte
# sequence to ip_address() to construct an address. The return value will be an IPv4Address
# or IPv6Address instance, depending on the type of address being used

import binascii
import ipaddress

ADDRESSES = [
'10.9.0.6',
'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
	addr = ipaddress.ip_address(ip)
	print('{!r}'.format(addr))
	print(' IP version:', addr.version)
	print(' is private:', addr.is_private)
	print(' packed form:', binascii.hexlify(addr.packed))
	print(' integer:', int(addr))
	print()
