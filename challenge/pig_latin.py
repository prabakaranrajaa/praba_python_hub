# Pig Latin
# Write a function called translate that takes the following words and translates them into pig Latin.
# a = 'i love python'	

# Here are the rules:
# 1.	If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2.	If a word starts with anything other than a vowel, move the first letter to the end and add ‘ay’ to the end. For example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def pig_latin(a): 
    output = []
    for i, word in enumerate(a.split()): 
        if word[0] in 'aeiou':
            output.append(word[i] + 'yay') 
        else:
            output.append(word[1:] + word[0] + 'ay') 
    return ' '.join(output)


print(pig_latin('i love python'))



# Using the enumerate() function we obtain the index of each letter in the string. The split() method turns the words in the string into strings. We use the if statement to check the first letter of the word is a vowel. If it is a vowel, we append ‘yay’ at the end. If it is not, we move the first letter to the end and append ‘ay’.