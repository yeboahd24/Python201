import mailbox

# The lock() and unlock() methods are used to prevent issues from simultaneous access to
# the file, and flush() forces the changes to be written to disk.

mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
	to_remove = []
	for key, msg in mbox.iteritems():
		if '2' in msg['subject']:
			print('Removing:', key)
			to_remove.append(key)
	for key in to_remove:
		mbox.remove(key)
finally:
	mbox.flush()
	mbox.close()
print(open('example.mbox', 'r').read())