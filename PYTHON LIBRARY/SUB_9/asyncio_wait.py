#!usr/bin/env/python3

# Internally, wait() uses a set to hold the Task instances it creates, which means that
# the instances start, and finish, in an unpredictable order. The return value from wait() is
# a tuple containing two sets holding the finished and pending tasks.

import asyncio

async def phase(i):
		print('in phase {}'.format(i))
		await asyncio.sleep(0.1 * i)
		print('done with phase {}'.format(i))
		return 'phase {} result'.format(i)

async def main(num_phases):
		print('starting main')
		phases = [
		phase(i)
		for i in range(num_phases)
		]
		print('waiting for phases to complete')
		completed, pending = await asyncio.wait(phases)
		results = [t.result() for t in completed]
		print('results: {!r}'.format(results))

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	event_loop.close()