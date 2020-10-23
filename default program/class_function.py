#!usr/bin/env/python3
# Accept Function Instead of Classes for Simple Interface
from collections import defaultdict

# missing keys
def log_missing():
	print('Key added')
	return 0

current = {'green': 12, 'blue': 3}
increments = [
	('red', 5),
	('blue', 17),
	('orange', 9),
]

results = defaultdict(log_missing, current)
print('Before:', dict(results))
for key, amount in increments:
	results[key] += amount
print('After:', dict(results))
