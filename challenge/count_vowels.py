# Count the Vowels
# Create a function called count_the_vowels. The function takes one argument, a string, and returns the number of vowels in the string. For example, ‘hello’ should return 2 vowels. If a vowel appears in a string more than once it should be counted as one. For example, ‘saas’ should return 1 vowel. Your code should count lowercase and uppercase vowels.

def count_vowels(a): 
    vowels = []
    for letter in a:
        if letter in 'AEIOUaeiou': 
            if letter not in vowels:
                vowels.append(letter)
    return len(vowels)


print(count_vowels('hello'))



# For this challenge, we create a string of vowels. The code checks if the letters in the string, are in the vowels string. If the letter is in the string, then it is appended to the vowels list. We then use the len() function to count the number of elements in the vowels list.