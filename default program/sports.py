# import requests
# import json

# base_url = "api.football-data.org"
# headers = { 'X-Auth-Token': 'd2e5987515e94e32a79668baf2f5f260'}


import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'd2e5987515e94e32a79668baf2f5f260'}

connection.request('GET', '/v2/competitions/2018', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response['name'])
print(response['seasons'])