import requests
from functools import lru_cache
from requests import HTTPError

@lru_cache(maxsize=24)
def get_webpage(module):
	"""
	Get specific Python module web pages
	"""
	webpage = f'https://docs.python.org/3/library/{module}'
	try: 
		with requests.get(webpage) as pages:
			return pages.content
	except HTTPError:
		return None


if __name__ == '__main__':
	modules = ['functools', 'collections', 'os', 'sys', 'stdtypes']
	for module in modules:
		pages = get_webpage(module)
	if pages:
		found = f'module page found {module}'
		print(found)

