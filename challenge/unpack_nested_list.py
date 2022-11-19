# Unpack A Nest
# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from 
# the nested list above – 34, 67, 78. Your output should be another list:
# [34, 67, 78]. The list output should not have duplicates.

nested_list = [[12, 34, 56, 67], [34, 68, 78]]

new_list = []
    # A nested for loop to access the inner list 
for arr in nested_list:
    for num in arr:
    # Create a list of numbers wanted 
        if num in [34, 67, 78]:
    # Checking if number already # exists before appending 
            if num not in new_list:
                new_list.append(num)
print(new_list)




# Unpack a Nest
# For this challenge we need to write a nested loop to access 
# the inner list of the nested list. We then create a new list of
# all the numbers that we need from the list.
