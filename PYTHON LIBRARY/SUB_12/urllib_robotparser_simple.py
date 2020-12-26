# robotparser implements a parser for the robots.txt file format, including a function that
# checks whether a given user agent can access a resource. It is intended for use in well-behaved
# spiders, or other crawler applications that need to be throttled or otherwise restricted.

from urllib import parse
from urllib import robotparser

AGENT_NAME = 'PyMOTW'
URL_BASE = 'https://pymotw.com/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()
PATHS = [
'/',
'/PyMOTW/',
'/admin/',
'/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
	print('{!r:>6} : {}'.format(
	parser.can_fetch(AGENT_NAME, path), path))
	url = parse.urljoin(URL_BASE, path)
	print('{!r:>6} : {}'.format(
	parser.can_fetch(AGENT_NAME, url), url))
	print()
