# argparse will automatically add options to generate help, if configured to do so. The
# add_help argument to ArgumentParser controls the help-related options.

# The help options (-h and --help) are added by default, but can be disabled by setting
# add_help to false.

import argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
print(parser.parse_args())