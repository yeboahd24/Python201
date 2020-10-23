#!usr/bin/env/python3
# Refresher for using KeyboardInterrupt as SIGINT handle

import asyncio


async def main():
    while True:   # Your app will run until you stop it
        print('<Your app is running>')
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print('Got signal: SIGINT, shouting down')

    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
