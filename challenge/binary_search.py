# Write a function called search_binary that searches for the number 22 in the following list and returns its index. The function should take two parameters, the list and the item that is being searched for. Use binary search (iterative Method).
# list1 = [12, 34, 56, 78, 98, 22, 45, 13]


def search_binary(list1, x): 
    low = 0
    high = len(list1) - 1
    mid_index = 0

    while low <= high:
        mid_index = (high + low) // 2

        if list1[mid_index] == x: 
            return mid_index
    # if an element is lower than the middle index # then search the lower part of the list
        elif list1[mid_index] > x: 
            high = mid_index - 1
    # if an element is higher than the middle index # then search the upper part of the list
        elif list1[mid_index] < x:
            low = mid_index + 1

# if an element is not found, return -1 
    return 'no element'

list1 = [12, 34, 56, 78, 98, 22, 45, 13]
list1 = sorted(list1) 
number = 22

results = search_binary(list1, number) 
if results == 'no element':
    print('Element is not in the list') 
else:
    print(f'The element index is {results}')









# The first step to solving a binary problem is to ensure that the list is sorted. A binary search does not work on a list that is not sorted. For this challenge, the first thing you had to do was sort the array or list. At its basic form, the binary search looks for the middle element in a list. If the list middle element is not what you are searching for, it will check whether the element you are searching for is greater than or less than the middle element. If it is greater, then it will search the middle element of the upper half of the list, if it is less, then it will search for the middle element of the lower part of the list. This process is repeated until the element is found. So, it picks a portion of the list and searches for the middle element. We use the iterative method for this challenge.