# Return Indexes
# Write a function called index_position. This function takes a string as 
# a parameter and returns the positions or indexes of all lower letters in the string.
# For example, ‘LovE’ should return [1,2].

def index_position (a): 
    idex = []
    for i, item in enumerate(a): 
        if item.islower():
            idex.append(i) 
    return idex


print(index_position('LovE'))


# Using the enumerate() function we can retrieve the item index or position. 
# The isupper() method returns True if a letter in the string is capitalized. 
# Once we find the capitalized letter, we want its index to be appended 
# to the idex list.

