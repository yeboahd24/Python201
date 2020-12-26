import argparse

# If the argument to --mode is not one of the allowed values, an error is generated and
# processing stops.

parser = argparse.ArgumentParser()
parser.add_argument(
'--mode',
choices=('read-only', 'read-write'),
)
print(parser.parse_args())