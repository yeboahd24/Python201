#!usr/bin/env/python3

"""Descriptor in action"""

# This class track all current cities without using descriptor method

# class Traveller(object):
# 	def __init__(self, name, current_city):
# 		self.name = name
# 		self._current_city = current_city
# 		self._cities_visited = [current_city]

# 	@property
# 	def current_city(self):
# 		return self._current_city

# 	@current_city.setter
# 	def current_city(self, new_city):
# 		if new_city != self._current_city:
# 			self._cities_visited.append(new_city)
# 		self._current_city = new_city  # update current city

# 	@property
# 	def cities_visited(self):
# 		return self._cities_visited

# alice = Traveller("Alice", "Barcelona")
# alice.current_city = "Paris"
# alice.current_city = "Brussels"
# alice.current_city = "Amsterdam"
# print(alice.cities_visited)



# using descriptors

class HistoryTracedAttribute:
	def __init__(self, trace_attribute_name) -> None:
		self.trace_attribute_name = trace_attribute_name # [1]
		self._name = None

	def __set_name__(self, owner, name):
		self._name = name

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return instance.__dict__[self._name]

	def __set__(self, instance, value):
		self._track_change_in_value_for_instance(instance, value)
		instance.__dict__[self._name] = value


	def _track_change_in_value_for_instance(self, instance, value):
		self._set_default(instance) # [2]
		if self._needs_to_track_change(instance, value):
			instance.__dict__[self.trace_attribute_name].append(value)


	def _needs_to_track_change(self, instance, value) -> bool:
		try:
			current_value = instance.__dict__[self._name]
		except KeyError: # [3]
			return True

		return value != current_value # [4]


	def _set_default(self, instance):
		instance.__dict__.setdefault(self.trace_attribute_name, []) # [6]



class Traveller:
	current_city = HistoryTracedAttribute("cities_visited") # [1]
	def __init__(self, name, current_city):
		self.name = name
		self.current_city = current_city # [5]

