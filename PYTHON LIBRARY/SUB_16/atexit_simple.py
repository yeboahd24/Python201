# The atexit module provides an interface to register functions to be called when a program
# closes down normally.
# Because the program does not do anything else, all_done() is called right away.

import atexit

def all_done():
	print('all_done()')

print('Registering')
atexit.register(all_done)
print('Registered')