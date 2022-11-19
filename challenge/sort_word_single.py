# Write a function called sort_words that takes a string of words as 
# an argument, removes the whitespaces, and returns a list of letters 
# sorted in alphabetical order. Letters will be separated by commas. 
# All letters should appear once in the list. This means that you sort and 
# remove duplicates. For example ‘love life’ should return as ['e,f,i,l,o,v'].

def sort_words(sentence): 
    list1 = []
    sentence = sentence.replace(' ', '') 
    for i in sentence:
        if i not in list1: 
            list1.append(i)
    list1.sort()
    sorted_words = [','.join(list1)] 
    return sorted_words


print(sort_words('love life'))


# In this challenge, we use the replace() method to remove the white spaces 
# between the words. Once the spaces are removed, we use the for loop to 
# iterate through the string and append the items to the list1 variable. 
# We use the not-in operator on list1 to ensure that we do not add duplicates 
# to the list. We use the join() method to add commas, between the string elements.