from urllib.parse import unquote, unquote_plus

print(unquote('http%3A//localhost%3A8080/%7Ehellmann/'))
print(unquote_plus(
'http%3A%2F%2Flocalhost%3A8080%2F%7Ehellmann%2F'
))
