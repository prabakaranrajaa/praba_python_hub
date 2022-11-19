# Sum the List

# Write a function called sum_list with one parameter that takes a nested 
# list of integers as an argument and returns the sum of the integers. 
# For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an 
# argument your function should return a sum of 33.


def sum_list(lst1: list): 
    counta = 0
    for items in lst1: 
        for i in items:
            counta += i
    return 'The sum is ', counta


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))




# In this exercise, we use the for loop to flatten the nested lists. 
# We have created a variable called counta. Every number in the list is 
# added to the count. 
# By the end of the iteration, 
# all the numbers will be added to the counter.