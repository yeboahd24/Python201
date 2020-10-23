#!usr/bin/env/python3

# callable object is when making a object like a function
# implementing callable object with __call__
from collections import defaultdict, UserDict


class Callable(object):
    def __init__(self, count):
        self._count = defaultdict(int)

    def __call__(self, *args, **kwargs):
        self._count[args] += 1
        return self._count[args]


# call = Callable(1)
# print(call())
# print(call())
# print(call())
#
# class Test(UserDict):
#
#     def __getitem__(self, item):
#         value = super().__getitem__(item)  # do not forget to call the super function
#         if value.startswith('pa'):
#             return f'guessing to be parrot or not {value}'
#         return value

# t = Test()
# t['os'] = 'parrot'
# print(t['os'])
