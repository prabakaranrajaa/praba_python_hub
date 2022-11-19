# What’s My Age?
# Write a function called your_age. This function asks a student to 
# enter their name and then it returns their age. For example, 
# if a user enters Peter as their name, your function should return, 
# ‘Hi, Peter, you are 27 years old. This function reads data from 
# the database (dictionary below). If the name is not in the dictionary, 
# your code should tell the user that their name is not in the dictionary, 
# and ask them for their age. Your code should then add the name and
# age to the dictionary of names_age below. Once added your code should 
# return to the user ‘Hi, (added name), you are (added age) years old’. 
# Remember to convert the input from user to lowercase letters

# names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}

names_age ={"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


def your_age():
# Convert name to lowercase letters
    name = input("Please enter your name: ").lower() # Use for loop to iterate over the dictionary 
    for key in names_age.keys():
        if key == name:
    # use the get method to access a specific value.
            return f'Hi, {name}! You are {names_age.get(key)} years old'
        else:
    # if name not in the dictionary 
            while name not in names_age.keys():
                age = input("Your name is not in the dictionary, " "please enter your age? ").lower()
    # Update the dictionary with name and age. 
                names_age.update({name: age})
            return f'Hi, {name}! You are {names_age.get(name)} years old'



print(your_age())


# What’s My Age?
# This challenge is about working with dictionaries. 
# Since all the keys in the dictionary are lowercase, convert the input from user to lowercase. 
# Then, we iterate over the dictionary to see if the input name exists in our database. 
# Once we find it, we use the get method to access the dictionary value (which is the age of the person).
# If the name is not in the dictionary, we use the while loop to update the dictionary with the new information from the user. 
# Once we update the dictionary, we return the updated information to the user. See code below:

