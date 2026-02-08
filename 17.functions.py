#!/usr/bin/python3

# def greet(text):
#     print(f"Hello to {text}")

# greet("Hemant")


# def counting(services):
#     aks_count = 0
#     for service in services:
#         if service == "AKS":
#             aks_count += 1
#     return aks_count

# services = [ "AKS", "AWD", "AWS", "AKS", "AMK" ]

# print(counting(services))

# try:
#     age = int(input("Enter your age: "))
#     print(f"your age is : {age}")
# except ValueError:
#     print("Please enter a number")


# resource = {
#     "name": "Hemant",
#     "address": "Unknown",
#     "profession" : "DevOps Engineer with killer skills"
# }

# attriburte = input("Enter the attriburte name to search: ")

# try:
#     print(resource[f"{attriburte}"])
# except KeyError:
#     print("Enter a vaild attriburte Key")

# # Multiple Exceptions (Professional)
# try:
#     value = int("abc")
# except ValueError:
#     print("Invalid number")
# except Exception as e:
#     print("Unexpected error:", e)

# # finally (Always Executes)
# try:
#     print("Checking service")
# except:
#     print("Error")
# finally:
#     print("Cleanup done")



# def servicecheck(services):
#     try:
#         for service, status in services.items():
#             if status == "Running":
#                 print (f"{service} is {status}")
#     except AttributeError:
#         print ("Invalid services data")

# services_status = {
#     "AWS" : "Stopped",
#     "Azure" : "Running",
#     "GCP" : "Running"
# }

# servicecheck(services_status)

# def check_services_status(services):
#     try:
#         for service, status in services.items():
#             if status != "Running":
#                 print("⚠ Alert:", service, "is", status)
#     except AttributeError:
#         print("Invalid services data")

# services_status = {
#     "AKS": "Running",
#     "WebApp": "Stopped",
#     "CosmosDB": "Running"
# }

# check_services_status(services_status)