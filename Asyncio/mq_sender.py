import asyncio
import argparse
import uuid
from msgproto import send_msg
from itertools import count

async def main(args):
    me = uuid.uuid4().hex[:8]
    print(f'Starting up {me}')
    reader, writer = await asyncio.open_connection(host=args.host, port=args.port)
    print(f'I am {writer.get_extra_info("sockname")}')
    channel = b'/null'
    await send_msg(writer, channel)
    chan = args.channel.encode()
    try:
        for i in count():
            await asyncio.sleep(args.interval)
            data = b'X'*args.size or f'Msg {i} from {me}'.encode()
            try:
                await send_msg(writer, chan)
                await send_msg(writer, data)
            except OSError:
                print('Connection ended.')
                break
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=25000, type=int)
    parser.add_argument('--channel', default='/topic/foo')
    parser.add_argument('--size', default=1, type=float)
    try:
        asyncio.run(main(parser.parse_args()))
    except KeyboardInterrupt:
        print('Bye!')