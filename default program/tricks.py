#!usr/bin/env/python3
import winsound


# Iterating loop over copy

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for day in days.copy():
	if day == 'Wed':
		days.remove(day)
		print(day, 'Deleted Successfully!')


# Store Function in Variable

my_own_print = print
my_own_print('i can write anything!')





# Justify your test

for x in range(1, 10):
	print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
	print(repr(x*x*x).rjust(4))


# loop iterates 5 times i.e 5 beeps will be produced.

freq = 100
dur = 50
for i in range(0, 10):
	winsound.Beep(freq, dur)
	freq+= 100
	dur+= 50

