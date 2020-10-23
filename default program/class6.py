#!usr/bin/env/python3

# Prefere class decorators over composable class extensions
# Using metaclass to automatically decorate all methods of a class
from functools import wraps
import types
trace_types = (
	types.MethodType,
	types.FunctionType,
	types.BuiltinFunctionType,
	types.BuiltinMethodType,
	types.MethodDescriptorType,
	types.ClassMethodDescriptorType
	)




def trace_func(func):
	if hasattr(func, 'tracing'): # Only decorate once
		return func
	@wraps
	def wrapper(*args, **kwargs):
		result = None
		try:
			result = func(*args, **kwargs)
			return result
		except Exception as e:
			result = e
			raise 
		finally:
			print(f'{func.__name__}({args!r}, {kwargs!r})' f'{result!r}')
		wrapper.tracing = True
		return wrapper


class TraceMeta(type):
	def __new__(meta, name, bases, class_dict):
		klass = super().__new__(meta, name, bases, class_dict)
		for key in dir(klass):
			value = getattr(klass,  key)
			if isinstance(value, trace_types):
				wrapped = trace_func(value)
				setattr(klass, key, wrapped)
		return klass




