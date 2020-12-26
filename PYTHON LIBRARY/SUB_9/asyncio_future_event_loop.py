# A Future represents the result of work that has not been completed yet. The event loop
# can watch for a Future object’s state to indicate that it is done, allowing one part of an
# application to wait for another part to finish some work.

# A Future acts like a coroutine, so any techniques useful for waiting for a coroutine can also
# be used to wait for the future to be marked done. The next example passes the future to
# the event loop’s run_until_complete() method.


import asyncio

def mark_done(future, result):
	print('setting future result to {!r}'.format(result))
	future.set_result(result)

event_loop = asyncio.get_event_loop()
try:
	all_done = asyncio.Future()
	print('scheduling mark_done')
	event_loop.call_soon(mark_done, all_done, 'the result')
	print('entering event loop')
	result = event_loop.run_until_complete(all_done)
	print('returned result: {!r}'.format(result))
finally:
	print('closing event loop')
	event_loop.close()
	print('future result: {!r}'.format(all_done.result()))


# The state of the Future changes to done when set_result() is called, and the Future
# instance retains the result given to the method for later retrieval.