#!usr/bin/env/python3
"""class compostion allows explecit relations between objects."""

class Country(object):
	def __init__(self):
		self.cities = []

	def addCity(self, city):
		self.cities.append(city)


class City(object):
	def __init__(self, numPeople):
		self.people = []
		self.numPeople = numPeople

	def addPerson(self, person):
		self.people.append(person)

	def join_country(self, country):
		self.country = country
		country.addCity(self)

		for i in range(self.numPeople):
			Person(i).join_city(self)

class Person(object):
	def __init__(self, ID):
		self.ID = ID

	def join_city(self, city):
		self.city = city
		city.addPerson(self)

	def people_in_my_country(self):
		x = sum([len(c.people) for c in self.city.country.cities])
		return x

US = Country()
NYC = City(10).join_country(US)
SF = City(5).join_country(US)

print(US.cities[0].people[0].people_in_my_country())  # 15

