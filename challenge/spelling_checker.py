# Spelling Checker
# Write a function called spelling_checker. This code asks the user to input a word and if a user inputs a wrong spelling it should suggest the correct spelling by asking the user if they meant to type that word. If the user says no, it should ask the user to enter the word again. If the user says yes, it should return the correct word. If the word entered by the user is correctly spelled the function should return the correct word. Use the module textblob.



from textblob import TextBlob


def spelling_checker(): 
    while True:
        word = input('Enter a word : ')
        # checking if the input word is correct 
        if word != TextBlob(word).correct():
        # suggesting the correct word to the user
            question = input(f'Did you mean '
                    f'{TextBlob(word).correct()}?. ' 
                    f'type yes/no :')
            if question == 'yes': 
                break
            else:
                print('Please try again') # if the word entered is correct
        # the code breaks and returns word 
        elif word == TextBlob(word).correct():
            break
    return f'Your word is, {TextBlob(word).correct()}'


print(spelling_checker())



# The textblob module is being used to check the word from the user. If the word is not spelled correctly, the module suggests a correct spelling to the user. If the user accepts the word, the word is returned. If the user does not accept the word, the code asks the user to enter another word. We are using a while loop, so this code will only break once the user inputs a correct word or accepts the correctly spelled word suggested by the code.

