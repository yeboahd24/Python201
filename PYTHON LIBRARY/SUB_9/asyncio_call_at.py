# It is also possible to schedule a call to occur at a specific time. The loop used for this
# purpose relies on a monotonic clock, rather than a wall-clock time, to ensure that the value
# of “now” never regresses. To choose a time for a scheduled callback, it is necessary to start
# from the internal state of that clock using the loop’s time() method.


import asyncio
import time

def callback(n, loop):
	print('callback {} invoked at {}'.format(n, loop.time()))

async def main(loop):
	now = loop.time()
	print('clock time: {}'.format(time.time()))
	print('loop time: {}'.format(now))
	print('registering callbacks')
	loop.call_at(now + 0.2, callback, 1, loop)
	loop.call_at(now + 0.1, callback, 2, loop)
	loop.call_soon(callback, 3, loop)
	await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
	print('entering event loop')
	event_loop.run_until_complete(main(event_loop))
finally:
	print('closing event loop')
	event_loop.close()
