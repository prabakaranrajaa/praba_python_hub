# Most Repeated Name
# Write a function called repeated_name that finds the most repeated name in 
# the following list

from collections import Counter
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"] 
def frequent_name(a):
    return max(Counter(a).most_common())


print(frequent_name(name))



# The collections module has a counter() class that 
# we can use to find the most common element of a list. 
# We use it here and it returns Peter which appears in the list 3 times.