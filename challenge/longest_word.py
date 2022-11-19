# Longest Word
# Write a function that has one parameter and takes a list of words as an argument.
# The function returns the longest word from the list. Name the function longest_word.
# The function should return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your function should return
# [10, JavaScript] as the longest word.

def longest_word(a):
    b =[]
    for word in a: 
        b.append([len(word), word])
    return max(b)

print(longest_word(['Java','Javascript','Python']))


# In this challenge, we use the append() method to append the strings and their 
# length to list b. If you print list b you will get a nested list of each word 
# and its length. The max() function finds the longest word in list b.

