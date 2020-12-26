# A user or system administrator often edits a configuration file with a regular text editor
# to set application behavior defaults, with the application then reading the file, parsing
# it, and acting based on its contents. Use the read() method of ConfigParser to read the
# configuration file.


from configparser import ConfigParser

parser = ConfigParser()
parser.read('simple.ini')
print(parser.get('bug_tracker', 'url'))