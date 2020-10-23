#!usr/bin/env/python3
from functools import wraps
import re
import time

""":key ,Courses, Profile
    Courses: display the semester courses
    Profile: check if all requirements are met if met then display the courses
"""

SemesterCourses = ['Programming', 'CompSkills', 'System Analysis', 'Statistics', 'PC Hardware and maintenance',
                   'Digital Electronics']

INDEX_FORMAT = ("UED\d{7}")


class Courses(object):
    @staticmethod
    def semester_courses():
        return '\n'.join(f"({index} {values.title()} " for index, values in enumerate(SemesterCourses, start=1))


class Profile(object):
    def __init__(self, program, index):
        self.program = program.lower()
        self.index = index.upper()

    def login_user_courses(self):
        valid = re.compile(INDEX_FORMAT)
        group = re.fullmatch(valid, self.index)
        if group:
            if self.program == 'computer science':
                print('Courses loading...')
                time.sleep(1.0)
                print(" ")
                return Courses.semester_courses()

            else:
                return f'invalid program name: {self.program}'
        else:
            return f'invalid index number: {self.index}'


p = Profile('Computer science', 'UED2900219')
print(p.login_user_courses())
