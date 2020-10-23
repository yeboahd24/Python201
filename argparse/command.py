import cmd
import random

class DiceCLI(cmd.Cmd):
	n_dice = 6 # number of dice

	def pre_loop(self):
		self.dice = None # no initial roll
		self.reroll_count = 0

	def do_roll(self, arg: str) -> bool:
		"""Roll the dice. Use the dice command to set the number fo dice"""
		self.dice = [random.randint(1, 6) for _ in range(self.n_dice)]
		print(f"{self.dice}")
		return False

	def do_reroll(self, arg: str) -> bool:
		"""Reroll selected. Provide the 0-based positions."""
		try:
			positions = map(int, arg.split())
		except ValueError as ex:
			print(ex)
		return False

		for p in positions:
			self.dice[p] = random.randint(1, 6)
			self.reroll_count += 1
		print(f"{self.dice} (reroll {self.reroll_count})")
		return False

	def do_dice(self, arg: str) -> bool:
		"""Sets the number of dice to roll"""
		try:
			self.n_dice = int(arg)
		except ValueError:
			print(f"Rolling   {self.n_dice} dice")
		return False

if __name__ == "__main__":
	game = DiceCLI()
	game.do_roll(5)
	game.do_roll(4)
	game.cmdloop()