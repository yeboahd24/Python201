import os
import tempfile
with tempfile.TemporaryFile() as temp:
	temp.write(b'Some data')
	temp.seek(0)
	print(temp.read())

# After writing, the file handle must be “rewound” using seek() to read the data back from it.