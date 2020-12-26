# To create a new file each time the program runs, pass a filemode argument to
# basicConfig() with a value of 'w'. Rather than managing the creation of files this way,
# though, it is better to use a RotatingFileHandler, which creates new files automatically
# and preserves the old log file at the same time.

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'
# Set up a specific logger with the desired output level.
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
# Add the log message handler to the logger.
handler = logging.handlers.RotatingFileHandler(
LOG_FILENAME,
maxBytes=20,
backupCount=5,
)
my_logger.addHandler(handler)

# Log some messages.
for i in range(20):
	my_logger.debug('i = %d' % i)

# See which files are created.
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
	print(filename)