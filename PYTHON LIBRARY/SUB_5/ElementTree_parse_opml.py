from xml.etree import ElementTree
with open('podcasts.opml', 'rt') as f:
	tree = ElementTree.parse(f)
print(tree)


# This method will read the data, parse the XML, and return an ElementTree object.