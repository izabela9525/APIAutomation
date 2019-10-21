import requests

# API url
url = "https://reqres.in/api/users?page=2"

# Send get Request
response = requests.get(url)
print(response)