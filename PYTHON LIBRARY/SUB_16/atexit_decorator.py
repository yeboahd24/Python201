# Functions that do not require any arguments can be registered by using register() as
# a decorator. This alternative syntax is convenient for cleanup functions that operate on
# module-level global data.

import atexit

@atexit.register
def all_done():
	print('all_done()')
	
print('starting main program')