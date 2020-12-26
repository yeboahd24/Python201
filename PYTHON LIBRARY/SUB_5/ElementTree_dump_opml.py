
# To visit all of the children in order, use iter() to create a generator that iterates over the
# ElementTree instance.


from xml.etree import ElementTree
import pprint
with open('podcasts.opml', 'rt') as f:
	tree = ElementTree.parse(f)
for node in tree.iter():
	print(node.tag)