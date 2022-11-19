# Create a function called all_the_same that takes one argument, a string, 
# a list, or a tuple and checks if all the elements are the same. 
# If the elements are the same, the function should return True. 
# If not, it should return False. 
# For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True.

def all_the_same(a):
    a = all(i == a[0] for i in a) 
    return a

print(all_the_same(['Mary', 'Mary', 'Mary']))

# We are using the in-built all() function. The all() function
# will return True if all the elements of iterable are true.