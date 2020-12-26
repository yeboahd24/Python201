# Programmers commonly need to implement a suite of command-line tools that all take a
# set of arguments, and then perform some sort of specialized action. For example, if the
# programs all need to authenticate the user before taking any real action, they would all
# need to support --user and --password options. Rather than add the options explicitly to
# every ArgumentParser, it is possible to define a parent parser with the shared options, and
# then have the parsers for the individual programs inherit from its options.

# The first step is to set up the parser with the shared argument definitions. Since each
# subsequent user of the parent parser will try to add the same help options, causing an
# exception, automatic help generation is turned off in the base parser.


import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--user', action="store")
parser.add_argument('--password', action="store")