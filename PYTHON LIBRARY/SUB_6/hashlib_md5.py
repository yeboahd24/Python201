# To calculate the MD5 hash, or digest, for a block of data (here a Unicode string converted
# to a byte string), first create the hash object, then add the data, and finally call digest()
# or hexdigest().

# This example uses the hexdigest() method instead of digest() because the output is
# formatted so it can be printed clearly. If a binary digest value is acceptable, use digest().

import hashlib
from hashlib_data import lorem
h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())