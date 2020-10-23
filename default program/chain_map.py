from collections import ChainMap
import os
import argparse

def main():
	"""This Override the username because of the ChainMap
		>>> python chain_map.py -u 'linux'
		linux
		linux
	"""

	app_default = {'username': 'admin', 'password': 'admin'}
	passer = argparse.ArgumentParser()
	passer.add_argument('-u', '--username')
	passer.add_argument('-p', '--password')
	arg = passer.parse_args()

	command_line_arguments = {key: value for key, value in vars(arg).items() if value}
	chain = ChainMap(command_line_arguments, os.environ, app_default)
	print(chain['username'])

if __name__ == '__main__':
	main()
	os.environ['username'] = 'Linux'
	main()


