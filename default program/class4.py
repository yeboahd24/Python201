#!usr/bin/env/ptyhon3

# The use of decriptors as a boilerplate
# using weakref to prevent memory leakage
from weakref import WeakKeyDictionary
class Grade(object):
	def __init__(self):
		self._values = WeakKeyDictionary()

	def __get__(self, instance, instance_type):
		if instance is None:
			return self
		return
		self._values.get(instance, 0)

	def __set__(self, instance, value):
		if not(0 <= value <= 100):
			raise  ValueError('Grade must be between 0 and 100')
		self._values[instance] = value



class Exam(object):
	def __init__(self):
		self._writing_grade = 0

	@staticmethod
	def _check_grade(value):
		if not(0 <= value <= 100): # using this as a validator
			raise ValueError('Grade must be between 0 and 100')

	@property
	def writing_grade(self):
		return self._writing_grade

	@writing_grade.setter
	def writing_grade(self, value):
		self._check_grade(value)
		self._writing_grade = value

	@property
	def math_grade(self):
		return self._math_grade

	@math_grade.setter
	def math_grade(self, value):
		self._check_grade(value)
		self._math_grade = value


class Exam(object):
	def __init__(self):
		math_grade =Grade()
		science_grade = Grade()


first_exam = Exam()
first_exam.math_grade = 90
print('Maths:', first_exam.math_grade)
first_exam.science_grade = 99
print('Science:', first_exam.science_grade)
# print('First Exams')
# print(first_exams._writing_grade)
# print('Second Exams')
# print(second_exam._writing_grade)
# third_exams = Exam()
# third_exams.math_grade = 97
# fourth_exams = Exam()
# fourth_exams.writing_grade


"""Note: Use WeakKeyDictionary to ensure that your descriptor classes don't cuase memory leaks"""