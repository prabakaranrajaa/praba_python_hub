# Save Emails
# Create a function called save_emails. This function takes no arguments but asks the user to input email, and it saves the emails in a CSV file. The user can input as many emails as they want. Once they hit ‘done’ the function saves the emails and closes the file. Create another function called open_emails. This function opens and reads the content of the CSV file. Each email must be in its line. Here is an example of how the emails must be saved:
# jj@gmail.com kate@yahoo.com

# and not like this: jj@gmail.comkate@yahoo.com


def save_emails(): 
    w = []
    while True:
        email = input("Enter your email: ") 
        w.append(email)
        if email == 'done': 
            break
        with open('emails.csv', 'a') as f:
            f. write(email) 
            f .write('\n')

# Second function to read emails 
def open_emails():
    with open('emails.csv', 'r') as f: 
        return f.read()

save_emails() 
print(open_emails())




# There are two functions in this code. The first one appends or writes the email on the file. We open the file (emails.csv) in append mode ‘a’ so we do not overwrite content that is already on the file. If you open a file in append mode, if the file does not exist it will be created. We use the escape character (\n) to ensure that every email is appended in the new line. Since we are using the with statement, the file will be automatically closed.
# The second function opens and reads the file. since we are just
# reading the file, we open the file in read mode(‘r’).

