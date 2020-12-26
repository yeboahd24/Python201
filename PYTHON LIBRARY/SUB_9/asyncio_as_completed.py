# as_completed() is a generator that manages the execution of a list of coroutines given to it
# and produces their results one at a time as each coroutine finishes running. As with wait(),
# order is not guaranteed by as_completed(), but it is not necessary to wait for all of the
# background operations to complete before taking other action.

# This example starts several background phases that finish in the reverse order from which
# they start. As the generator is consumed, the loop waits for the result of the coroutine using
# await

import asyncio

async def phase(i):
		print('in phase {}'.format(i))
		await asyncio.sleep(0.5 - (0.1 * i))
		print('done with phase {}'.format(i))
		return 'phase {} result'.format(i)

async def main(num_phases):
		print('starting main')
		phases = [
		phase(i)
		for i in range(num_phases)
		]
		print('waiting for phases to complete')
		results = []
		for next_to_complete in asyncio.as_completed(phases):
			answer = await next_to_complete
			print('received answer {!r}'.format(answer))
			results.append(answer)
		print('results: {!r}'.format(results))
		return results

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	event_loop.close()

	