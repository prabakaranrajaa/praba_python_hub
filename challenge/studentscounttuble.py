# Tuple of Student Sex
# You work for a school and your boss wants to know how many female and male students are enrolled in the school.
# The school has saved the students in a list. Your task is to write a code that will count
# how many males and females are in the list. Here is a list below:

# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
# 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)]


students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']


def count_students(arr: list) -> list:
    # create an empty list to append lowercase strings
    new_list = []
    student_count = []
# converting names to lowercase # and appending to new_list
    for names in students:
        new_list.append(names.lower())
# Finding and counting all males in the # list and putting it in a tuple
    for sex in new_list:
        if sex == 'male':
            student_count.append((sex, new_list.count(sex)))
            break
# Finding and counting all females in the # list and putting it in a tuple
    for j in new_list:
        if j == 'female':
            student_count.append((j, new_list.count(j)))
            break
# returning a tuple of students
    return student_count


print(count_students(students))


# Tuple of Student Sex
# The first thing to do for this challenge is to ensure that we convert all
# the strings into lowercase letters, using the lower() method.
# So, we create a new list with names converted into lowercase.
# Then we search for males and females in the list. We use the count method to c
# ount how many times each appears in the new_list. We then combine the sex and
# the number of times it appears in the list into a tuple (sex, new_list.count(sex).
# We then append the tuples to the student count list. Notice that we use the break statement after append,
# to ensure that we only iterate through the list once.
