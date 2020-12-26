import logging
import random
import threading
import time

# In this example, the ActivePool class simply serves as a convenient way to track which
# threads are able to run at a given moment. A real resource pool would allocate a connection
# or some other value to the newly active thread, and reclaim the value when the thread is
# done. Here, it is just used to hold the names of the active threads to show that at most two
# are running concurrently.


class ActivePool:
	def __init__(self):
		super(ActivePool, self).__init__()
		self.active = []
		self.lock = threading.Lock()

	def makeActive(self, name):
		with self.lock:
			self.active.append(name)
			logging.debug('Running: %s', self.active)

	def makeInactive(self, name):
		with self.lock:
			self.active.remove(name)
			logging.debug('Running: %s', self.active)


def worker(s, pool):
	logging.debug('Waiting to join the pool')
	with s:
		name = threading.current_thread().getName()
		pool.makeActive(name)
		time.sleep(0.1)
		pool.makeInactive(name)

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
	t = threading.Thread(
	target=worker,
	name=str(i),
	args=(s, pool),
)
t.start()



