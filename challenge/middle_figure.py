# Middle Figure
# Write a function called middle_figure that takes two parameters a, and b. 
# The two parameters are strings. The function joins the two strings and finds the 
# middle element. If the combined string has a middle element, the function should
# return the element, otherwise, return ‘no middle figure’. Use ‘make love’ as 
# an argument for a and ‘not wars’ as an argument for b. Your function 
# should return ‘e’ as the middle element. Whitespaces should be removed.

def middle_figure(a: str,b: str): 
    c = (a + b).replace(' ','') 
    print(c)
    b = len(c) 
    middle = b//2
    if len(c)% 2 == 1: 
        return c[middle]
    else:
        return 'No middle figure'


print(middle_figure('make love', 'not wars'))



# The first step in this challenge is to concatenate the two strings and 
# find the length of the new string using the len() function. 
# Remember to remove To find the middle element we use the floor division(//). 
# The floor division will round off to the nearest integer, which is 4.
# The element sitting on position or index 4 is the middle element. 
# Only strings with odd number lengths will return a middle element.