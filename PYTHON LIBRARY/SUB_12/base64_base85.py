# The Base85 functions use an expanded alphabet that is more space-efficient than the
# one used for Base64 encoding.

# Several Base85 encodings and variations are used in Mercurial, git, and the PDF file
# format. Python includes two implementations, b85encode() implements the version used in
# Git Mercurial, and a85encode() implements the Ascii85 variant used by PDF files.


import base64

original_data = b'This is the data, in the clear.'
print('Original : {} bytes {!r}'.format(
len(original_data), original_data))
b64_data = base64.b64encode(original_data)
print('b64 Encoded : {} bytes {!r}'.format(
len(b64_data), b64_data))
b85_data = base64.b85encode(original_data)
print('b85 Encoded : {} bytes {!r}'.format(
len(b85_data), b85_data))
a85_data = base64.a85encode(original_data)
print('a85 Encoded : {} bytes {!r}'.format(
len(a85_data), a85_data))
