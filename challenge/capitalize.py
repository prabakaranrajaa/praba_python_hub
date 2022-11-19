# Capitalize First Letter
# Write a function called capitalize. This function takes a string as 
# an argument and capitalizes the first letter of each word. For example, 
# ‘i like learning’ becomes ‘I Like Learning’.


def capitalize(a: str): 
    upper = []
    for i, word in enumerate(a.split()): 
        if word[0].islower():
            upper.append(word.capitalize()) 
        else:
            upper.append(word) 
    return ' '.join(upper)

print(capitalize('i like learning'))


# The enumerate() function returns the element and its index while iterating 
# through the string. The capitalize() method will capitalize 
# the first letter of a string. In this code, we use the islower() method to 
# check which word in our string has lower letters. We then use the capitalize()
# method to capitalize these words and append them to a list. 
# We then use the join() method to join the elements in our 
# output list into a single string.