# The getpass() function prints a prompt, then reads input from the user until the user
# presses the enter key. The input is returned as a string to the caller.

import getpass
try:
	p = getpass.getpass()
except Exception as err:
	print('ERROR:', err)
else:
	print('You entered:', p)