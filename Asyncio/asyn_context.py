#!usr/bin/env/python3
# connection to be opened and closed

# Async context manager

import asyncio
from contextlib import contextmanager, asynccontextmanager
# class Connection(object):
# 	def __init__(self, host, port):
# 		self.host = host
# 		self.port = port

# 	async def __aenter__(self):
# 		self.conn = await get_conn(self.host, self.port)
# 		return conn

# 	async def __aexist__(sefl, exc_type, exc, tb):
# 		await self.conn.close()


# async with Connection('localhost', 9001) as conn:
# 	# do stuff with conn
# 	pass

# blocking way

# @contextmanager  
# def web_page(url):
# 	data = download_webpage(url)                          
# 	yield data
# 	update_status(url)

# async with web_page('google.com') as data:
# 	process(data)


# Non blocking way

# @asynccontextmanager
# async def web_page(url):
# 	data = download_webpage(url)
# 	yield data
# 	await update_status(url)

# async with web_page('googl.com') as data:
# 	process(data)



# # Non blocking with little help
# @asynccontextmanager
# async web_page(url):
# 	loop asyncio.get_event_loop()
# 	data = await loop.run_in_executor(None, download_webpage, url)
# 	yield data

# async with web_page('google.com') as data:
# 	process(data)

