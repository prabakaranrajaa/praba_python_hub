# Only Words with Vowels
# Create a function called words_with_vowels, this function takes a string of words and returns a list of only words that have vowels in them. For example, ‘You have no rhythm’ should return [‘You’,’have’, ‘no’].
 

def vowels_count(a): 
    vowels = []
    for word in a.split(): 
        for i in word:
            if i in 'aeiou':
                if word not in vowels: vowels.append(word)
    return vowels
print(vowels_count('You have no rhythm'))




# Notice that we are using the nested for loop to find the letters in the words. We iterate through the words to check if any of the letters in the words are vowels. If a word has a vowel in it, we append it to the vowels list. In the vowels list, we only have words that have vowels in them.


