# An asyncio.Event is based on a threading.Event. It allows multiple consumers to wait
# for something to happen without looking for a specific value to be associated with the
# notification.

# As with the Lock, both coro1() and coro2() wait for the event to be set. The difference
# is that both can start as soon as the event state changes, and they do not need to acquire
# a unique hold on the event object.


import asyncio
import functools

def set_event(event):
	print('setting event in callback')
	event.set()

async def coro1(event):
		print('coro1 waiting for event')
		await event.wait()
		print('coro1 triggered')

async def coro2(event):
		print('coro2 waiting for event')
		await event.wait()
		print('coro2 triggered')

async def main(loop):
		# Create a shared event.
		event = asyncio.Event()
		print('event start state: {}'.format(event.is_set()))
		loop.call_later(
		0.1, functools.partial(set_event, event)
		)
		await asyncio.wait([coro1(event), coro2(event)])
		print('event end state: {}'.format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(event_loop))
finally:
	event_loop.close()