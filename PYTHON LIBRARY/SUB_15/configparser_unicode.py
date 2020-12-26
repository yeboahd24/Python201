from configparser import ConfigParser

parser = ConfigParser()
# Open the file with the correct encoding.
parser.read('unicode.ini', encoding='utf-8')
password = parser.get('bug_tracker', 'password')
print('Password:', password.encode('utf-8'))
print('Type :', type(password))
print('repr() :', repr(password))