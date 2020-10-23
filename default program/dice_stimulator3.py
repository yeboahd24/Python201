#!usr/bin/env/python3

"""This is a dice stimulator game with type hint"""
import random
from typing import List, Set

class Dice(object):
	RNG = random.Random() # class variable or class instance

	def __init__(self, n: int, sides: int = 6) -> None:
		self.n_dice = n
		self.sides = sides
		self.faces = List[int]
		self.roll_number = 0

	def __str__(self) -> str:
		return ", ".join(f"{i}: {f}" for i, f in enumerate(self.faces))

	def total(self) -> int:
		return sum(self.faces)

	def average(self) -> float:
		return sum(self.faces)/self.n_dice

	def first_roll(self) -> List[int]:
		self.roll_number = 0
		self.faces = [self.RNG.randint(1, self.sides) for _ in range(self.n_dice)] # comprehensions
		return self.faces

	def reroll(self, postisions: Set[int]) -> List[int]:
		self.roll_number += 1
		for p in postisions:
			self.faces[p] = self.RNG.randint(1, self.sides)
		return self.faces

def example_mypy_failure() -> None:
	"""Trying to valiate the type hint leads to error
		this error happens because the n_dice suppose to be integer
	"""
	d = Dice(2.3) # error because the type hint is integer make it d = Dice(2)
	print(d.first_roll())
	print(d.reroll([1])) 
	d.first_roll()
	print(d) # return string representation
	
example_mypy_failure()  


