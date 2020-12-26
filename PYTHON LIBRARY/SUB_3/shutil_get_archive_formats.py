# for creating and extracting archives in shutil. get_archive_formats() returns a sequence
# of names and descriptions for formats supported on the current system


import shutil
for format, description in shutil.get_archive_formats():
	print('{:<5}: {}'.format(format, description))
