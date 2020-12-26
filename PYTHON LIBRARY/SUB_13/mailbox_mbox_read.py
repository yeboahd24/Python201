import mailbox

# To read an existing mailbox, open it and treat the mbox object like a dictionary. The keys
# are arbitrary values defined by the mailbox instance and are not necessary meaningful other
# than as internal identifiers for message objects.

mbox = mailbox.mbox('example.mbox')
for message in mbox:
	print(message['subject'])