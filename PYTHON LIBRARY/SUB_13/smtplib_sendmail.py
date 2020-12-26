# The most common use of SMTP is to connect to a mail server and send a message. The mail
# server hostname and port can be passed to the constructor, or connect() can be invoked
# explicitly. Once connected, call sendmail() with the envelope parameters and body of the
# message. The message text should be fully formed and comply with RFC 5322,
# 1
# since
# smtplib does not modify the contents or headers at all. That means the From and To headers
# need to be added by the caller.

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message.
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subject'] = 'Simple test message'
server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True) # Show communication with the server.
try:
	server.sendmail('author@example.com',
		['recipient@example.com'],
		msg.as_string())
finally:
	server.quit()



# The second argument to sendmail(), the recipients, is passed as a list. Any number of
# addresses can be included in the list to have the message delivered to each of them in turn.
# Since the envelope information is separate from the message headers, it is possible to blind
# carbon-copy (BCC) someone by including their address in the method argument but not in
# the message header.
