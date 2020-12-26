# If the path being joined to the URL starts with a slash (/), urljoin() resets the URL’s
# path to the top level. If it does not start with a slash, the new path value is appended to
# the end of the existing path for the URL.


from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/',
'/subpath/file.html'))
print(urljoin('http://www.example.com/path/',
'subpath/file.html'))