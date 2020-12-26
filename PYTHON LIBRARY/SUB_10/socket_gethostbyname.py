# Use gethostbyname() to consult the operating system hostname resolution API and convert
# the name of a server to its numerical address.

import socket

HOSTS = [
'apu',
'pymotw.com',
'www.python.org',
'nosuchname',
]

for host in HOSTS:
	try:
		print('{} : {}'.format(host, socket.gethostbyname(host)))
	except socket.error as msg:
		print('{} : {}'.format(host, msg))