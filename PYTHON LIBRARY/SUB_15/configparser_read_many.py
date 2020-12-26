from configparser import ConfigParser
import glob

parser = ConfigParser()
candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
'simple.ini', 'multisection.ini']
found = parser.read(candidates)
missing = set(candidates) - set(found)
print('Found config files:', sorted(found))
print('Missing files :', sorted(missing))