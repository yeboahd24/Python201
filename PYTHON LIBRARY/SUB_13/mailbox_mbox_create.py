# The mbox format is the simplest to show in documentation, since it is entirely plain text.
# Each mailbox is stored as a single file, with all of the messages concatenated together. Each
# time a line starting with “From ” (“From” followed by a single space) is encountered, it
# is treated as the beginning of a new message. Whenever those characters appear at the
# beginning of a line in the message body, they are escaped by prefixing the line with >.

import mailbox
import email.utils

from_addr = email.utils.formataddr(('Author',
'author@example.com'))
to_addr = email.utils.formataddr(('Recipient',
'recipient@example.com'))
payload = '''This is the body.
From (will not be escaped).
There are 3 lines.
'''
mbox = mailbox.mbox('example.mbox')
mbox.lock()

try:
	msg = mailbox.mboxMessage()
	msg.set_unixfrom('author Sat Feb 7 01:05:34 2009')
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = 'Sample message 1'
	msg.set_payload(payload)
	mbox.add(msg)
	mbox.flush()

	msg = mailbox.mboxMessage()
	msg.set_unixfrom('author')
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = 'Sample message 2'
	msg.set_payload('This is the second body.\n')
	mbox.add(msg)
	mbox.flush()
finally:
	mbox.unlock()
print(open('example.mbox', 'r').read())
	