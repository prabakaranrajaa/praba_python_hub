# Write a function called hide_password that takes no parameters.
# The function takes an input (a password) from a user and returns a hidden password.
# For example, if the user enters ‘hello’ as a password
# the function should return ‘****’ as a password and tell the user that the password is 4 characters long.

def your_password():
    password1 = input('Enter password')
    password = len(password1) * '*'
    return f'You password is {password} ' \
        f'and its {len(password)} characters long'


print(your_password())


# In this challenge, we get to use the input() function to get information from a user.
# We then use the len() function to get the length of the password.
# We use the multiplication operator to multiply each element of the string with ‘*’.
