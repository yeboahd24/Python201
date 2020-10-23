#!usr/bin/env/python3

"""Compose Classes Instead of Nesting Many Levels of Built-in Types
	Eg: recording grades of student who names aren't know
"""
from collections import defaultdict

class SimpleGradebook(object):
	def __init__(self):
		self._grades = {}

	def add_student(self, name):
		self._grades[name] = []

	def report_grade(self, name, score):
		self._grades[name].append(score)

	def average_grade(self, name):
		grades = self._grades[name]
		return sum(grades) / len(grades)


# book = SimpleGradebook()
# book.add_student('Linux')
# book.report_grade('Linux', 90)
# print(book.average_grade('Linux'))


class BySubjectGradebook(object):
	def __init__(self):
		self._grades = {}  # Outer dict

	def add_student(self, name):
		self._grades[name] = defaultdict(list) # Inner dict
	
	def report_grade(self, name, subject, grade):
		by_subject = self._grades[name]
		grade_list = by_subject[subject]
		grade_list.append(grade)

	def average_grade(self, name):
		by_subject = self._grades[name]
		total, count = 0, 0
		for grades in by_subject.values():
			total += sum(grades)
			count += len(grades)
		return total / count

book = BySubjectGradebook()
book.add_student('Linux')
book.report_grade('Linux', 'Programming', 90)
book.report_grade('Linux', 'Math', 89)
print(book.average_grade('Linux'))