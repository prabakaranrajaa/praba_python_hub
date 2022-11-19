# Password Validator
# Write a function called password_validator. The function asks the user to enter a password. A valid password should have at least one upper letter, one lower letter, and one number. It should not be less than 8 characters long. When the user enters a password, the function should check if the password is valid. If the password is valid, the function should return the valid password. If the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password. The code should only stop once the user enters a valid password. (use while loop).

# Extra Challenge: Valid Email
# emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]

# Write a function called email_validator that takes a list of emails and checks if the emails are valid. The function returns a list of only valid emails. A valid email address will have the following - @ symbol (if the @ sign is at the beginning of the name, the email is invalid. If there are more than one @signs, the email is invalid. All valid emails must have a dot com at the end (.com), if not, the email is invalid. For example, the list of emails above should output the following as valid emails:
# ['ben@mail.com', 'kenny@gmail.com']
# If no emails in the list are valid, the function should return ‘all emails are invalid’def password_checker(): errors = []
def password_checker():
    errors = []
    while True:
        password = input('Enter your password: ') 
        if not any(i.isupper() for i in password):
            errors.append("Please add at least one "
                          "capital letter to your password") 
        elif not any(i.islower() for i in password):
            errors.append("Please add at least one "
                          "small letter to your password") 
        elif not any(i.isdigit() for i in password):
            errors.append('Please add at least one '
                        'number to your password') 
        elif len(password) < 8:
            errors.append("Your password is less "
                    "than 8 characters") 
        if len(errors) > 0:
            print('Check the following errors:') 
            print(str(errors))
            del errors[0:] 
        else:
            return f'Your password is {password}'


print(password_checker())




# In this code, we use the while loop to ensure that the code runs until a valid password is entered. All errors in the input password are appended to the errors list. The any() function checks if any of the characters in the password satisfy a given condition. If a condition is not satisfied an error is raised.