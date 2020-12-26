# Three methods can be used to access the directory listings and discover the names of files
# available on the file system. iterdir() is a generator, yielding a new Path instance for each
# item in the containing directory.


import pathlib

p = pathlib.Path('.')
for f in p.iterdir():
	print(f)


