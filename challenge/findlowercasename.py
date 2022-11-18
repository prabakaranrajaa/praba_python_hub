#  Lowercase Names

# names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

# You are given a list of names above. This list is made up of names of lowercase and uppercase letters.
# Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters.
# Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return:

# ('kerry', 'dickson', 'carol', 'adam')


names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

# creating an empty list
d = []
# Using sorted function to sort list in descending order
for name in sorted(names, reverse=True):
    if name.islower():
        d.append(name)
        tuple_names = tuple(d)

print(tuple_names)


# Lower case names
# For this challenge, we have to use two functions, the sorted function and the tuple function.
# The sorted function will sort the list in descending order.
# To sort a list in descending order, set reverse to True.
