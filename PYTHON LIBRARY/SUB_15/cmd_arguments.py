# A command interpreter created with cmd uses a loop to read all lines from its input, parse
# them, and then dispatch the command to an appropriate command handler. Input lines
# are parsed into two parts: the command, and any other text on the line. For example, if
# the user enters foo bar, and the interpreter class includes a method named do_foo(), it is
# called with "bar" as the only argument.
# The end-of-file marker is dispatched to do_EOF(). If a command handler returns a value
# that evaluates to true, the program will exit cleanly. Thus, to provide a clean way to exit
# the interpreter, make sure to implement do_EOF() and have it return True.
# The following simple example program supports the “greet” command.

import cmd

class HelloWorld(cmd.Cmd):
	def do_greet(self, person):  # means any method should use do_ before anything
		"""greet [person]
		Greet the named person"""
		if person:
			print("hi,", person)
		else:
			print('hi')

	def do_EOF(self, line):
		return True

	def postloop(self):
		print()

if __name__ == '__main__':
	HelloWorld().cmdloop()