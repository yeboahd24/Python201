# Once a ConfigParser is populated with the desired data, it can be saved to a file by calling
# the write() method. This approach can be used to provide a user interface for editing the
# configuration settings, without the need to write any code to manage the file.

import configparser
import sys
parser = configparser.ConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'dhellmann')
parser.set('bug_tracker', 'password', 'secret')
parser.write(sys.stdout)