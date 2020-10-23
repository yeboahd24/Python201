#! usr/bin/env/python3
from random import randint
from typing import Tuple
class Dice(object):
	
	def __init__(self) -> None:
		self.faces: Tuple[int, int] = (0, 0)

	def roll(self) -> None:
		"""This return the faces of the dice"""
		self.faces = (randint(1, 6), randint(1, 6))


	def total(self) -> int:   # total number of faces
		return sum(self.faces)

	def hardway(self) -> bool:
		"""This test if the game is hard or not"""
		return self.faces[0] == self.faces[1]

	def easyway(self) -> bool:
		return self.faces[0] != self.faces[1]

if __name__ == "__main__":
	dice = Dice()
	print(dice.roll())
	# print(dice.faces)
	# print(dice.total())
	# print(dice.hardway())
	# print(dice.easyway())



