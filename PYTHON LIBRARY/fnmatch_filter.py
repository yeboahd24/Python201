
# Internally, fnmatch converts the glob pattern to a regular expression and uses the re
# (page 13) module to compare the name and pattern. The translate() function is the public
# API for converting glob patterns to regular expressions.


import fnmatch
import os
import pprint
pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
files = os.listdir('.')
print('\nFiles :')
pprint.pprint(files)
print('\nMatches :')
pprint.pprint(fnmatch.filter(files, pattern))
print('Regex :', fnmatch.translate(pattern))