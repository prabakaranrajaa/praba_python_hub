# Odd and Even
# Write a function called odd_even that has one parameter and takes
# a list of numbers as an argument. The function returns the difference between
# the largest even number in the list and the smallest odd number in the list.
# For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
            odd.append(i)
    return max(even) - min(odd)


print(odd_even([1, 2, 4, 6]))


# In this challenge, we use the modulus operator to find even and odd in the list.
# Then we use the max() and min() functions to return the max number and min number.
