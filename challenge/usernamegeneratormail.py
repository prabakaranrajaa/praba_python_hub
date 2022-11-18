# User Name Generator
# Write a function called user_name that generates a username from the user’s email.
# The code should ask the user to input an email and the code should return
# everything before the @ sign as their user name. For example,
# if someone enters ben@gmail.com, the code should return ben as their user name.


def user_name():
    your_email = input("Enter your email")
    user_name = your_email.split('@')[0]
    return f'You user name is {user_name}'


print(user_name())


# The split() function splits the email at the @ element. Once, the email is split,
# we can use indexing to access the elements of the email.
# The part that we want to use for the user name is sitting at index 0,
# that is why we use [0] in our code to access it.
