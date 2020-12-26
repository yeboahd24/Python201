# This sample program, which is based on the one in the standard library documentation,
# receives incoming messages and echos them back to the sender. It starts by creating a
# TCP/IP socket, and then bind() is used to associate the socket with the server address. In
# this case, the address is localhost, referring to the current server, and the port number is
# 10000.

# Calling listen() puts the socket into server mode, and accept() waits for an incoming
# connection. The integer argument is the number of connections the system should queue
# up in the background before rejecting new clients. This example expects to work with only
# one connection at a time.
# accept() returns an open connection between the server and the client, along with the
# client’s address. The connection is actually a different socket on another port (assigned by
# the kernel). Data is read from the connection with recv() and transmitted with sendall().
# When communication with a client ends, the connection needs to be cleaned up using
# close(). This example uses a try:finally block to ensure that close() is always called,
# even in the event of an error.

import socket
import sys

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port.
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# Listen for incoming connections.
sock.listen(1)
while True:
	# Wait for a connection.
	print('waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print('connection from', client_address)
		# Receive the data in small chunks and retransmit it.
		while True:
				data = connection.recv(16)
				print('received {!r}'.format(data))
				if data:
					print('sending data back to the client')
					connection.sendall(data)
				else:
					print('no data from', client_address)
					break
	finally:
		# Clean up the connection.
		connection.close()