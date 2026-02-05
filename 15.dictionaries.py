#!/usr/bin/python3

# aks_cluster = {
#     "name": "myAKSCluster",
#     "location": "eastus",
#     "node_count": 3,
#     "kubernetes_version": "1.21.2",
# }

# print(aks_cluster["name"])
# print(aks_cluster["node_count"])


# for key, value in aks_cluster.items():
#     print(f"{key}: {value}")


# services = {
#     "aws": "running",
#     "azure": "stopped",
#     "gcp": "running",
#     "digitalocean": "stopped",
# }

# for service, status in services.items():
#     if status == "stopped":
#         print(f"⚠ Alert: {service} is stopped")
#     else:
#         print(f"{service} is running")


services_list=[ {"name": "aws", "status": "running"}, 
                {"name": "azure", "status": "stopped"}, 
                {"name": "gcp", "status": "running"}, 
                {"name": "digitalocean", "status": "stopped"} ]

# List of Dictionaries (Very Common Pattern)
for service in services_list:
    print (f"{service['name']} current service status: {service['status']}")

# tuples are read-only ordered collections of elements
regions = ("East US", "West Europe", "Central India")
print(regions[0])

#sets are unordered collections of unique elements
subscriptions = {"prod", "dev", "test", "prod"}
print(subscriptions)