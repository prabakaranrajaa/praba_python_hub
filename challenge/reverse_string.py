# Reverse a String
# str1 = "the love is real"

# Write a function called read_backwards that takes a string as an argument 
# and reverses it. For example, the string above should return: "real is love the"

str1 = "the love is real"

def read_backwards(n: str) -> str: # Create an empty list
    x = []
    for i in n.split()[::-1]: # Using split to split string on whitespaces
        x.append(i)
# using the join method to join string
    return ' '.join(x)


print(read_backwards(str1))


# Reverse a String
# In this challenge, we use the split method to split the string on white spaces.
# We then append the strings to the empty list, and reverse the words using [::- 1]. 
# We then get the words in the list and join them using the join method.
