# Division and Square-root
# Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5,
# returns its remainder if it is not divisible by 5.	For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

def divide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return f'The square-root of the number is {sq_root}'
    else:
        remainder = number % 5
        return f'The remainder of the division is {remainder}'


print(divide_or_square(19))


# we use conditional statements to create two conditions. If any of those conditions evaluate to True,
# that block of code will be executed. The if statement checks if the number is divisible by 5, if it is,
# we calculate the square root of the number. The else statement will execute only if the number is not divisible by 5.
# In that case, the else block will return the remainder of the division.
