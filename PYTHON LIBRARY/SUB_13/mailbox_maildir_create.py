# The only real difference between creating a Maildir and an mbox is that the argument to
# the Maildir constructor is a directory name instead of a filename. As before, if the mailbox
# does not exist, it is created when messages are added.

# Although it is safe to write to the same Maildir from multiple processes, add() is not thread-safe.
# Use a semaphore or other locking device to prevent simultaneous modifications to the mailbox from
# multiple threads of the same process.



import mailbox
import email.utils
import os

from_addr = email.utils.formataddr(('Author',
'author@example.com'))
to_addr = email.utils.formataddr(('Recipient',
'recipient@example.com'))
payload = '''This is the body.
From (will not be escaped).
There are 3 lines.
'''
mbox = mailbox.Maildir('Example')
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
	msg.set_unixfrom('author Sat Feb 7 01:05:34 2009')
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = 'Sample message 2'
	msg.set_payload('This is the second body.\n')
	mbox.add(msg)
	mbox.flush()
finally:
	mbox.unlock()

for dirname, subdirs, files in os.walk('Example'):
	print(dirname)
	print(' Directories:', subdirs)
	for name in files:
		fullname = os.path.join(dirname, name)
		print('\n***', fullname)
		print(open(fullname).read())
		print('*' * 20)
