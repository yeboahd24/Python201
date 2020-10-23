import random

""" Organizing your code into functions."""
OPTIONS = ['rock', 'paper', 'scissor']

class RockPaperScissorsStimulator(object):
	"""Using self to access attributes"""
	def __init__(self):
		self.computer_choice = None
		self.human_choice = None

	def get_computer_choice(self):
		self.computer_choice = random.choice(OPTIONS)

	def get_human_choice(self):
		choice_number = int(input('Enter the number of your choice: '))
		self.human_choice = OPTIONS[choice_number - 1]

	def print_options(self):
		print('\n'.join(f'({i} {option.title()}' for i, option in enumerate(OPTIONS)))

	def print_choices(self):
		print(f'You choose {self.human_choice}')
		print(f'The computer choose {self.computer_choice}')

	def print_win_lose(self, human_beats, human_lose_to):
		if self.computer_choice == human_lose_to:
			print(f'Sorry, {self.computer_choice} beats {self.human_choice}')
		elif self.computer_choice == human_beats:
			print(f'Yes, {self.human_choice} beats {self.computer_choice}')

	def print_results(self):
		if self.human_choice == self.computer_choice:
			print('Draw')
		if self.human_choice == 'rock':
			self.print_win_lose('scissor', 'paper')
		elif self.human_choice == 'paper':
			self.print_win_lose('rock', 'scissor')
		elif self.human_choice == 'scissor':
			self.print_win_lose('paper', 'rock')

	def simulate(self):
		self.print_options()       # Note here should step by step
		self.get_human_choice()
		self.get_computer_choice()
		self.print_choices()
		self.print_results()

RPS = RockPaperScissorsStimulator()
RPS.simulate()