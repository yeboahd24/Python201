#!usr/bin/env/python3
import asyncio
import inspect

"""This is the basics of asyncio you must grap"""

# Async functions are functions, not coroutines

# async def f():
# 	return 123

# print(type(f)) # function
# print(inspect.iscoroutinefunction(f)) # True
# coro = f() # coroutine
# print(type(coro))
# print(inspect.iscoroutine(coro))

# # This behavior is identical to the way generator functions work in Python

# def g():
# 	yield 123
# print(type(g)) # function not generator yet
# gen = g() # generator function now
# print(type(gen))


# Coroutine internals

# async def f():
# 	return 123

# coro = f()
# try:
# 	coro.send(None)
# except StopIteration as e:
# 	print('The answer was: ', e.value)  # you don't have to do this manually because is handle by task(create_task)


# Using await on a coroutine

# async def f():
# 	await asyncio.sleep(1.0)
# 	return 123

# async def main():
# 	result = await f() # coroutine
# 	return result

# Coroutine cancellation with CancelledError
# async def f():
# 	try:
# 		while True: 
# 			await asyncio.sleep(0)
# 	except asyncio.CancelledError:
# 		print('I was cancelled')
# 	else:
# 		return 111

# coro = f()
# coro.send(None)
# coro.send(None)
# coro.throw(asyncio.CancelledError)
	


# Using the event loop to execute coroutine
# async def f():
# 	await asyncio.sleep(0)
# 	return 111

# loop = asyncio.get_event_loop()
# coro = f()
# print(loop.run_until_complete(coro))


# Interacting with a Future instance

async def main(f: asyncio.Future):
	await asyncio.sleep(1)
	f.set_result('I have finished')

loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(fut.done())  # False

loop.create_task(main(fut))
loop.run_until_complete(fut)
print(fut.done()) # True
print(fut.result())
