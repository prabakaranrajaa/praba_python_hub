# Sort by Last Name

# You work for a local school in your area. The school has a list of names of 
# students saved in a list. The school has asked you to write a program that 
# takes a list of names and sorts them alphabetically. The names should be sorted 
# by last names. Here is a list of names:
# [‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris Brown’,’ Tom Cruise’]
# Your code should not just sort them alphabetically, but it should also switch 
# the names (the last name must be the first). Here is how your code output should look:
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']
# Write a function called sorted_names.

names = ['Beyonce knowles', 'Alicia Keys',
'Katie Perry', 'Chris Brown', 'Tom Cruise']


def sorted_names(list1): 
    list2 = []

    for i in list1: 
        list2.append(i.split())

    list3 = []
    # creating a key for the sorted function 
    x = lambda x: x[-1]
    for j in sorted(list2, key=x):
    # appending sorted names to list3 
        list3.append(' '.join([j[-1], j[0]]))

    return list3


print(sorted_names(names))
