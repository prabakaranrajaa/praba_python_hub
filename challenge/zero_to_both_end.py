# Zero Both ends
# Write a function called zeroed code that takes a list of numbers as an argument.
# The code should zero (0) the first and the last number in the list. For example,
# if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].

list1 = [2, 5, 7, 8, 9]


def zeroed(arr: list) -> list:
    # Access and modify the first element
    arr[0] = 0
# Access and modify the last element
    arr[-1] = 0
    return arr


print(zeroed(list1))

# Zero Both ends
# This challenge requires a little slicing. Just access the first element and
# the last element in the list, and replace them with zeros.
