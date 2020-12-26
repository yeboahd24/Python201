# The digest value is different in this example because the algorithm changed from MD5 to
# SHA1

import hashlib
from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
