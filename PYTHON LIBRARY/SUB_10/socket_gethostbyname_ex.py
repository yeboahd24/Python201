# For access to more naming information about a server, use gethostbyname_ex(). It returns the canonical hostname of the server, any aliases, and all of the available IP addresses
# that can be used to reach it.

import socket

HOSTS = [
'apu',
'pymotw.com',
'www.python.org',
'nosuchname',
]

for host in HOSTS:
	print(host)
try:
	name, aliases, addresses = socket.gethostbyname_ex(host)
	print(' Hostname:', name)
	print(' Aliases :', aliases)
	print(' Addresses:', addresses)
except socket.error as msg:
	print('ERROR:', msg)
print()
