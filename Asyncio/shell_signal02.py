#!usr/bin/env/python3
# Handle both SIGINT and SIGTERM, but stop the loop only once

import asyncio
from signal import SIGINT, SIGTERM


#
#
# async def main():
#     try:
#         while True:  # Your app will run until you stop it
#             print('<Your app is running>')
#             await asyncio.sleep(1)
#     except asyncio.CancelledError:
#         for i in range(3):
#             print('<Your app is shutting down...>')
#             await asyncio.sleep(1)
#
#
# def handler(sig):
#     loop.stop()
#     print(f'Got signal: {sig!s}, shouting down')
#     loop.remove_signal_handler(SIGTERM)
#     loop.add_signal_handler(SIGINT, lambda: None)
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     for sig in (SIGTERM, SIGINT):
#         loop.add_signal_handler(sig, handler, sig)
#         loop.create_task(main())
#         loop.run_forever()
#         tasks = asyncio.all_tasks(loop=loop)
#         for t in tasks:
#             t.cancel()
#         group = asyncio.gather(*tasks, return_exceptions=True)
#         loop.run_until_complete(group)
#         loop.close()

async def main():
    loop = asyncio.get_running_loop()
    for sig in (SIGTERM, SIGINT):
        loop.add_signal_handler(sig, handler, sig)
    try:
        while True:
            print('<Your app is running>')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('<Your app is shouting down>')
        await asyncio.sleep(1)


def handler(sig):
    loop = asyncio.get_running_loop()
    for task in asyncio.all_tasks(loop=loop):
        task.cancel()
    print(f'<Got signal: {sig!s}, shouting down')
    loop.remove_signal_handler(SIGTERM)
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == '__main__':
    asyncio.run(main())
