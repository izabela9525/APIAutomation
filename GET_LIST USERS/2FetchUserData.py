import json

import jsonpath
import requests

# API url
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

json_response = json.loads(response.text)
# print(json_response)

# pages = jsonpath.jsonpath(json_response, 'total_pages')
# assert pages[0] == 2

# For is take all user names and print it
for i in range(0, 3):

    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print((first_name[0]))
