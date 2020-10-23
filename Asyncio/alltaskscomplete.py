#!usr/bin/env/python3

import asyncio

async def f(delay):
	await asyncio.sleep(1 / delay) # ZeroDivisonError but won't stop the execution of the function
	return delay

loop = asyncio.get_event_loop()
for i in range(10):
	loop.create_task(f(i))  
pending = asyncio.all_tasks()
group = asyncio.gather(*pending, return_exceptions=True) # This makes all the tasks to run before reporting any errors
results = loop.run_until_complete(group)
print(f'Results: {results}')
loop.close()