# Find Missing Numbers
# list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
# 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

# Write a function called missing_numbers that takes a list of sequence of numbers and finds the missing numbers in the sequence. The list above should return:

# [4, 8, 10, 13, 16, 29, 30]

list3 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]


def missing_numbers(arr: list) -> list: 
    missing_numz = []
# find the missing numbers using range 
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr: 
            missing_numz.append(i)

    return missing_numz


print(missing_numbers(list3))




# Find Missing Numbers There are many ways you can solve this challenge. Here we using the range function to find the missing numbers in the sequence.