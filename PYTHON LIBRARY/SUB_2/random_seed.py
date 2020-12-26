#!usr/bin/env/python3

import random
random.seed(1) # This help to maintain the same random results eg. if the random number is 5 
#No matter how much you run the program you still get the same value because of the seed
for i in range(5):
	print('{:04.3f}'.format(random.random()), end=' ')
print()

# The argument to seed() can be any hashable object.