# The first step when using argparse is to create a parser object and tell it which arguments
# to expect. The parser can then be used to process the command-line arguments when the
# program runs. The constructor for the parser class (ArgumentParser) takes several arguments
# to set up the description used in the help text for the program and other global behaviors
# or settings.

import argparse

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
print(parser.parse_args(['-a', '-bval', '-c', '3']))