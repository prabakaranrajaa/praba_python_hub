# Any Number of Arguments
# Write a function called any_number that can receive any number of arguments
# (integers and floats) and return the average of those integers.
# If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as 
# average. If you pass 12, 90 your function should return 51.0 as average.


def any_num (*args):
    ave = sum(args)/len(args) 
    return f'The average is {ave}'

print(any_num(12, 90))

print(any_num(12, 90, 12, 34))


# In this challenge, you get to know about *args. 
# You can use any word you want as a parameter as long as you use the * sign at 
# the beginning of the word. However, it's a common convention to use args.
# The *args simply tells the function that we are not sure 
# how many arguments we will need, so the function lets us add as 
# many arguments as possible. In the example below, we add two numbers as 
# arguments. However, we can add as many numbers as we want and 
# the function will work just fine. 
# The *args make functions more flexible.