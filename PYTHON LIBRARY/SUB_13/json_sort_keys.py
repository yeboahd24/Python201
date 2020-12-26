# Another benefit of JSON over pickle is that JSON produces human-readable
# results. The dumps() function accepts several arguments to make the output even easier to
# decipher. For example, the sort_keys flag tells the encoder to output the keys of a dictionary
# in sorted—instead of random—order.


import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))
unsorted = json.dumps(data)
print('JSON:', json.dumps(data))
print('SORT:', json.dumps(data, sort_keys=True))
first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)
print('UNSORTED MATCH:', unsorted == first)
print('SORTED MATCH :', first == second)