import time
import asyncio


async def main():
    print(f'{time.ctime()} Hello')
    await asyncio.sleep(1.0)  # wainting for one minute
    print(f'{time.ctime()} Goodbye!')


# asyncio.run(main()) # using asycio.run in the func avoid more stuffs like get_event_loop() etc
loop = asyncio.get_event_loop()
coro = main()
asyncio.run(coro)


# Note this is the same as the above one
async def main():
    print(f'{time.ctime()} Hello')
    await asyncio.sleep(1.0)  # wainting for one minute
    print(f'{time.ctime()} Goodbye!')

# loop = asyncio.get_event_loop() # coroutine
# task = loop.create_task(main()) # without this your code won't run
# loop.run_until_complete(task)
# pending = asyncio.all_tasks(loop=loop)
# for task in pending:
# 	task.cancel()
# group = asyncio.gather(*pending, return_exceptions=True)
# loop.run_until_complete(group)
# loop.close()
