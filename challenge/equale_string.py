# Write a function called equal_strings. 
# The function takes two strings as arguments and compares them. 
# If the strings are equal (if they have the same characters and have equal length), 
# it should return True, if they are not, it should return False.
# For example, ‘love’ and ‘evol’ should return True.
def equal_strings(st1, st2): 
    str1 = sorted(st1)
    str2 = sorted(st2) 
    if str1 == str2:
        print(str1)
        print(str2)
        return True 
    else:
        return False


print(equal_strings('love', 'veol'))


# To compare the two strings, first, we need to sort them. 
# We use the sorted() function to sort the two strings. 
# Then we use the (==) operator to compare the two strings.


