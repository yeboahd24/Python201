# The cmd module contains one public class, Cmd, which is designed to be used as a base class for
# interactive shells and other command interpreters. By default, cmd uses readline
# for interactive prompt handling, command-line editing, and command completion.


import cmd

class HelloWorld(cmd.Cmd):
	def do_greet(self, line):
		print("hello")

	def do_EOF(self, line):
		return True


if __name__ == '__main__':
	HelloWorld().cmdloop()