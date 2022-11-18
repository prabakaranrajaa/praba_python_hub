# Index of the Longest Word

# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the list.
# If there is no longest word (if all the strings are of the same length), the function should return zero (0).
# For example, the list below should return 2.

# words1 = ["Hate", "remorse", "vengeance"] And this list below, shoul return zero (0) words2 = ["Love", "Hate"]


def word_index(arr: list):
    for word in arr:
        for j in range(len(arr) - 1):  # Checking if the lengths of all the words are equal
            if len(arr[j]) == len(arr[j + 1]):
                return 0
                # Using len function and max to find the longest word
            elif len(word) == len(max(arr)):         # using list method index to find
                # index of the longest word
                return f'The longest word is at index: {arr.index(word)}'


words1 = ["aate", "aremorsegghhhh", "avengeance"]
words2 = ["a", "a"]
print(word_index(words1))
print(word_index(words2))


# The first thing we do, is check if all the strings in the list are of the same length. If so, we return 0.
# If they are not, we search for the longest word using the len() function and max() function.
# Once we find it, we search for its index using the index method.
