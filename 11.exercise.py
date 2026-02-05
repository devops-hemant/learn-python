#!/usr/bin/python3

'''
Exercise A: Sum of 1..N (for loop)
Ask the user for N and print the sum from 1 to N.
'''

num = int(input("Enter the Vaule on N Numebr: "))

j=0
for i in range(1, num+1):
    j += i
    
print(j)

