from concurrent import futures

def task(n):
	print(n)
with futures.ThreadPoolExecutor(max_workers=2) as ex:
	print('main: starting')
	ex.submit(task, 1)
	ex.submit(task, 2)
	ex.submit(task, 3)
	ex.submit(task, 4)
print('main: done')