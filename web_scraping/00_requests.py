import requests
import pprint

# GET request to google.com
response = requests.get('https://www.google.com')
print(response.status_code)
print(response.headers)
# print(response.text)

# Get request to HTTPBin Web API
response = requests.get('https://httpbin.org/get', params={'key': 'value'}) 
pprint.pprint(response.json())

