# Sort by Length
# names = [ "Peter", "Jon", "Andrew"]
# Write a function called sort_length that takes a list of strings as 
# an argument, and sorts the strings in ascending order according to their length.
# For example, the list above should return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions


def sort_length(arr: list):
    for item in range(len(arr)):
        for j in range(len(arr) - 1):
    # Check if any of the words is longer than the other
            if len(arr[j]) > len(arr[j + 1]):
    # swap the longest for the shortest 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

names = ["Peter", "Jon", "Andrew"] 
print(sort_length(names))



# Sort by Length
# For this challenge, we find the longest word and then we swap them with 
# the shorter words. The shorter words come first, and the longer 
# words comes later.
