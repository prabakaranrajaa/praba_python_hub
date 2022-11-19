# Find my Position
# Write a function called find_index that takes two arguments; a list of integers, and an integer. The function should return the indexes of the integer in the list. If the integer is not in the list, the function should convert all the numbers in the list into the given integer.

# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7, your code should return [4, 5] as the indexes of 7 in the list. If the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_index(arr: list, n: int) -> list: 
    list1 = []
    # Using enumerate to find index of integer 
    for i, j in enumerate(arr):
        if j == n:
            list1.append(i)
            # If integer not in list 
        if n not in arr:
            for j in arr:
                list1.append(n) 
            return list1

    return list1


lst1 = [1, 2, 4, 6, 7, 7]


print(find_index(lst1, 7))
print(find_index(lst1, 8))



# Find my Position
# In this challenge, it would be easy to use the enumerate function. Since we are looking for the index of a number, the enumerate function, will return the index of all the numbers in the list. We use the (if j == n) conditional statement to return only indexes of the given number. If the number is not in the list, we convert all the numbers in the list to the given number.
