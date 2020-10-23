#!usr/bin/evn/python3

# The use of generic typing
# This method is good for database connection

class LazyRecord(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		value = f"Value for {name}"
		setattr(self, name, value)

		return value


class LoggingLazyRecord(LazyRecord):
	def __getattr__(self, name):
		print(f'* Called __getattr({name!r})', f'populating instance dictionary')
		result = super().__getattr__(name)
		print(f'* Returning{result!r}')
		return result



# data = LazyRecord()
# print('Before:', data.__dict__)      # Here I access the missing property foo. This causes Python to call the __getattr__
# print('foo:', data.foo)				# method above which mutatate the instance dictionary__dict__
# print('After:', data.__dict__)

# data = LoggingLazyRecord()
# print('exist:', data.exists)
# print('First foo: ', data.foo)   # This behaviour is specially helpful for use cases like lazily accessing
# print('Second: ', data.foo)		# schemaless data.__getattr__ runs a property.


class ValidatingRecord(object):
	def __init__(self):
		self.exists = 5

	def __getattribute__(self, name):
		print(f'* Called __getattribute__{name!r}')
		try:
			value = super().__getattribute__(name)
			print(f'*Found {name!r}, returning {value!r}')
			return value
		except AttributeError:
			value = f'Value for {name}'
			print(f'* Setting {name!r} to {value!r}')
			setattr(self, name, value)
			return value

# data = ValidatingRecord()
# print('exists: ', data.exists)
# print('First foo: ', data.foo)
# print('Second foo: ', data.foo)

# class MissingPropertyRecord(object):
# 	def __getattr__(self, name):
# 		if name == 'bad_name':
# 			raise AttributeError(f'{name} is missing')

# data = MissingPropertyRecord()
# print(data.bad_name)


class SavingRecord(object):
	def __setattr__(self, name, value):
		# Save some data for the record
		super().__setattr__(name, name)


class LoggingSavingRecord(SavingRecord):
	def __setattr__(self, name, value):
		print(f'* Called __setattr__({name!r}, {value!r})')
		super().__setattr__(name, value)


data = LoggingSavingRecord()
print('Before: ', data.__dict__)
data.foo = 5
print('After: ', data.foo)