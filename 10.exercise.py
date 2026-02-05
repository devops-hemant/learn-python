# #!/usr/bin/python3
# '''
# Write a program that:

# Asks the user for a number
# Checks if the number is:

# Positive
# Negative
# Zero
# Even
# Odd
# '''


# # number_value=int(input("Enter a number: "))


# while True:
#     user_input = input("Enter a number: ")
#     try:
#         number_value = int(user_input)  #float(user_input) for decimals
#         break
#     except ValueError:
#         print("Please enter a valid integer (e.g., -3, 0, 42).")


# if number_value > 0 :
#     sign = "positive"
# elif number_value < 0 :
#     sign = "negative"
# else:
#     sign = "zero"

# if number_value == 0:
#     print(f"{number_value} is zero(even)")
# else:
#     parity = "even" if number_value % 2 == 0 else "odd"
#     print(f"{number_value} is {sign} and {parity}.") 