from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)


# Although the return value acts like a tuple, it is really based on a namedtuple, a subclass
# of tuple that supports accessing the parts of the URL via named attributes as well as
# indexes. In addition to being easier to use for the programmer, the attribute API offers
# access to several values not available in the tuple API.
