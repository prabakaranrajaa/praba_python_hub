# Difference of two Lists

# Write a function called difference that takes two lists as arguments. 
# This function should return all the elements that are in list a but not in 
# list b and all the elements in list b not in list
# a.	For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function.


def difference(arr1: list, arr2: list): # Find items in list 1 not in list 2
    list1 = [i for i in arr1 if i not in arr2 ] # Find items in list 2 one not in list 1 
    list2 = [j for j in arr2 if j not in arr1] # concatenate the two lists
    return 'The difference between two sets is ', list1 + list2

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))


# Difference of two Lists
# We use two list-comprehension statements, first one is to find the items in 
# list 1 not in list two and second one to find items in list 2 not in list 1

