# An optional keyword argument, access, is supported by both platforms. Use ACCESS_READ
# for read-only access, ACCESS_WRITE for write-through access (assignments to the memory go
# directly to the file), and ACCESS_COPY for copy-on-write access (assignments to memory are
# not written to the file).


import mmap
with open('lorem.txt', 'r') as f:
	with mmap.mmap(f.fileno(), 0,access=mmap.ACCESS_READ) as m:
		print('First 10 bytes via read :', m.read(10))
		print('First 10 bytes via slice:', m[:10])
		print('2nd 10 bytes via read :', m.read(10))


