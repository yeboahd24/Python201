# By default, join() blocks indefinitely. Alternatively, a float value may be passed that
# represents the number of seconds to wait for the thread to become inactive. If the thread
# does not complete within the timeout period, join() returns anyway


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
t.start() 
d.join(0.1)
t.join()