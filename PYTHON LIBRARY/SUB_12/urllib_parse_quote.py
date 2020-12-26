# Special characters within the query arguments that might cause parse problems with the
# URL on the server side are “quoted” when passed to urlencode(). To quote them locally
# to make safe versions of the strings, use the quote() or quote_plus() function directly.


from urllib.parse import quote, quote_plus, urlencode

url = 'http://localhost:8080/~hellmann/'
print('urlencode() :', urlencode({'url': url}))
print('quote() :', quote(url))
print('quote_plus():', quote_plus(url))