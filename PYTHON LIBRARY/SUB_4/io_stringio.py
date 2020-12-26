# StringIO provides a convenient means of working with text in memory using the file API
# (e.g., read(), write()). Using StringIO to build large strings can offer performance savings
#  In-memory stream buffers
# are also useful for testing, where writing to a real file on disk may slow down the test suite.


import io
# Write to a buffer.
output = io.StringIO()
output.write('This goes into the buffer. ')
print('And so does this.', file=output)
# Retrieve the value written.
print(output.getvalue())
output.close() # Discard buffer memory.
# Initialize a read buffer.
input = io.StringIO('Inital value for read buffer')
# Read from the buffer.
print(input.read())