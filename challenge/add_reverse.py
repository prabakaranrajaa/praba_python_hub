# Add and Reverse
# Write a function called add_reverse. This function takes two lists as 
# argument and adds each corresponding number, and reverses the outcome. 
# For example, if you pass [10, 12, 34] and [12, 56, 78]. Your code 
# should return [112, 22, 68]. If the two lists are not of equal lengths, 
# the code should return a message that "the lists are not of equal lengths".


def add_reverse(n:list, k:list): # Creating an empty list 
    new_list = []
    if len(n) == len(k):
        for i in range(0, len(n)):
    # adding and appending corresponding numbers 
            new_list.append(n[i] + k[i])
    # Reversing new list 
            new_list.reverse()
        return new_list 
    else:
        return f'Lists have different lengths'


# Lists to add and reverse 
list1 = [10, 12, 34]
list2 = [12, 56, 78]

print(add_reverse(list1, list2))


# Add and Reverse
# This challenge is best solved using the range() function. 
# The first step is to check if the list are of equal lengths; 
# we use the len() function for that. Once we confirm that the lists are of 
# equal lengths, we use the range function to get the index of each 
# element in the list. We then add and append the results to the empty 
# list we created. We then apply the list method reverse() to our new list,
# to reverse the content of the list.
