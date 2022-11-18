# Strings to Integers
# Write a function called convert_add that takes a list of strings as an argument and converts it to
# integers and sums the list. For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.

def convert_add(list1) -> int:
    b = []
    for i in list1:
        b.append(int(i))
    return sum(b)


print(convert_add(['1', '3', '5']))


# In this challenge, we use typecasting to convert the strings in the list into integers.
# Once they are converted, we use the built-in sum function to sum the integers in list b.


def convert_add(list1: list):
    list2 = []
    count = 0
    for i in list1:
        list2.append(int(i))
    for j in list2:
        count += j
    return count


print(convert_add(['1', '3', '5']))

# If you do not want to use the in-built sum() function, you can create a second for loop in
# the function that will iterate through list2 of integers. We add all the elements of list2 to the variable count.
