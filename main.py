#!/usr/bin/python3

# import json

# with open("resources.json", "r") as file:
#     resources = json.load(file)

# for r in resources:
#     print(r["name"], "->", r["status"])


import json

with open("resources.json", "r") as file:
    resources = json.load(file)

for r in resources:
    if r["status"] != "Running":
        print("⚠ Alert:", r["name"], "is", r["status"])