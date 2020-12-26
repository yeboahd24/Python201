import signal
import time

def receive_alarm(signum, stack):
	print('Alarm :', time.ctime())

# Call receive_alarm in 2 seconds.
signal.signal(signal.SIGTERM, receive_alarm)
signal.set_wakeup_fd(2)

print('Before:', time.ctime())
time.sleep(4)
print('After :', time.ctime())

print(dir(signal))