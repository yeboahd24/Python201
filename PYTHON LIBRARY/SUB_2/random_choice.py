# One common use for random number generators is to select a random item from a sequence
# of enumerated values, even if those values are not numbers. random includes the choice()
# function for making a random selection from a sequence. This example simulates flipping
# a coin 10,000 times to count how many times it comes up heads and how many times it
# comes up tails.


import random
import itertools
outcomes = {
'heads': 0,
'tails': 0,
}

sides = list(outcomes.keys())
for i in range(10000):
	outcomes[random.choice(sides)] += 1
print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])
