# Set or list
# You want to implement a code that will search for a number in a range. You have a decision to make as to whether to store the number in a set or a list. Your decision will be based on time. You have to pick a data type that executes faster.
# You have a range and you can either store it in a set or a list depending on which one executes faster when you are searching for a number in the range. See below:
# a = range(10000000) x = set(a)
# y = list(a)
# Let’s say you are looking for a number 9999999 in the range above. Search for this number in the list and the set. Your challenge is to find which code executes faster. You will pick the one that executes quicker, lists, or sets. Run the two searches and time them.

import timeit

# Testing the speed of execution in a set 
speed_test = '''
a = range(1000) 
b = set(a)
i = 999999

for i in b:
    print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))




# Set vs list
# To test the speed of the code, we are going to use the timeit function for both codes. We create a variable called speed_test that has the code. We then pass this variable to the timeit function and we set the number of executions to 3.
# Set

import timeit

# Testing the speed of execution in a set 
speed_test = '''
a = range(100000) 
b = list(a)
i = 999999

for i in b:
    print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))
# From the results, we can conclude that sets execute slightly faster than lists. What is your conclusion?