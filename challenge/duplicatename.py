# Duplicate Names
# Write a function called check_duplicates that takes a list of strings as an argument.
# The function should check if the list has any duplicates. If there are duplicates,
# the function should return the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below should return apple as a duplicate and
# list of names should return "no duplicates".

# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates(arr: list):
    for item in arr:
        # Using count to find items more than one
        if arr.count(item) > 1:
            return item
        else:
            return 'No duplicates'


# lists
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))


# Duplicate Names
# Below we use a for loop and a conditional statement to iterate over a list and
# check if there are items in the list that appear more than once. We use the list method count() each item.
# Once we find that item, we return it.
