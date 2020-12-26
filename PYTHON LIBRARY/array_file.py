#The contents of an array can be written to and read from files using built-in methods coded
#efficiently for that purpose.


import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)
# Write the array of numbers to a temporary file.
output = tempfile.NamedTemporaryFile()
a.tofile(output.file) # Must pass an *actual* file
output.flush()
# Read the raw data.
with open(output.name, 'rb') as input:
	raw_data = input.read()
	print('Raw Contents:', binascii.hexlify(raw_data))
	# Read the data into an array.
	input.seek(0)
	a2 = array.array('i')
	a2.fromfile(input, len(a))
	print('A2:', a2)