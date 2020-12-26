# The logging module is integrated with warnings through the captureWarnings() function,
# which configures warnings to send messages through the logging system
# instead of outputting them directly.

import logging
import warnings

logging.basicConfig(
level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')
logging.captureWarnings(True)
warnings.warn('This warning is sent to the logs')