import argparse

def get_args():
	"""This takes in required argument -x with optionals -y and -z
	>>> python arg_demo2.py -x 'linux'
	Namespace(x='linux', y=False, z=None)
	"""
	parser = argparse.ArgumentParser(
		description='A simple ArgumentParser',
		epilog='This is were you might put an example usage'
	)
	
	# required argument
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-x', '--execute', action = 'store', required=True, help = 'Help text for option X')

	# optional arguments
	group.add_argument('-y', help = 'Help text for option Y', default = False)
	parser.add_argument('-z', help = 'Help text for option Z', type = int)

	print(parser.parse_args())

if __name__ == '__main__':
	get_args()