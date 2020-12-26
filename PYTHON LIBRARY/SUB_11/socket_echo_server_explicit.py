
# It is important to bind a server to the correct address, so that clients can communicate with
# it. The previous examples all used 'localhost' as the IP address, which limits connections
# to clients running on the same server. Use a public address of the server, such as the value
# returned by gethostname(), to allow other hosts to connect. The next example modifies the
# echo server to listen on an address specified via a command-line argument.


import socket
import sys

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the address given on the command line.
server_name = sys.argv[1]

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