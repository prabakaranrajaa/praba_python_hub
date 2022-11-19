# Just Digits
# In this challenge, copy the text below and save it as a CSV file. Save it in the same folder as your Python file. Save it as python.csv.
# Write a function called just_digits that reads the text from the CSV file and returns only digit elements from the file. Your function should return 1991, 2, 200, 3, 2008 as a list of strings.


# “Python was released in 1991 for the first time. Python 2 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3 was released in 2008 and was a major revision of the language that is not completely backward-compatible.”



def just_digits():
    with open('oo.csv', 'r') as file: 
        a = file.read().split(',')
        # print(a)
        list1 = [] 
        for i in a:
            if i.isdigit(): 
                list1.append(i)
        return list1


print(just_digits())



# When opening files, it is good practice to open them with a with statement. This means that you don’t have to close the file at the end of the operation as the with statement will automatically close the file. In this code, we open the file in the read mode. We use the split() method to split the words in the text into strings. By default, the split method splits the text on the whitespaces. The isdigit() method checks which string elements are non- numeric. These non-numeric elements are appended to the list1 variable.