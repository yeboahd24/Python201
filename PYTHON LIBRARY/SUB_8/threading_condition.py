import logging
import threading
import time

# the consumer()
# threads wait for the Condition to be set before continuing. The producer() thread is
# responsible for setting the condition and notifying the other threads that they can
# continue

def consumer(cond):
	"""wait for the condition and use the resource"""
	logging.debug('Starting consumer thread')
	with cond:
		cond.wait()
		logging.debug('Resource is available to consumer')

def producer(cond):
	"""set up the resource to be used by the consumer"""
	logging.debug('Starting producer thread')
	with cond:
		logging.debug('Making resource available')
		cond.notifyAll()

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s (%(threadName)-2s) %(message)s',
)


condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer,
args=(condition,))
c2 = threading.Thread(name='c2', target=consumer,
args=(condition,))
p = threading.Thread(name='p', target=producer,
args=(condition,))


c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()