# Count String
# Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.


def count(a): 
    d = {}
    for i in range(len(a)): 
        x = a[i]
        count = 0
        for j in range(i, len(a)): 
            if a[j] == a[i]:
                count = count + 1 
        countz = dict({x: count}) 
        # updating the dictionary 
        if x not in d.keys():
            d.update(countz) 
    return d

print(count('hello'))


# This code creates a dictionary from a string. The code uses a nested for loop. The first for loop returns the index elements of the string. The second for loop also returns the index. If the element index of loop one is equal to that of loop 2, 1 is added to the count variable. The if statement is used to update the dictionary d.