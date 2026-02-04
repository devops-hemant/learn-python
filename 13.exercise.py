#!/usr/bin/python3

'''
Exercise C: Count vowels in a string
Use a for loop over a string and count vowels a e i o u (case‑insensitive).
'''
line = input("Enter a text line: ")

for l in line:
    if l.lower() in "aeiou":
        print(f"{l} is Vowel")

    

    
