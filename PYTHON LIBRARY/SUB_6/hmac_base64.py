import base64
import hmac
import hashlib


with open('lorem.txt', 'rb') as f:
	body = f.read()

hash = hmac.new(
	b'secret-shared-key-goes-here', # The secret key
	body, # content
	hashlib.sha1, # key type
)

digest = hash.digest()
print(base64.encodebytes(digest))

