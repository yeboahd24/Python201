
import socket

# Since flags includes AI_CANONNAME, the canonical name of the server—which may be
# different from the value used for the lookup if the host has any aliases—is included in the
# results this time. Without the flag, the canonical name value is left empty.


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
responses = socket.getaddrinfo(
	host='www.python.org',
	port='http',
	family=socket.AF_INET,
	type=socket.SOCK_STREAM,
	proto=socket.IPPROTO_TCP,
	flags=socket.AI_CANONNAME,
)


for response in responses:
# Unpack the response tuple.
	family, socktype, proto, canonname, sockaddr = response
	print('Family :', families[family])
	print('Type :', types[socktype])
	print('Protocol :', protocols[proto])
	print('Canonical name:', canonname)
	print('Socket address:', sockaddr)
	print()
