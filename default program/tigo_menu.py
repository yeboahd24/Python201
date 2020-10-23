#!usr/bin/env/python3

"""Telecommunication Data Bundle Purchase Menu"""
# By Linux(Software Engineer)
import random
from functools import wraps

OPTIONS = ['BigTime Xtra', 'Fuse Xtra', 'Xtra Unlimited Calls']
OPTIONS_ONE = ['25MB + 25MB @50p', '65MB + 65MB @1GH', '150MB + 150MB @2GH']

def decorator(func):
	wraps(func)
	def wrapper(*args,):
		print('One-Stop Shop')
		print("*"*13)
		return func(*args)
	return wrapper


class Menu(object):
	InitialAmount = 1000_000.00 # Initial balance

	def __init__(self):
		self.human_choice = None

	def get_human_choice(self):
		choice_number = int(input("Enter the number of your choice: "))
		self.human_choice = OPTIONS[choice_number - 1]
		if choice_number == 1:
			print(('\n'.join(f'({i} {option.title()}' for i, option in enumerate(OPTIONS_ONE, start=1))))
			print(" ")
			choice_number = int(input("Enter the number of your choice: "))
			
			if choice_number == 1:
				if Menu.InitialAmount < 50:
					raise ValueError(f"You don't have enough balance")
				Menu.InitialAmount -= 50
				print(('Congratulation you purchase 25MB + 25MB with unlimited'))
				return(f"Your new balance is: {Menu.InitialAmount}")


			if choice_number == 2:
				if Menu.InitialAmount < 100:
					raise ValueError(f"You don't have enough balance")
				Menu.InitialAmount -= 100
				print(('Congratulation you purchase 65MB + 65MB with unlimited'))
				return(f"Your new balance is: {Menu.InitialAmount}")

			if choice_number == 3:
				if Menu.InitialAmount < 200:
					raise ValueError(f"You don't have enough balance")
				Menu.InitialAmount -= 200
				print(('Congratulation you purchase 150MB + 150MB with unlimited'))
				return(f"Your new balance is: {Menu.InitialAmount}")


	@decorator
	def print_options(self):
		return ('\n'.join(f'({i} {option.title()}' for i, option in enumerate(OPTIONS, start=1)))






menu = Menu()
print(menu.print_options())
print(" ")
print(menu.get_human_choice())








# 	def get_all_options(self):
# 		print(self.print_options())
# 		self.get_human_choice()

# if __name__ == '__main__':
# 	menu = Menu()
# 	menu.get_all_options()



