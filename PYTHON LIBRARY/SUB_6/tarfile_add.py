
import tarfile
print('creating archive')
with tarfile.open('tarfile_add.tar', mode='w') as out:
	print('adding README.txt')
	out.add('README.txt')
print()
print('Contents:')
with tarfile.open('tarfile_add.tar', mode='r') as t:
	for member_info in t.getmembers():
		print(member_info.name)
