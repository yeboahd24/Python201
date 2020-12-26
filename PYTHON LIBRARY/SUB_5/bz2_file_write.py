# BZ2File can be used to write to and read from bzip2-compressed files using the usual
# methods for writing and reading data.

import bz2
import io
import os
data = 'Contents of the example file go here.\n'
with bz2.BZ2File('example.bz2', 'wb') as output:
	with io.TextIOWrapper(output, encoding='utf-8') as enc:
		enc.write(data)
os.system('file example.bz2')

