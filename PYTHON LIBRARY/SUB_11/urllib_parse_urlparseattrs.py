from urllib.parse import urlparse

# The username and password are available when present in the input URL, and set to
# None when not. The hostname is the same value as netloc, in all lowercase and with the
# port value stripped. The port is converted to an integer when present and None when not

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print('scheme :', parsed.scheme)
print('netloc :', parsed.netloc)
print('path :', parsed.path)
print('params :', parsed.params)
print('query :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port :', parsed.port)
