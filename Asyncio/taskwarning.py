#!usr/bin/env/python3

# Destroyer of pending tasks
import asyncio

async def f(delay):
	await asyncio.sleep(delay)

loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))
loop.run_until_complete(t1)
loop.close() # Task was destroyed but it is pending, it means some task in pending, not completed yet






