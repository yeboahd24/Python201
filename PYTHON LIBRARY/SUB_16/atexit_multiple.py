# It is also possible to register more than one function and to pass arguments to the
# registered functions. That approach can be useful to cleanly disconnect from databases and
# remove temporary files, among other things. Instead of keeping a list of resources that need
# to be freed, a separate cleanup function can be registered for each resource.

import atexit

def my_cleanup(name):
	print('my_cleanup({})'.format(name))

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')

# The exit functions are called in the reverse of the order in which they are registered.
# This method allows modules to be cleaned up in the reverse order from which they are
# imported (and therefore register their atexit functions), which should reduce dependency
# conflicts.