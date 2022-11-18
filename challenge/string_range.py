# A String Range
# Write a function called string_range that takes a single number and
# returns a string of its range. The string characters should be separated by dots(.)
# For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.


def string_range(num: int):
    x = [str(i) for i in range(num)]  # Using join method to add dots
    x = " . ".join(x)
    return x


print(string_range(6))


# In this code, using list comprehension we create a list from the range.
# However, to use the join() method on the list,
# we must ensure that our list elements are in string format.
# We use the str() function to convert x into a string before calling the join() function to join the string with dots.
