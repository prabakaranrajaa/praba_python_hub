# List of Tuples
# Write a function called make_tuples that takes two lists, equal lists, 
# and combines them into a list of tuples. For example, if list a is [1,2,3,4] 
# and list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].


def make_tuples(a,b): 
    a = zip(a,b)
    return list(tuple(a))

print(make_tuples([1,2,3,4],[5,6,7,8]))

# The easiest way to deal with this problem is to use the Python built-in 
# zip() function. The function combines the two lists into pairs of tuples.
# We use the list() and the tuple() function to ensure that the tuples will be in a list.