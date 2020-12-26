# The ensure_future() function returns a Task tied to the execution of a coroutine. That
# Task instance can then be passed to other code, which can wait for it without knowing how
# the original coroutine was constructed or called.

import asyncio

async def wrapped():
		print('wrapped')
		return 'result'
async def inner(task):
		print('inner: starting')
		print('inner: waiting for {!r}'.format(task))
		result = await task
		print('inner: task returned {!r}'.format(result))
async def starter():
		print('starter: creating task')
		task = asyncio.ensure_future(wrapped())
		print('starter: waiting for inner')
		await inner(task)
		print('starter: inner returned')

event_loop = asyncio.get_event_loop()
try:
	print('entering event loop')
	result = event_loop.run_until_complete(starter())
finally:
	event_loop.close()