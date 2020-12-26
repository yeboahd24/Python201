import os
import signal
import time
import sys
pid = os.getpid()
received = False

def signal_usr1(signum, frame):
	"Callback invoked when a signal is received"
	global received
	received = True
	print('CHILD {:>6}: Received USR1'.format(pid))
	sys.stdout.flush()


print('CHILD {:>6}: Setting up signal handler'.format(pid))
sys.stdout.flush()
signal.signal(signal.SIGTERM, signal_usr1)
print('CHILD {:>6}: Pausing to wait for signal'.format(pid))
sys.stdout.flush()
time.sleep(3)

if not received:
	print('CHILD {:>6}: Never received signal'.format(pid))

