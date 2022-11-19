# Count the Dots
# Write a function called count_dots. This function takes a string separated by dots as a parameter 
# and counts how many dots are in the string. For example, ‘h.e.l.p.’ should return 4 dots, 
# and ‘he.lp.’ should return 2 dots.

def count_dots(word):
    m = word.split(".")
    return f'The string has {len(m)-1} dots'

print(count_dots("h.e.l.p."))


# We use the split() function to split the word at the dots. 
# Once the word is split, we use the len() function to count the dots.