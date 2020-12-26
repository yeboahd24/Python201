# A Barrier establishes a control
# point, and all participating threads then block until all of the participating “parties” have
# reached that point. With this approach, threads can start up separately and then pause
# until they are all ready to proceed.


import threading
import time

def worker(barrier):
	print(threading.current_thread().name,
	'waiting for barrier with {} others'.format(
	barrier.n_waiting))
	worker_id = barrier.wait()
	print(threading.current_thread().name, 'after barrier',
	worker_id)


NUM_THREADS = 3
barrier = threading.Barrier(NUM_THREADS)
threads = [
threading.Thread(
name='worker-%s' % i,
target=worker,
args=(barrier,),
)
for i in range(NUM_THREADS)
]
for t in threads:
	print(t.name, 'starting')
	t.start()
	time.sleep(0.1)
for t in threads:
	t.join()
