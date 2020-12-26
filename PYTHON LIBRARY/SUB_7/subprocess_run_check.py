import subprocess
try:
	subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
	print('ERROR:', err)