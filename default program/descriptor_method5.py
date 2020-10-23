class SharedDataDescriptor:
	def __init__(self, initial_value):
		self.value = initial_value

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return self.value

	def __set__(self, instance, value):
		self.value = value

class ClientClass:
	descriptor = SharedDataDescriptor("first value")

client1 = ClientClass()
print(client1.descriptor)  # first value
client2 = ClientClass()
print(client2.descriptor) # first value because they shared common descriptor
client2.descriptor = "value for client 2"  
print(client1.descriptor) # value for client2
print(client2.descriptor) # value for client2 because change in the other affect the other is like mutable objects

"""In other to avoid this you have to use __dict__ magic method in your SharedDataDescriptor"""


# if you don't wanna use __dict__ you can use WeakKeyDictionary

from weakref import WeakKeyDictionary

class DescriptorClass:
	def __init__(self, initial_value):
		self.value = initial_value
		self.mapping = WeakKeyDictionary()

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return self.mapping.get(instance, self.value)

	def __set__(self, instance, value):
		self.mapping[instance] = value

