# Given a sequence of encoded bytes as a bytes instance, the decode() method translates
# them to code points and returns the sequence as a str instance.


import unicodedata
from codecs_to_hex import to_hex
text = 'français'
print('Raw : {!r}'.format(text))
for c in text:
	print(' {!r}: {}'.format(c, unicodedata.name(c, c)))
	print('UTF-8 : {!r}'.format(to_hex(text.encode('utf-8'), 1)))
	print('UTF-16: {!r}'.format(to_hex(text.encode('utf-16'), 2)))