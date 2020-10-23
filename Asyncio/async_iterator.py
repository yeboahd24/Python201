#!usr/bin/env/python3
import asyncio

async def doubler(n):  # Async generator
	for i in range(n):
		yield i, i * 2
		await asyncio.sleep(0.1)

async def main():
	result = [x async for x in doubler(3)] # list comprehension
	print(result)
	result = {x: y async for x, y in doubler(3)} #  dict comprehension
	print(result)
	result = {x async for x in doubler(3)} # set comprehension
	print(result)

asyncio.run(main())


