# To open the file in text mode, set mode to 'w+t' when the file is created.

import tempfile
with tempfile.TemporaryFile(mode='w+t') as f:
	f.writelines(['first\n', 'second\n'])
	f.seek(0)
	for line in f:
		print(line.rstrip())


		