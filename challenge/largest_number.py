# Largest Number

# Write a function called largest_number that takes a list of integers and 
# re-arrange the individual digits to create the largest number possible. 
# For example, if you pass the following as an argument: list1 = [3, 67, 87, 9, 2]. 
# Your code should return the number in this exact format: 9,877,632 as 
# the largest number.

def largest_number(arr: list): # Create empty list
    list1 = []
    # remove brackets and spaces in the lists
    n = str(arr).strip('[,]').replace(',', '').replace(' ', '') # append the numbers to the empty list
    for i in n:
        list1.append(int(i))
    # Sorting the list in descending order 
    list1.sort(reverse=True)
    # removing parenthesis and spaces from the sorted # list and converting it to int
    large_number = int(str(list1).strip('[]').replace(',', '').replace(' ', ''))
    # return a large formatted number
    return 'The largest number is, {:,}'.format(large_number)


n = [3, 67, 87, 9, 2]

print(largest_number(n))


# Largest Number
# This challenge requires that we use some string methods such as strip and 
# replace to convert the number into integer. Here is the full code below:
