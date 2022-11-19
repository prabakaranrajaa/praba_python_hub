# Create a Nested List
# Write a function called nested_lists that takes any number of lists and 
# creates a 2-dimensional nested list of lists. For example, if you pass 
# the following lists as arguments: [1, 2, 3, 5], [1, 2, 3,
# 4], [1, 3, 4, 5].
# Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]

def nested_lists(*args: list): 
    list1 =[]
    for i in range(len(args)): 
        for j in args:
            list1.append(j) 
            break

    return list1


print(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))


# Create a Nested List
# The first thing is we pass *args as a parameter to ensure that our function 
# can take any number arguments. Then we create an empty list to append the lists to.
# We use the range to keep track of the number lists passed as argument.
# We use the for loop to iterate through the lists and append them to the empty list.
