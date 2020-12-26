# The sched module implements a generic event scheduler for running tasks at specific times.

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name, start):
	now = time.time()
	elapsed = int(now - start)
	print('EVENT: {} elapsed={} name={}'.format(
		time.ctime(now), elapsed, name))
	
start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, print_event, ('first', start))
scheduler.enter(3, 1, print_event, ('second', start))
scheduler.run()