# To test whether a section exists, use has_section(),
# passing the section name as the argument to the method.

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisection.ini')
for candidate in ['wiki', 'bug_tracker', 'dvcs']:
	print('{:<12}: {}'.format(candidate, parser.has_section(candidate)))