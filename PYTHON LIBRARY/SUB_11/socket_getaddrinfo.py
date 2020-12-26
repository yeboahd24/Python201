# getaddrinfo() converts the basic address of a service into a list of tuples with all of the
# information necessary to make a connection. Each tuple may contain different network
# families or protocols.

import socket

def get_constants(prefix):
	"""Create a dictionary mapping socket module
	constants to their names.
	"""
	return {
		getattr(socket, n): n
		for n in dir(socket)
		if n.startswith(prefix)
	}

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
for response in socket.getaddrinfo('www.python.org', 'http'):
	 # Unpack the response tuple.
	family, socktype, proto, canonname, sockaddr = response
	print('Family :', families[family])
	print('Type :', types[socktype])
	print('Protocol :', protocols[proto])
	print('Canonical name:', canonname)
	print('Socket address:', sockaddr)
	print()

