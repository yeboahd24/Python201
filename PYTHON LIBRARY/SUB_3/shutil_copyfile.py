# copyfile() copies the contents of the source to the destination. It raises IOError if it does
# not have permission to write to the destination file.

import glob
import shutil
print('BEFORE:', glob.glob('shutil_copyfile.*'))  # current file
shutil.copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')
print('AFTER:', glob.glob('shutil_copyfile.*'))