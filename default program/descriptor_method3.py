#!usr/bin/env/python3

class ProtectedAttribute(object):
	def __init__(self, requires_role = None) -> None:
		self.permission_required = requires_role
		self._name = None


	def __set_name__(self, owner, name):
		self._name = name

	def __set__(self, user, value):
		if value is None:
			raise ValueError(f"{self._name} can't be set None")
		user.__dict__[self._name] = value

	def __delete__(self, user):
		if self.permission_required in user.permissions:
			user.__dict__[self._name] = None
		else:
			raise ValueError(f"User {user!s} doesn't have {self.permission_required}")


class User(object):
	"""Only users with "admin" privileges can remove their email address."""
	email = ProtectedAttribute(requires_role="admin")

	def __init__(self, username: str, email: str, permission_list: list = None) -> None:
		self.username = username
		self.email = email
		self.permissions = permission_list or []

	def __str__(self):
		return self.username


admin = User("root", "root@d.com", ["admin"])
user = User("user", "user1@d.com", ["email", "helpdesk"])
print(admin.email)
del admin.email
print(admin.email)  # None
print(admin.email is None) # True
print(user.email)
# user.email = None  # Error




"""Normal descriptor without __set_name__"""

# class DescriptorNameWriter(object):
# 	def __init__(self, name):
# 		self._name = name

# 	def __get__(self, instance, value):
# 		if instance is None:
# 			return self
# 		instance.__dict__[self._name] = value

# 	def __set__(self, instance, value):
# 		instance.__dict__[self._name] = value

# class ClientClass(object):
# 	descritptor = DescriptorNameWriter('descriptor')

# client = ClientClass()
# client.descriptor = 'Value'
# print(client.descriptor)




# class DescriptorNameWriter(object):
# 	def __init__(self, name = None):
# 		self.name = name

# 	def __set_name__(self, owner, name):
# 		self.name = name  # This makes it more pythonic, if we used this we don't have to use __set__ method again

# 	def __get__(self, instance, value):
# 		if instance is None:
# 			return self
# 		instance.__dict__[self.name] = value

	# def __set__(self, instance, value):
	# 	instance.__dict__[self.name] = value



# class ClientClass(object):
# 	descriptor = DescriptorNameWriter()

# client = ClientClass()
# client.descriptor = 'linux'
# print(client.descriptor)




"""Non Data Descriptor: is a descriptor with __get__ method only"""

# class NonDataDescriptor:
# 	def __get__(self, instance, owner):
# 		if instance is None:
# 			return self
# 		return 42

# class ClientClass:
# 	descriptor = NonDataDescriptor()

# client = ClientClass()
# print(client.descriptor)
# client.descriptor = 90
# print(client.descriptor)
# del client.descriptor  # deleting will only delete the 90 that you set
# print(client.descriptor) # return 42 which is the default value


"""Data Descriptor: is a descriptor with __get__ and __set__ method implemented"""


class DataDescriptor:
	def __get__(self, instance, owner):
		if instance is None:
			return self
		return 42


	def __set__(self, instance, value):
		# logger.debug("setting %s.descriptor to %s", instance, value)
		instance.__dict__["descriptor"] = value

class ClientClass:
	descriptor = DataDescriptor()


client = ClientClass()
print(client.descriptor)
client.descriptor = 99
print(client.descriptor) # returns 42 again becuase it override
# del client.descriptor # error because __delete__ method is not implemented



		
# x = 'foo ba'
# y = [(i.upper(), len(i)) for i in x]
# print(y)