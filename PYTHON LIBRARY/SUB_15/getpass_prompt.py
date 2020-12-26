import getpass

p = getpass.getpass(prompt='What is your favorite color? ')
if p.lower() == 'blue':
	print('Right. Off you go.')
else:
	print('Auuuuugh!')