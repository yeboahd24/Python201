# Nested for loops that iterate over multiple sequences can often be replaced with
# product(), which produces a single iterable whose values are the Cartesian product of the
# set of input values.

from itertools import *
import pprint

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')
DECK = list(
	product(
		chain(range(2, 11), FACE_CARDS),
		SUITS,
	)
)

# for card in DECK:
# 	print('{:>2}{}'.format(*card), end=' ')
# 	if card[1] == SUITS[-1]:
# 		print()

#Odering
FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')
DECK = list(
	product(
		SUITS,
		chain(range(2, 11), FACE_CARDS),
	)
)

# for card in DECK:
# 	print('{:>2}{}'.format(card[1], card[0]), end=' ')
# 	if card[1] == FACE_CARDS[-1]:
# 		print()

for i in FACE_CARDS:
	for x in SUITS:
		print(list(zip(i, x)), end="")


print('Product')
t = list(
	product(
			(FACE_CARDS), SUITS)  # THIS MEANS NESTED LOOP CAN BE AVOIDED WITH PRODUCT
	)




print(t)