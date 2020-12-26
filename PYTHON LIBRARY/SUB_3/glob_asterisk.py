# An asterisk (*) matches zero or more characters in a segment of a name—for example,
# dir/* or *.


import glob
for name in sorted(glob.glob('*')):
	print(name)