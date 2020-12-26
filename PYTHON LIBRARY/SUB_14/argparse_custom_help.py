
import argparse

# print_usage() prints the short usage message for an argument parser, and print_help()
# prints the full help output.

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
print('print_usage output:')
parser.print_usage()
print()
print('print_help output:')
parser.print_help()
