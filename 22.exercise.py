#!/usr/bin/python3

# Task 1
import json

with open("resources.json", "r") as resources:
    data = json.load(resources)
    for resource in data:
        if resource["type"] == "AKS" :
            print(f"{resource['name']}")

# aks_resources = [
#     r["name"] for r in data
#     if r.get("type") == "AKS"
# ]

# print(aks_resources)

# Task 2

import json

stopped_count=0
with open("resources.json", "r") as resources:
    data = json.load(resources)
    for resource in data:
        if resource["status"] == "Stopped":
            stopped_count+=1

print(stopped_count)
print (len(data))

if stopped_count > 0:
    result = "FAIL"
else:
    result = "PASS"

report= {
    "total": len(data),
    "stopped": stopped_count,
    "status": result
}

with open("summary.json", "w") as file:
    json.dump(report, file, indent=2)

# Task 3

with open("resources.json", "r") as resources:
    data = json.load(resources)
    for resource in data:
        if resource["type"] == "AKS" and resource["status"] == "Stopped":
            print("CRITICAL: Kubernetes down")
        # else:
        #     print("Kubernetes Up")


# import json

# with open("resources.json", "r") as resources:
#     data = json.load(resources)

# critical = any(
#     r.get("type") == "AKS" and r.get("status") == "Stopped"
#     for r in data
# )

# if critical:
#     print("🚨 CRITICAL: Kubernetes down")
# else:
#     print("✅ Kubernetes healthy")