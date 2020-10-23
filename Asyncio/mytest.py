#!usr/bin/env/python3
import time
import asyncio

# async def twoTimesTable():
# 	MULTIPLYER = 2
# 	NUMBER_OF_RANGE = 21
# 	for value in range(1, NUMBER_OF_RANGE):
# 		results = MULTIPLYER * value
# 		print(f'{MULTIPLYER} x {value} = {results}')
# 		await asyncio.sleep(.5)
#
# loop = asyncio.get_event_loop()
# coro = twoTimesTable()
# asyncio.run(coro)

'''Running multiple function at the same time'''


async def main():
    MULTIPLYER = 2
    NUMBER_OF_RANGE = 21
    for value in range(1, NUMBER_OF_RANGE):
        results = MULTIPLYER * value
        print(f'{MULTIPLYER} x {value} = {results}')
        await asyncio.sleep(.5)


def fiveTimesTable():
    MULTIPLYER = 5
    NUMBER_OF_RANGE = 21
    for value in range(1, NUMBER_OF_RANGE):
        results = MULTIPLYER * value
        print(f'{MULTIPLYER} x {value} = {results}')
        time.sleep(.5)


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_in_executor(None, fiveTimesTable)
loop.run_until_complete(task)


# async def main():
#     loop = asyncio.get_running_loop()
#     loop.run_in_executor(None, fiveTimesTable)
#     MULTIPLYER = 2
#     NUMBER_OF_RANGE = 21
#
#     for value in range(1, NUMBER_OF_RANGE):
#         results = MULTIPLYER * value
#         print(f'{MULTIPLYER} x {value} = {results}')
#         await asyncio.sleep(.5)


# def fiveTimesTable():
#     MULTIPLYER = 5
#     NUMBER_OF_RANGE = 21
#     for value in range(1, NUMBER_OF_RANGE):
#         results = MULTIPLYER * value
#         print(f'{MULTIPLYER} x {value} = {results}')
#         time.sleep(.5)

#
# if __name__ == '__main__':
#     asyncio.run(main())
