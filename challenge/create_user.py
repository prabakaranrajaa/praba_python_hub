# Create User
# Write a function called create_user. This function asks the user to enter their name,
# age, and password. The function saves this information in a dictionary. 
# For example, if the use enters name as Peter, age - 18 and password - love. 
# The function should save the information as: 
#     {'name': 'Peter', 'age': 18, 'password': 'love'}
# Once the information is saved. The function should print to the user that - "User saved. Please login"
# The function should then ask the user to re-enter their name and password.
# If the name and password match with what is saved in the dictionary, 
# the function should return "Logged in successfully". If the name and 
# password do not match with what is saved in the dictionary, 
# the function should print ('Wrong password or user name. Please try again'.
# The function should keep running until the user enters correct logging details.

def create_user():
    d = {} # create an empty dictionary 
    name = input("Enter your name: ") 
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    # Updating the dictionary using update method. 
    d.update({'name': name})
    d.update({'age': age}) 
    d.update({'password': password})
    print("User saved. Please login")
    # using while loop to ensure the code runs # until user enters correct login details 
    while True:
        user_name = input("Please enter your user name to login : ") 
        password = input("Please enter your password : ")
        if user_name == d.get('name') and password == d.get('password'):
            return "Logged in successfully" 
        else:
            print('Wrong password or user_name please try again')


print(create_user())


# Create User
# In this challenge, we create an empty dictionary and use the update method to
# update it with information from user. We then use a while loop to ensure 
# the code runs until correct user details are entered.
