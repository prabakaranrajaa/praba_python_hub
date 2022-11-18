# Biggest Odd Number
# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
# For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension.


def biggest_odd(string1: str):
    odd_nums = [i for i in string1
                if int(i) % 2 != 0]
    return f' The biggest old number is {max(odd_nums)}'


print(biggest_odd('23569'))


# Using list-comprehension, we use a for loop and if statement to return a list of odd numbers.
# Here you get to use the modulus operator (%). The modulus operator returns the remainder of a division.
# If the remainder is zero, the operator returns a zero. A number is odd if it returns a remainder when divided by 2.
# In this code, we use the if statement to return only numbers that are not divisible by 2.
# The max() function will return the biggest odd number in the list.
