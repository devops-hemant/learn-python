#!/usr/bin/python3

'''
Task 1
Write a function:
Input: list of services
Output: number of "VM"
'''

services = ["kubernetes", "VM", "Disks", "VM", "RDS", "VM"]

# method 1
def counter_fun1(resources):
    return (resources.count("VM"))

# method 2
def counter_fun2(resources):
    count = 0
    for resource in resources:
        if resource == "VM":
            count += 1

    return(count)

print (counter_fun1(services))
print (counter_fun2(services))


'''
Task 2
Use try / except:
Ask user for a number
Print square of the number
Handle invalid input
'''
def squreprint():
    try:
        number = int (input("Enter a Number: "))
        print (number * number)
    except ValueError:
        print("Enter a vaild interger value")

squreprint()