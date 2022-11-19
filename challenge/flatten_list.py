# Flatten the List
# Write a function called flat_list that takes one argument, a nested list. 
# The function converts the nested list into a one- dimension list. 
# For example [[2,4,5,6]] should return [2,4,5,6].

def convert_list(lst1: list): 
    list1 = []
    for items in lst1:
        for i in items:
            list1.append(i) 
    return list1


print(convert_list([[[2, 4, 5, 6]]]))


# Notice how we use nested for loops in the code below? 
# The first for loop access the outer list, and the inner for loop 
# access the inner list. 
# Once we access the elements of the inner list,
# we append them to list1. With this small code, we have flattened the list.