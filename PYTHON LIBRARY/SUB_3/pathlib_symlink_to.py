# Use symlink_to() to create a symbolic link. The link will be named based on the path’s
# value and will refer to the name given as an argument to symlink_to().

import pathlib
p = pathlib.Path('example_link')
p.symlink_to('index.txt')
print(p)
print(p.resolve().name)