# The client program sets up its socket differently from the way a server does. Instead of
# binding to a port and listening, it uses connect() to attach the socket directly to the
# remote address.

# After the connection is established, data can be sent through the socket with sendall()
# and received with recv(), just as in the server. When the entire message is sent and a copy
# received, the socket is closed to free up the port.


import socket
import sys

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening.
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
try:
	# Send data.
	message = b'This is the message. It will be repeated.'
	print('sending {!r}'.format(message))
	sock.sendall(message)
	# Look for the response.
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print('received {!r}'.format(data))
finally:
	print('closing socket')
	sock.close()

