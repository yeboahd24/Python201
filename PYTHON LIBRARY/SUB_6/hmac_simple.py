# The new() function creates a new object for calculating a message signature. This example
# uses the default MD5 hash algorithm.


import hmac
digest_maker = hmac.new(b'secret-shared-key-goes-here')
with open('lorem.txt', 'rb') as f:
	while True:
		block = f.read(1024)
		if not block:
			break
		digest_maker.update(block)
digest = digest_maker.hexdigest()
print(digest)
