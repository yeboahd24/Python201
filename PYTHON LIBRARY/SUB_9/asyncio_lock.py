# A Lock can be used to guard access to a shared resource. Only the holder of the lock can
# use the resource. Multiple attempts to acquire the lock will block so that there is only one
# holder at a time.


import asyncio
import functools

def unlock(lock):
	print('callback releasing lock')
	lock.release()

async def coro1(lock):
		print('coro1 waiting for the lock')
		with await lock:
			print('coro1 acquired lock')
		print('coro1 released lock')

async def coro2(lock):
		print('coro2 waiting for the lock')
		await lock
		try:
			print('coro2 acquired lock')
		finally:
			print('coro2 released lock')
			lock.release()

async def main(loop):
		# Create and acquire a shared lock.
		lock = asyncio.Lock()
		print('acquiring the lock before starting coroutines')
		await lock.acquire()
		print('lock acquired: {}'.format(lock.locked()))
		# Schedule a callback to unlock the lock.
		loop.call_later(0.1, functools.partial(unlock, lock))
		# Run the coroutines that want to use the lock.
		print('waiting for coroutines')
		await asyncio.wait([coro1(lock), coro2(lock)]),

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(event_loop))
finally:
	event_loop.close()