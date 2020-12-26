# The parent parser approach described earlier is one way to share options between related
# commands. An alternative approach is to first combine the commands into a single program,
# and then use sub-parsers to handle each portion of the command line

# Each sub-parser also has its own help, which describes the arguments and options for
# that command
# Eg: python3 argparse_subparsers.py create -h
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='commands')
# A list command
list_parser = subparsers.add_parser(
'list', help='List contents')
list_parser.add_argument(
'dirname', action='store',
help='Directory to list')
# A create command
create_parser = subparsers.add_parser(
'create', help='Create a directory')
create_parser.add_argument(
'dirname', action='store',
help='New directory to create')
create_parser.add_argument(
'--read-only', default=False, action='store_true',
help='Set permissions to prevent writing to the directory',
)
# A delete command
delete_parser = subparsers.add_parser(
'delete', help='Remove a directory')
delete_parser.add_argument(
'dirname', action='store', help='The directory to remove')
delete_parser.add_argument(
'--recursive', '-r', default=False, action='store_true',
help='Remove the contents of the directory, too',
)
print(parser.parse_args())
