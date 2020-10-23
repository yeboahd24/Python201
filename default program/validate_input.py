#!usr/bin/env/python3

from datetime import date

def get_date1():
	"""This illustrate how easy to use input() function.
		This will behave badly when the user enters invalid
		date.
	"""
	year = int(input('year: '))
	month = int(input('month [1-12]: '))
	day = int(input('day [1-31]: '))
	result = date(year, month, day)
	return result
# print(get_date1())

# validatin it in a pythonic way
# This will handle any errors in the get_date2 function

def get_integer(prompt:str) -> int:
	while True:
		value_text = input(prompt)
		try:
			value = int(value_text)
			return value
		except ValueError as ex:
			print(ex)

def get_date2() -> date:
	while True:
		year = get_integer('year: ')
		month = get_integer('month [1-12]: ')
		day = get_integer('day [1-31]: ')
		try:
			result = date(year, month, day)
			return result
		except ValueError as ex:
			problem = f'invalid, {ex}'
			return problem
print(get_date2())
