# splitext() works like split(), but divides the path on the extension separator, rather
# than the directory separator.


import os.path

PATHS = [
	'filename.txt',
	'filename',
	'/path/to/filename.txt',
	'/',
	'',
	'my-archive.tar.gz',
	'no-extension.',
]
for path in PATHS:
	print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))