from concurrent import futures
import threading
import time

def task(n):
	print('{}: sleeping {}'.format(
	threading.current_thread().name,
	n)
	)
	time.sleep(n / 10)
	print('{}: done with {}'.format(
	threading.current_thread().name,
	n)
	)
	return n / 10




ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)
print('main: future: {}'.format(f))
print('main: waiting for results')
result = f.result()
print('main: result: {}'.format(result))
print('main: future after result: {}'.format(f))
