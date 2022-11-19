# Reversed List


# You are given a string of words. Some of the words in the string contain 
# uppercase letters. Write a code that will return all the words that have 
# an uppercase letter. Your code should return a list of the words. 
# Each word in the list should be reversed. Here is how your output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

import string

str1 = 'leArning is hard, bUt if You appLy youRself ' \
    'you can achieVe success'

upper_names = []
for word in str1.split(): 
    for letter in word:
# Using string module to find uppercase letters 
        if letter in string.ascii_uppercase:
            upper_names.append("".join(word[::-1])) 
print(upper_names)



# Reversed List
# For this challenge we import the string module to get a list of uppercase 
# letters (string.ascii_uppercase). We check if any of the words in 
# the string have uppercase letters, if they do we append the words to 
# the upper_names list. We then use reverse ([::-1]) to reverse the words in the list.

