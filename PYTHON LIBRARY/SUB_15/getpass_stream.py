# By default, getpass() uses sys.stdout to print the prompt string. For a program that
# may produce useful output on sys.stdout, it is frequently a better choice to send the prompt
# to another stream such as sys.stderr.


import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print('You entered:', p)