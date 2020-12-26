# Daemon threads are useful for services
# where there may not be an easy way to interrupt the thread

import threading
import time
import logging

def daemon():
	logging.debug('Starting')
	time.sleep(0.2)
	logging.debug('Exiting')

def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start() # To wait until a daemon thread has completed its work, use the join() method.
d.join()
t.join()

