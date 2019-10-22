import requests
import json

# API url
url = "https://reqres.in/api/users?page=2"

# Send get Request
response = requests.get(url)

#Validate status code
assert response.status_code == 200

# Fetch responese header
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

# Fetch cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

print(response.elapsed)

