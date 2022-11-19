# Even Number or Average

# Write a function called even_or_average that ask a user to input five numbers.
# Once the user is done, the code should return the largest even number in 
# the inputted numbers. If there is no even number in the list, the code should 
# return the average of all the five numbers.


def even_or_average(): 
    avg_num = [] 
    even_number = []
    # Using while loop to ensure code keeps running 
    while True:
        number = input("Please enter numbers or done: ") 
        avg_num.append(int(number))
        if int(number) % 2 == 0: 
            even_number.append(number)
    # Once the user inputs five numbers the code breaks 
        if len(avg_num) == 5:
            break
    if len(even_number) > 0: # checking if list empty
        return f'The largest even number: {max(even_number)}'

    else:
        return f'The average is : {sum(avg_num) / len(avg_num):.2f}'


print(even_or_average())
