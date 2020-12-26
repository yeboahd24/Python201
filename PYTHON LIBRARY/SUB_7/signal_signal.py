import signal
import os
import time
def receive_signal(signum, stack):
	print('Received:', signum)
# Register signal handlers.
signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGINT, receive_signal)
# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())
while True:
	print('Waiting...')
	time.sleep(3)
	receive_signal(10, 20)

