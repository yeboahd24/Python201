
import collections
import random
# Set the random seed so we see the same output each time
# the script is run.
random.seed(1)
d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)
for i in range(5):
	n = random.randint(0, 100)
	print('n =', n)
	d1.append(n)
	d2.appendleft(n)
	print('D1:', d1)
	print('D2:', d2)
