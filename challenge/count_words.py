# Words and Elements
# Write two functions. The first function is called count_words which takes 
# a string of words and counts how many words are in the string.

# The second function called count_elements takes a string of words and 
# counts how many elements are in the string. Do not count the whitespaces. 
# The first function will return the number of words in a string and 
# the second one will return the number of elements (less whitespace). 
# If you pass ‘I love learning’, the count_words function should return 3 
# words and count_elements should return 13 elements.

def count_words(arr: str): 
    words = []
    for word in arr.split(): 
        words.append(word) 
        print(words)
    return f'There are {len(words)} ' \
        f'words in the sentence'


print(count_words('I love learning'))



# The split() function splits the string into smaller strings. 
# By default, the split() function uses any white spaces to split a string. 
# Once the string is split, we use the for loop to 
# iterate through the strings and append them to the words variable.
# The len() function counts how many items are on our list.

def count_characters(a):
    a = a.replace(' ', '') 
    return f'The string has ' \
        f'{len(a)} elements '

print(count_characters('I love learning'))



# Second function
# Since the len() function counts white spaces as elements, we use the replace() 
# method to remove white spaces in the string before using the len() function.
