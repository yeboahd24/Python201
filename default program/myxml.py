
def myxml(tagname, content='', **kwargs):
	"""The function has one mandatory parameter,
		one with a default, and '**kwargs'
	"""
	attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
	return f'<{tagname}{attrs}>{content}</{tagname}>'

print(myxml('p', 'hello world', a=1, b=2, c=3))