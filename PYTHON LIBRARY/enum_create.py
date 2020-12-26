#!usr/bin/env/python3

import enum
#The enum module defines an enumeration type with iteration and comparison capabilities.
#It can be used to create well-defined symbols for values, instead of using literal integers or
#strings.


class BugStatus(enum.Enum):
	new = 7
	incomplete = 6
	invalid = 5
	wont_fix = 4 #same
	in_progress = 3
	fix_committed = 2
	fix_released = 1 # same
	by_design = 4 #same
	closed = 1 # same


# print('\nMember name: {}'.format(BugStatus.wont_fix.name))
# print('Member value: {}'.format(BugStatus.wont_fix.value))


# for status in BugStatus:
# 	print('{:15} = {}'.format(status.name, status.value))

#The members are produced in the order they are declared in the class definition. The
#names and values are not used to sort them in any way.

# enum aliasing
for status in BugStatus:
	print('{:15} = {}'.format(status.name, status.value))
print('\nSame: by_design is wont_fix: ',BugStatus.by_design is BugStatus.wont_fix)
print('Same: closed is fix_released: ',BugStatus.closed is BugStatus.fix_released)
