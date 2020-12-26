#!usr/bin/env/python3


import enum

'''In some cases, it is more convenient to create enumerations programmatically, rather than
hard-coding them in a class definition. For those situations, Enum also supports passing the
member names and values to the class constructor.
'''

BugStatus = enum.Enum(
value='BugStatus',
names=('fix_released fix_committed in_progress '
'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus.new))
print('\nAll members:')
for status in BugStatus:
	print('{:15} = {}'.format(status.name, status.value))