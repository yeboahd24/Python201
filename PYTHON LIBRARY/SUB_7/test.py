import signal
import time

def receive_signal(name, age):
	print('What is your name?')
	print('Received:', name)
# Register signal handlers.
signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGINT, receive_signal)
signal.strsignal(2)

# print(dir(signal))

while True:
	print('Waiting...')
	time.sleep(3)
	receive_signal('linux', 20)