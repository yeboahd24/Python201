# Using Thread to debug

import logging
import threading
import time

def worker():
	logging.debug('Starting')
	time.sleep(0.2)
	logging.debug('Exiting')

def my_service():
	logging.debug('Starting')
	time.sleep(0.3)
	logging.debug('Exiting')
	
logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # Use default name
w.start()
w2.start()
t.start()