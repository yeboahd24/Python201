import asyncio

# The remaining background operations should be handled explicitly for several reasons.
# Although pending tasks are suspended when wait() returns, they will resume as soon as
# control reverts to the event loop. Without another call to wait(), nothing will receive the
# output of the tasks; that is, the tasks will run and consume resources with no benefit. Also,
# asyncio emits a warning if there are pending tasks when the program exits. These warnings
# may be printed on the console, where users of the application will see them. Therefore, it
# is best either to cancel any remaining background operations, or to use wait() to let them
# finish running.

async def phase(i):
		print('in phase {}'.format(i))
		try:
			await asyncio.sleep(0.1 * i)
		except asyncio.CancelledError:
			print('phase {} canceled'.format(i))
			raise
		else:
			print('done with phase {}'.format(i))
			return 'phase {} result'.format(i)

async def main(num_phases):
		print('starting main')
		phases = [
		phase(i)
		for i in range(num_phases)
		]

		print('waiting 0.1 for phases to complete')
		completed, pending = await asyncio.wait(phases, timeout=0.1)
		print('{} completed and {} pending'.format(
		len(completed), len(pending),
		))

		# Cancel remaining tasks so they do not generate errors
		# as we exit without finishing them.
		if pending:
			print('canceling tasks')
		for t in pending:
			t.cancel()
		print('exiting main')


event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	event_loop.close()