from urllib.parse import urlencode


# Encoding replaces special characters such as spaces to ensure they are passed to the
# server using a format that complies with the standard.

query_args = {
'q': 'query string',
'foo': 'bar',
}
encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)