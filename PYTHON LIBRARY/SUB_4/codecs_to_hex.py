import binascii
def to_hex(t, nbytes):
	"""Format text t as a sequence of nbyte long values
	separated by spaces.
	"""
	chars_per_item = nbytes * 2
	hex_version = binascii.hexlify(t)
	return b' '.join(hex_version[start:start + chars_per_item]
	for start in range(0, len(hex_version), chars_per_item))

if __name__ == '__main__':
	print(to_hex(b'abcdef', 1))
	print(to_hex(b'abcdef', 2))

# The function uses binascii to get a hexadecimal representation of the input byte string,
# then inserts a space between every nbytes bytes before returning the value.

