# When the address of a server is available, use gethostbyaddr() to do a “reverse” lookup
# for the name.

import socket

hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')
print('Hostname :', hostname)
print('Aliases :', aliases)
print('Addresses:', addresses)