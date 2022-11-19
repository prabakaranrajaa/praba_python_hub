# Student Marks
# Write a function called student_marks that records marks achieved by students in a test. The function should ask the user to input the name of the student and then ask the user to input the marks achieved by the student. The information should be stored in a dictionary. The name is the key and the marks is the value. When the user enters done, the function should return a dictionary of names and values entered.


def get_marks(): 
    d = {}
    while True:
        name = input('Enter the student name or done: ') 
        if name == 'done':
            break
        marks = int(input('Enter the marks: ')) 
        d[name] = d.get(marks, 0) + marks
    return d 
print(get_marks())






# In this code, we ask the user to input the name of the student and their marks in the test. The code only breaks once the user enters ‘done’. When that happens, the dictionary is returned. We use the get method(d.get) to add values to the dictionary. The get method(), searches for the key, and then it adds value to that key.