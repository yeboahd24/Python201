# A single argument definition can be configured to account for multiple arguments on the
# command line being parsed. Set nargs to one of the flag values from Table 14.1, based on
# the number of required or expected arguments.
# The parser enforces the argument count instructions and generates an accurate syntax
# diagram as part of the command help text.

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--three', nargs=3)
parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more', nargs='+')
print(parser.parse_args())