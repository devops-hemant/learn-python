#!/usr/bin/python3

'''
Operator    Meaning
==          equal to
!=          not equal
>           greater than
<           less than
>=          greater or equal
<=          less or equal
'''

age = int(input("Enter your age: "))

if age >= 18:
    print("you are an adult.")
else:
    print("you are not an adult")


marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

age = 25
license = True

if age > 18 and license == True:
    print("you can drive the car.")
else:
    print("you can't drive the car yet.")


day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print(f"{day} is a Weekend!")