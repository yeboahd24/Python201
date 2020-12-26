import asyncio
import functools

# If the timing of the callback does not matter, call_soon() can be used to schedule the call
# for the next iteration of the loop. Any extra positional arguments after the function are
# passed to the callback when it is invoked. To pass keyword arguments to the callback, use
# partial() from the functools

def callback(arg, *, kwarg='default'):
	print('callback invoked with {} and {}'.format(arg, kwarg))

async def main(loop):
		print('registering callbacks')

		loop.call_soon(callback, 1)
		wrapped = functools.partial(callback, kwarg='not default')
		loop.call_soon(wrapped, 2)
		await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
	print('entering event loop')
	event_loop.run_until_complete(main(event_loop))
finally:
	print('closing event loop')
	event_loop.close()



