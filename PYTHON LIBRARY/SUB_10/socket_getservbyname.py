# In addition to an IP address, each socket address includes an integer port number. Many
# applications can run on the same host, listening on a single IP address, but only one socket
# at a time can use a port at that address. The combination of IP address, protocol, and
# port number uniquely identifies a communication channel and ensures that messages sent
# through a socket arrive at the correct destination.

# Some of the port numbers are pre-allocated for a specific protocol. For example, communication between email servers using SMTP occurs over port number 25 using TCP, and
# web clients and servers use port 80 for HTTP. The port numbers for network services with
# standardized names can be looked up with getservbyname().

import socket
from urllib.parse import urlparse

URLS = [
'http://www.python.org',
'https://www.mybank.com',
'ftp://prep.ai.mit.edu',
'gopher://gopher.micro.umn.edu',
'smtp://mail.example.com',
'imap://mail.example.com',
'imaps://mail.example.com',
'pop3://pop.example.com',
'pop3s://pop.example.com',
]

for url in URLS:
	parsed_url = urlparse(url)
	port = socket.getservbyname(parsed_url.scheme)
	print('{:>6} : {}'.format(parsed_url.scheme, port))