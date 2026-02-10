#!/usr/bin/python3

# with open("app.log", "r") as file:
#     content = file.read()
#     print(content)


# with open("app.log", "r") as file:
#     for line in file:
#         print (line.casefold().strip())


# with open("app.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             print(f"❌ {line.strip()}")



# error_count = 0

# with open("app.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             error_count += 1

# print("Total errors:", error_count)


# with open("report.log", "w+") as file:
#     file.write("I am the first line\n")
#     file.write("I am the second line\n")

#     file.seek(0)  # move cursor to beginning
#     content=file.read()
#     print(content)

# with open("report.log", "r") as file:
#     for line in file:
#         print (line.strip())


# # to append the Data

# with open("report.log", "a") as file:
#     file.write("I am a new line\n")

# with open("report.log", "r") as file:
#     for line in file:
#         print (line.strip())

# try:
#     with open("missing.log", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found!")


# env=prod
# region=centralindia
# replicas=3


with open("config.txt", "w+") as file:
    file.write("env=prod\nregion=centralindia\nreplicas=3")
    file.seek(0)
    content=file.read()
    print(content)
    
config = {}

with open("config.txt", "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        config[key] = value

    print(config)
