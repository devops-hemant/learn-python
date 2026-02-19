#!/usr/bin/python3

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users =response.json()

# names = [user["name"] for user in users]
# print(names)

for user in users:
    print(user["name"])
else:
    print("API call Failed")