import argparse
"""This print out a help test
>>> python arg_demo.py -h
"""

def get_args():
	parser = argparse.ArgumentParser(
		description='A simple ArgumentParser',
		epilog='This is were you might put an example usage'
	)
	return parser.parse_args()

if __name__ == '__main__':
	get_args()
