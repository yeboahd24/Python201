# Most applications are configured to log to a file. Use the basicConfig() function to set up
# the default handler so that debug messages are written to a file.
# Running the script in the  listing repeatedly causes more messages to be appended
# to the file.

import logging

LOG_FILENAME = 'logging_example.out'

logging.basicConfig(
filename=LOG_FILENAME,
level=logging.DEBUG,
)
logging.debug('This message should go to the log file') #input
with open(LOG_FILENAME, 'rt') as f:
	body = f.read()
print('FILE:')
print(body)
