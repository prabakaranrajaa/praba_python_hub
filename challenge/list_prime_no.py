# List of Prime Numbers
# Write a function called prime_numbers.
# This function asks a user to enter a number (integer) as an argument and returns
# a list of all the prime numbers within its range. For example, if user enters 10,
# your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers() -> list:
    prime_num = []
    # Creating a range of the input number
    n = int(input('Please enter a number (integer): '))
# remember to add a 1 and the end ensure # all numbers in the range are covered
    for i in range(0, n + 1):
        # only numbers above 1 are needed
        if i > 1:
            for j in range(2, i):
                # if a number in the range is divisible by j # Then number is not prime
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
    return prime_num


print(prime_numbers())


# List of Prime Numbers
# A prime number is a number that has two factors, 1 and itself.
# Prime numbers start from 2. For this challenge we use the range function
# to find range of the number.
