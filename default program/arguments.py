#!usr/bin/env/python3
# arguments are passed by values


def foo(argument):
    argument += ' in function'
    return argument


immutable = 'hello'
mutable = list('hello')
print(foo(mutable))  # same as
print(mutable)  # this because it is mutable


def packing(first, second, third):
    print(first)
    print(second)
    print(third)
    
l = [1, 2, 3]
# packing(l) # doing it this way gives and error so we need to pack it with the *
packing(*l)  # no error
# this is equivalent to, a, b, c = [1, 2, 3]


