# Zeros to the End
# Write a function called zeros_last. This function takes a list as argument.
# If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the original list sorted in ascending order.
# For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].


from ast import IsNot


def zeros_last(arr: list) -> list:
    i = 0  # setting index 0
    arr1 = arr
    for num in arr:
        # Checking for non-zero numbers
        if num != 0:
            # Moving non-zero numbers to the front of the list
            arr[i] = num
            i += 1

# Moving zero elements to the end of the list.
    while i < len(arr):
        arr[i] = 0
        i += 1
        return arr

    else:
        # if no zeros return original list in ascending order
        return sorted(arr1)


list1 = [1, 4, 6, 0, 7, 0]
list2 = [2, 1, 4, 7, 6]

print(zeros_last(list1))
print(zeros_last(list2))

# Zeros to the End
# The challenge is about understanding indexing. The first step is to identify non-zero numbers in the list.
# Once we identify them, we move them to the front of the list, while incrementing the index by 1.
# We then fill the remaining spots with the zeros in the list.
