# Tracebacks for exceptions raised in atexit callbacks are printed to the console. The last
# exception raised is raised again and serves as the final error message of the program.

import atexit

def exit_with_exception(message):
	raise RuntimeError(message)
	
atexit.register(exit_with_exception, 'Registered first')
atexit.register(exit_with_exception, 'Registered second')