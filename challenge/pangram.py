# Pangram
# Write a function called check_pangram that takes a string and checks if it is a pangram. A pangram is a sentence that contains all the letters of the alphabet. If it is a pangram, the function should return True, otherwise, return False. The following sentence is a pangram so it should return True:

# 'the quick brown fox jumps over a lazy dog'


import string

def check_pangram(sentence): 
    list1 = []
    alphabet = string.ascii_lowercase
    # removing white spaces in the string 
    sentence = sentence.replace(' ', '') 
    for i in sentence:
        if i not in list1: 
            list1.append(i)
            list1.sort()
    sentence = ''.join(list1) 
    if alphabet == sentence:
        return True 
    else:
        return False


print(check_pangram('the quick brown fox '
'jumps over a lazy dog'))





# We use the string module to get the alphabet letters in lowercase. We then remove the whitespaces from our string using the replace() method. We use the for loop to loop through the string, remove duplicates and append the elements of the string to list1. We sort the elements of list1 in alphabetical order using the sort() method, and use the join() method to join the string elements. We then compare the sorted sentence to the alphabet. If the sentence variable has all the elements in the alphabet variable, the code will return True.