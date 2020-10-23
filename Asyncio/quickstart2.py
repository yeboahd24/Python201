import time
import asyncio


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(1.5)
    print(f'{time.ctime()} Hello from a thread!')


if __name__ == '__main__':
    asyncio.run(main())
