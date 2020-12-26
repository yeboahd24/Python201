'''In situations where a namedtuple is created based on values outside the control of the
program (such as to represent the rows returned by a database query, where the schema
is not known in advance), the rename option should be set to True so the invalid fields are
renamed.
The new names for renamed fields depend on their index in the tuple, so the field with
name class becomes _1 and the duplicate age field is changed to _2.
'''


import collections

# with_class = collections.namedtuple(
# 'Person', 'name class age',
# rename=True)
# print(with_class._fields)
# two_ages = collections.namedtuple(
# 'Person', 'name age age',
# rename=True)
# print(two_ages._fields)


Person = collections.namedtuple('Person', 'name age')
bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)
print('As Dictionary:', bob._asdict()) # as dict
print('\nBefore:', bob)

bob2 = bob._replace(name='Robert') # replacing
print('After:', bob2)
print('Same?:', bob is bob2)
