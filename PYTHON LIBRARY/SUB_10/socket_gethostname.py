# To find the official name of the current host, use gethostname().
# The name returned will depend on the network settings for the current system, and may
# change if it is on a different network (such as a laptop attached to a wireless LAN).

import socket

print(socket.gethostname())