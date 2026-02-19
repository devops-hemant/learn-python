#!/usr/bin/python3

# import json

# with open("resources.json", "r") as file:
#     resources = json.load(file)

# for r in resources:
#     print(r["name"], "->", r["status"])


# import json

# with open("resources.json", "r") as file:
#     resources = json.load(file)

# for r in resources:
#     if r["status"] != "Running":
#         print("⚠ Alert:", r["name"], "is", r["status"])


# stopped_count = 0
# for r in resources:
#     if r["status"] == "Stopped":
#         stopped_count += 1

# print(f"total stopped resources number: {stopped_count}")


# import json

# filename="resources.json"

# try:
#     with open(filename, "r") as file:
#         data = json.load(file)
#         for i in data:
#             print(f"{i['name']} = {i['status']}")
# except FileNotFoundError:
#     print(f"❌ {filename} JSON file not found")
# except json.JSONDecodeError:
#     print(f"❌ {filename} Invalid JSON format")



# api_response = {
#     "subscription": "prod",
#     "resources": [
#         {"name": "aks-prod", "status": "Running"},
#         {"name": "web-prod", "status": "Stopped"}
#     ]
# }

# for i in api_response["resources"]:
#     if i["status"] == "Stopped":
#         print(f"Alert!!!! {i['name']} is {i['status']}")


import json

with open("resources.json", "r") as file:
    resources = json.load(file)

stopped_count = 0
for r in resources:
    if r["status"] == "Stopped":
        stopped_count += 1

print(f"total stopped resources number: {stopped_count}")

report = {
    "total_resources": len(resources),
    "stopped": stopped_count,
    "status": "FAIL" if stopped_count > 0 else "PASS"
}

with open("report.json", "w") as file:
    json.dump(report, file, indent=2)