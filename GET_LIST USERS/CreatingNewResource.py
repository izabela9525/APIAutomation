import requests
import json

url = "https://reqres.in/api/users"

response = requests.post(url)

# Read input JSON file

file = open('C:\\Users\\izabe\\Desktop\\API_tests', 'r')
json_input = file.read()
resquest_json = json.loads(json_input)

print(resquest_json)