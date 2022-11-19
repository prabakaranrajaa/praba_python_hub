# Unique Numbers
# Write a function called unique_numbers that takes a list of numbers as an argument. 
# Your function is going to find all the unique numbers in the list. 
# It will then sum up the unique numbers. You will calculate the difference between
# the sum of all the numbers in the original list and the sum of unique 
# numbers in the list. If the difference is an even number, 
# your function should return the original list.
# If the difference is an odd number, your function should return a list with
# unique numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
# return [1, 2, 4, 5, 6, 7, 8, 8].

def uniq_numbers(a: list): 
    list1 = []
    for number in a:
        if number not in list1: 
            list1.append(number)
            print(list1)
    dif = sum(a) - sum(list1) 
    if dif % 2 == 0:
        return list1
    else:
        return a


print(uniq_numbers([1, 2, 4, 5, 6, 7, 8]))


# For this challenge, once we append the unique numbers to list1, 
# we use the sum() function to sum the original list(a) and 
# the list with unique numbers, (list1). We use the modulus operator(%) to 
# check if the difference between the two numbers, is an even number or an odd number.