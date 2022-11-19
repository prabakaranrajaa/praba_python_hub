# Swap Values
# Write a function called swap_values.
# This function takes a list of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your function should return
# [7, 4, 67, 2].

def swap_values(arr: list):
    # Create a variable for first number
    first_number = arr[0]
# Create a second variable for the last number
    last_number = arr[-1]
# assign last number to index 1
    arr[0] = last_number
# assign first number to index -1
    arr[-1] = first_number
    return arr


list1 = [2, 4, 67, 7]
print(swap_values(list1))

# Swap Values
# The easy way to solve this challenge, would be to create separate variables for the numbers
# that you want to swap. Use list slicing to get the values.
