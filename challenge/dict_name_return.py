# Dictionary of names
# You are given a list of names, and you are asked to write a code that returns
# all the names that start with ‘S’. Your code should return a dictionary of
# all the names that start with S and how many times they appear in the dictionary. Here is a list below:

# names = ["Joseph","Nathan", "Sasha", "Kelly",
# "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}


from collections import Counter
names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]


d = {}  # Creating an empty dictionary
for name in names:
    if name.startswith('S'):
        # Using the dictionary update method
        d.update({name: names.count(name)})
print(d)

# Dictionary of names
# In this challenge we are asked to create a dictionary of names that start with ‘S’.
# So, first we need to find all the names in the list that start with ‘S’, then we need to return
# these results in a dictionary. The easy way to find the names is to use the startwith method.
# This method will return all names that start with the given element. In the code below, we create an empty dictionary;
# then we search for all the elements that start with ‘S’. Using the dictionary method – update,
# we update the empty dictionary with the results of our search.


count = []  # Creating an empty list
for name in names:
    if name.startswith("S"):
        # Appending names that start with S to the list
        count.append(name)
# Using the counter method to return a dictionary
        names = Counter(count)
print(names)

# Second Method
# Another method would be to use the Counter class from the collections module.
# The Counter class keeps track of elements and their count and stores the results in a dictionary.
# It returns the name of the element as a key and its count as value. See code below:
