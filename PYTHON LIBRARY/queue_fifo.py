#!usr/bin/env/python3

import queue
q = queue.Queue()
for i in range(5):
	q.put(i)
while not q.empty():
	print(q.get(), end=' ')
print()
