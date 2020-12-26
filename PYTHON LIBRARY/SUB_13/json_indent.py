import json

# When indent is a non-negative integer, the output more closely resembles that of pprint
# with leading spaces for each level of the data structure matching the indent
# level.

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))
print('NORMAL:', json.dumps(data, sort_keys=True))
print('INDENT:', json.dumps(data, sort_keys=True, indent=2))