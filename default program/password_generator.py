import random

def create_password_generator(characters):
	def create_password(length):  # in here we are implenting the closure rule here
		output = []
		for i in range(length):
			output.append(random.choice(characters))
		return ''.join(output)
	return create_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5)) # note the digit 5 is the inner function which is the length
print(alpha_password(10))