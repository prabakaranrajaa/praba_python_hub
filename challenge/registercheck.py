# Register Check
# Write a function called register_check that checks how many students are in school.
# The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’.
# If the student is not in school, the dictionary says ‘no’. Your function should return the number of students in school.
# Use the dictionary below. Your function should return 3.

#register = {'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'}


register = {'Michael': 'yes', 'John': 'no',
            'Peter': 'yes', 'Mary': 'yes', 'praba': 'yes'}


def register_check(reg: dict):  # Create a count variable
    count = 0
    for value in reg.values():
        if value == 'yes':
            count += 1
    return 'Number of students in school is', count


print(register_check(register))


# Another way to go about it:

# register = {'Michael':'yes', 'John': 'no','Peter':'yes', 'Mary': 'yes'}

def register_check1(reg: dict):
    count = 0
    for key, value in reg.items():
        if value == 'yes':
            count += 1
    return 'Number of students in school is', count


print(register_check1(register))


# To count the yes in the dictionary, we need to access the dictionary values(a.values) using a for loop.
# The for loop iterates through the dictionary in search of yes values. Every value is added to the count variable.
