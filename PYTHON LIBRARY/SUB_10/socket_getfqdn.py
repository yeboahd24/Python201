# Use getfqdn() to convert a partial name to a fully qualified domain name
# The name returned will not necessarily match the input argument in any way if the input
# is an alias, as www is here.

import socket

for host in ['apu', 'pymotw.com']:
	print('{:>10} : {}'.format(host, socket.getfqdn(host)))