# argparse combines the argument definitions into “groups.” By default, it uses two groups:
# one for options and another for required position-based arguments.

import argparse
parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('--optional', action="store_true",
default=False)
parser.add_argument('positional', action="store") # no default value
print(parser.parse_args())