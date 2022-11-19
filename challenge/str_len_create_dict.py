# Length of Words
# s = 'Hi my name is Richard'

# Write a function called string_length that takes a string of words 
# (words and spaces) as argument. This function should return the length of 
# all the words in the string. Return the results in a form of a dictionary.
# The string above should return:

# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}


s = 'Hi my name is Richard'


def string_length(s: str) -> dict: 
    list1 = []
    dict1 = {}
# converting string into a list of strings 
    for word in s.split():
        list1.append(word)
# update the dictionary with word lengths 
    for word in list1:
        dict1.update({word: len(word)}) 
    return dict1


print(string_length(s))


# Length of Words
# This challenge requires that we create a dictionary of length of words.
# The word will be the key and the length of the word is the value. 
# Below, we use the split function to split the string into a list of strings. 
# We then iterate through the list and update our empty dictionary with 
# the words (key) and length of the words (value).

