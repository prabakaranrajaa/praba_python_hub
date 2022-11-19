# User Name Generator
# Write a function called user_name, that creates a username for the user.
# The function should ask a user to input their name. The function 
# should then reverse the name and attach a randomly issued number 
# between 0 – 9 at the end of the name. The function should return the username.


import random
num = random.randint(0,10) 
def user_name():
    name = input('Enter name: ')
    name = name[::-1]
    username = name + str(num) 
    return username
print(user_name())

# In this exercise, you get to use the random module. 
# Every time you call the function, the random module issues 
# a random number between 0 and 10. This number is added to the end of 
# the name using the + sign. We use slicing [::-1] to reverse the name.
# Another way around it would have been to use the reverse() method to reverse the name.