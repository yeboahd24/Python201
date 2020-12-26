#!usr/bin/env/python3

# Use glob() to find only files matching a pattern.
# The glob processor supports recursive scanning using the pattern prefix ** or by calling
# rglob() instead of glob().

import pathlib
p = pathlib.Path('..')
# for f in p.glob('*.py'):
# 	print(f)

for f in p.rglob('contextlib_*.py'):
	print(f)
