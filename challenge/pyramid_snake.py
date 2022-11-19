# Pyramid of Snakes

# Write a function called Python_snakes that takes a number as an argument and creates the following shape, 
# using the number’s range: (hint: Use the loops and emoji library. If you pass 7 as argument, your code should print the following:
#         ⠦
#        ⠦ ⠦
#       ⠦ ⠦ ⠦
#     ⠦ ⠦ ⠦ ⠦
#    ⠦ ⠦ ⠦ ⠦ ⠦
#   ⠦ ⠦ ⠦ ⠦ ⠦ ⠦


from emoji import emojize

def python_snakes(n: int):
# the loop to determine the number of rows of the pyramid 
    for i in range(0, n):
# The loop that determines number of columns 
        for j in range(n, i, -1):
# print space between the snake signs 
            print(end=" ")
        for k in range(0, i):
# printing the snake emoji 
            print(emojize(':snake:'), end=" ")
            print(emojize(":grinning_face_with_big_eyes:"), end=" ")
            # print(emojize(":winking_face_with_tongue:"), end=" ")
            # print(emojize(":zipper-mouth_face:"), end=" ")
        print("\n")

python_snakes(7)

# Pyramid of Snakes
# With this challenge, we use loops to create a Pyramid of snakes. 
# We import the emoji library to get the snake emoji. See code below:

