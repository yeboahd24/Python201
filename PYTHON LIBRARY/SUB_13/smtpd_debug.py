# The previous example shows the arguments to process_message(), but smtpd also includes a
# server specifically designed for more complete debugging, called DebuggingServer. It prints
# the entire incoming message to the console and then stops processing (it does not proxy the
# message to a real mail server).
#That is smtpd_custom.py
import smtpd
import asyncore

server = smtpd.DebuggingServer(('127.0.0.1', 1025), None)
asyncore.loop()