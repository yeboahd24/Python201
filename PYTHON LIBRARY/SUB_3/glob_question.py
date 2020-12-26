# A question mark (?) is another wildcard character. It matches any single character in that
# position in the name.

import glob
for name in sorted(glob.glob('example?.txt')):
	print(name)

for name in sorted(glob.glob('dir/*[0-9].*')):
	print(name)