
# When creating an application that will access web resources owned by someone else, the courteous
# approach is to include real user agent information in the requests, so they can identify the
# source of the hits more easily.


from urllib import request
r = request.Request('http://localhost:8080/')
r.add_header(
'User-agent',
'PyMOTW (https://pymotw.com/)',
)
response = request.urlopen(r)
data = response.read().decode('utf-8')
print(data)
