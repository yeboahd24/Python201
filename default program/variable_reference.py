import copy
"""Understanding variable reference
	using mutable and immutabel data structures
	Eg:
		mutable = [1,2,3]
		immutable = (1,2,3)
"""

mutable = [1,2,3,4,5,8]
immutable = [5,8,13,21]

mutable_b = mutable # two objects refereces to same object
immutable_b = immutable

# print(mutable_b is mutable) # True
# print(immutable_b is immutable)  # True

# changing one of the references
mutable += [mutable[-2] + mutable[-1]]
immutable += (immutable[-2] + immutable[-1],)

print(mutable_b is mutable)  # changing one part affect the other
print(immutable_b is immutable) # this remain the same because is unchangerble

# creating shallow copy
some_dict = {'a': [1,1,2,3]}
another_dict = some_dict.copy()
# print(another_dict) # this make clone of some_dict
# print(id(some_dict['a']) == id(another_dict['a'])) # True 

# creating deepcopy

another_dict = copy.deepcopy(some_dict) # this create a copy of no reference
some_dict['a'].append(5)
print(some_dict) # {'a': [1,1,2,3,5]}
print(another_dict) # {'a': 1,1,2,3}

# let see what happens after we update
print(id(some_dict['a']) == id(another_dict['a'])) # False 



