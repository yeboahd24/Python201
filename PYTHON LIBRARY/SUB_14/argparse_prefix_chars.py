import argparse

parser = argparse.ArgumentParser(
description='Change the option prefix characters',
prefix_chars='-+/',
)
parser.add_argument('-a', action="store_false",
default=None,
help='Turn A off',
)
parser.add_argument('+a', action="store_true",
default=None,
help='Turn A on',
)
parser.add_argument('//noarg', '++noarg',
action="store_true",
default=False)
print(parser.parse_args())


# Set the prefix_chars parameter for the ArgumentParser to a string containing all of
# the characters that should be allowed to signify options. Although prefix_chars establishes
# the allowed switch characters, the individual argument definitions specify the syntax for a
# given switch. This apparent redundancy gives explicit control over whether options using
# different prefixes are aliases (such as might be the case for platform-independent commandline syntax) or alternatives (e.g., using + to indicate turning a switch on and - to turn it
# off). In the previous example, +a and -a are separate arguments, and //noarg can also be
# given as ++noarg, but not --noarg.