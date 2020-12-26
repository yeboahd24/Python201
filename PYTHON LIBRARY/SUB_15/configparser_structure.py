

from configparser import ConfigParser

# Both sections() and options() return lists of strings, while items() returns a list of tuples
# containing the name–value pairs.

parser = ConfigParser()
parser.read('multisection.ini')
for section_name in parser.sections():
	print('Section:', section_name)
	print(' Options:', parser.options(section_name))
	for name, value in parser.items(section_name):
		print(' {} = {}'.format(name, value))
		print()
