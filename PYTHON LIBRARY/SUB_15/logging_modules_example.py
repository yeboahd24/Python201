# The word root was embedded in all of the previous log messages because the code uses the
# root logger. An easy way to tell where a specific log message originates is to use a separate
# logger object for each module; log messages sent to a logger include the name of that logger.
# The following example illustrates logging from different modules in a way that makes it easy
# to trace the source of the message.

import logging

logging.basicConfig(level=logging.WARNING)
logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')
logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')