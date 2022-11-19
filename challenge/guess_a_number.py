# Guess a Number
# Write a function called guess_a_number. The function should ask a user to guess a randomly generated number. If the user guesses a higher number, the code should tell them that the guess is too high, if the user guesses low, the code should tell them that their guess is too low. The user should get a maximum of three guesses. When the user guesses right, the code should declare them a winner. After three wrong guesses, the code should declare them a loser.


import random
random_number = random.randint(0,10) 
def guess_number():
    c = 0
    while c < 4:
        guess = int(input("Guess a number "
    "between 1 and 10: "))
        c += 1
        if c == 3:
            print("You have run out of guesses. " "You lose")
            break
        elif guess > random_number: 
            print('Your guess is too high. '
        'Try again') 
        elif guess < random_number:
            print('Your guess is too low. ' 'Try again')
        else:
            return 'Correct. You win' 
    return ''


print(guess_number())



# We use the random module to issue a random number between 0 and 10. We use the while loop to ensure the code keeps running until the condition becomes False. The condition becomes False when the user guesses the right number or when they run out of guesses. The user gets a maximum of three (3) guesses.