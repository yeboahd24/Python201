# To pass a sequence of values using separate occurrences of the variable in the query string,
# set doseq to True when calling urlencode().

from urllib.parse import urlencode

query_args = {
'foo': ['foo1', 'foo2'],
}
print('Single :', urlencode(query_args))
print('Sequence:', urlencode(query_args, doseq=True))

