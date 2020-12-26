import multiprocessing
import time

def slow_worker():
	print('Starting worker')
	time.sleep(0.1)
	print('Finished worker')

if __name__ == '__main__':
	p = multiprocessing.Process(target=slow_worker)
	print('BEFORE:', p, p.is_alive())
	p.start()
	print('DURING:', p, p.is_alive())

	p.terminate()
	print('TERMINATED:', p, p.is_alive())
	p.join()
	print('JOINED:', p, p.is_alive())