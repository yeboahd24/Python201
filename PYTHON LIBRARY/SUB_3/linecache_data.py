# The linecache module is used within other parts of the Python standard library when
# dealing with Python source files.
# This module is especially useful when looking for multiple lines from the same file,
# such as when producing a traceback for an error report.

import os
import tempfile


lorem = '''Lorem ipsum dolor sit amet, consectetuer
	adipiscing elit. Vivamus eget elit. In posuere mi non
	risus. Mauris id quam posuere lectus sollicitudin
	varius. Praesent at mi. Nunc eu velit. Sed augue massa,
	fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
	eros pede, egestas at, ultricies ac, apellentesque eu,
	tellus.
	Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
	convallis accumsan. Ut felis. Donec lectus sapien, elementum
	nec, condimentum ac, interdum non, tellus. Aenean viverra,
	mauris vehicula semper porttitor, ipsum odio consectetuer
	lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
	aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
	porttitor eros.'''


def make_tempfile():
	fd, temp_file_name = tempfile.mkstemp()
	os.close(fd)
	with open(temp_file_name, 'wt') as f:
		f.write(lorem)
	return temp_file_name

def cleanup(filename):
	os.unlink(filename)


