#!usr/bin/env/python3


class DescriptorClass(object):
	"""All know that descriptor attributes should be in the class not the __init__
		instance--> this is the instance of your class, so in this case test and test1 becomes our instance
		owner--> this the name of class of the instance, ClientClass is now our owner here
	"""
	def __get__(self, instance, owner):
 		if instance is None:  # don't forget to add this
 			return f"{self.__class__.__name__}.{owner.__name__}"
 		return f"value for {instance}"


class ClientClass(object):
	descriptor = DescriptorClass()

test = ClientClass.descriptor  # calling ClientClass directly
test1 = ClientClass().descriptor
print(test)
print(test1)
