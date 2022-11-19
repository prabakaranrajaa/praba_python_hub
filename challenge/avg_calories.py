# Average Calories

# Create a function called average_calories that calculates the average calories 
# intake of a user. The function should ask the user to input their calories 
# intake for any number of days and once they hit ‘done’ it should calculate 
# and return the average intake.

def average_calories(): 
    scores = []
    while True:
        score = input('Enter a score or done when quit: ') 
        if score == 'done':
            break 
        scores.append(int(score))
    return f" Mean of scores is " \
        f"{sum(scores) / len(scores):.2f}"


print(average_calories())


# This simple average calorie calculator will run until the user enters ‘done’,
# then it will calculate the average calories. The input from the user is added to
# the scores variable. We use the sum() function and the len() function to calculate
# the average calories in the scores list. The while loop is what keeps the function 
# running until something happens that makes it break out of the loop. Once we hit
# ‘done’ the loop is halted by the break statement.

