
# Both methods create Path instances prepopulated with an absolute file system reference.
import pathlib
home = pathlib.Path.home()
print('home: ', home)
cwd = pathlib.Path.cwd()
print('cwd : ', cwd)

