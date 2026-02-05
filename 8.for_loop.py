#!/usr/bin/python3


#!/usr/bin/python3


# Print numbers 0 to 4
for i in range(5):
    print(i)

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Step by 2 (1, 3, 5, 7, 9)
for i in range(1, 10, 2):
    print(i)




# Over a dictionary
person = {"name": "Hemant", "city": "Bengaluru", "role": "Contractor"}
for key in person:
    print(key, "->", person[key])

# Better: items()
for key, value in person.items():
    print(key, "=", value)



names = ["Asha", "Rahul", "Meera"]
for idx, name in enumerate(names, start=1):
    print(f"{idx}: {name}")


# # Over a dictionary
person = {"name": "Hemant", "city": "Bengaluru", "role": "Contractor"}

for idx, (key, value) in enumerate( person.items(), start=1 ) :
    print(idx, key, "=", value)


products = ["Pen", "Book", "Bottle"]
prices = [10, 120, 250]

for item, price in zip(products, prices):
    print(f"{item}: ₹{price}")



# break: stop the loop early
for n in range(1, 10):
    if n == 5:
        break
    print(n)  # prints 1..4

# continue: skip current iteration
for n in range(1, 6):
    if n == 3:
        continue
    print(n)  # prints 1, 2, 4, 5

# else on loops: runs if loop didn't break
for n in range(1, 5):
    if n == 100:
        break
else:
    print("Finished loop without break.")


# break: stop the loop early
for n in range(1, 10):
    if n == 5:
        break
    print(n)  # prints 1..4

# continue: skip current iteration
for n in range(1, 6):
    if n == 3:
        continue
    print(n)  # prints 1, 2, 4, 5

# else on loops: runs if loop didn't break
for n in range(1, 5):
    if n == 100:
        break
else:
    print("Finished loop without break.")



# Squares of 1..5
squares = [n*n for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Filter + transform: even squares up to 10
even_squares = [n*n for n in range(1, 11) if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]



'''
Common Pitfalls (and how to avoid them)

Infinite loop: Forgetting to update the counter in a while loop.
Modifying a list while iterating: iterate over a copy or build a new list.
'''
nums = [1, 2, 3, 4]
for n in nums[:]:  # iterate over a copy
    if n % 2 == 0:
        nums.remove(n)
