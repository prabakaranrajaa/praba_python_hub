# Longest Value
# Write a function called longest_value that takes a dictionary as an argument and returns
# the first longest value of the dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(d: dict):
    # Using max and key len to get the longest value
    longest = max(d.values(), key=len)
    return longest


fruits = {'fruit': 'apple', 'color': 'green', 'a': 'z'}
print(longest_value(fruits))


# Longest Value
# We use the max function to return the max value of the dictionary values. The max function has a key parameter.
# Since we are looking for the first longest value, we pass len to the key parameter.
# If we do not pass len to the key parameter, it will return green as the longest value
# which is lexicographically larger than apple.
