import secrets
import string

"""Generating alphanumeric password with at least one lower and upper character and at least three digits"""
alphabet = string.ascii_letters + string.digits
while True:
	password = ''.join(secrets.choice(alphabet) for i in range(10))
	if any(c.islower() for c in password) and any(c.upper() for c in password)\
	and sum(c.isdigit() for c in password) >=3:
	    break
# print(password)

#temporaly url
# generally for password reset
url = 'https://www.python.org/reset=' + secrets.token_urlsafe()
# print(url)
