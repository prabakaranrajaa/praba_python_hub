###################################
#                                                                   #
#                                                                   #
#       VARIABLES in python                         #
#                                                                   #
#                                                                   #
###################################


# Variables are containers for storing data values.

# we can give any alphabets or letters variable 
# for e.g.,

name = " R O C K "

# here i give name as a variable and it contains the element R O C K as a string...
# string we have to give it like only " " in this double quotes.
# String variables can be declared either by using single or double quotes. it's ur wish

# for STRING variable

name = "ROCK"

#for INT variable

age = 19

# here i give age as a variable and it contains int 18 a number.


#for Float variable 

CGP = 8.5

#here i give float element on cgpa variable

# if i want to print it we have to put those variable by printing

print(name)
print(age)
print(CGP)

# output will be as 
###################
#   ROCK          #
#   18            #
#   8.5           #
###################

# python is case- sensitive language.. so 
# we have to put the variable correctly 
# for E.G.,

a = "Apple"
A = "APPLE"

# we printing the variable a only ...

print(a)

# it will print only ' a ' vairable and output will be as Apple.

# casting 
# if we want to give varaible data type specify... we can give like this ,

x = str(45)
# it is an string 45 not integer // it will be noted as only string 45..
y = int(234)
# same like that it is 234 integer
z = float(21.2134)
# like int it is float 21.2134 
s = str("hello world")
# string hello world




#  we have to give the variable name correctly
# rule of python variable
# 
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

# for e.g.,

# legal variable types

myname = "rock"
my_name = "sam"
_my_name = "tom"
MYNAME = "TOM"
myname21 = "TIM"

# like thiss


# Illegal variable names
#################
12name = "hello"
my-name ="rock"
my name ="sam"  
#################
# we can't give the varaible as space and hyphen and staring numbers ....
# it will give error


#### we can give many values to multiple varaible 

# for e.g.,

name,age,cgp = "rock",19,8.5

# like this and we can print like as

print(name,age,cgp)

# or

print(name)
print(age)
print(cgp)
 
##### we can give one value to multiple Variables

a = b = c = "alphabets"
d = e = f = 34
g = h = i = 56.7

# if we print a b c it will print alphabets only
# if we print d e f it will print 34 
# if we print g h i it will print 56.7
# or we can call single variable or multiple variable

# now i am calling a and e and i
print(a)
print(e)
print(i)
# it will print the order as ,
#   alphabet
#   34
#   56.7

# we can give variable as unpack a collection 
# for e.g., [] it is a list
# i am giving a variable for this [] and i input some values 

info_data = ["ROCK" , 19 , 8.5 , "lgrock007"]

# i am giving some data in this list if we call this as like

name,age,cgp,nickname = info_data

# if i call like this , it will assign a value inside the info_data for all giving values

# if i print ..,

print(name)
print(age)
print(cgp)
print(nickname)

# it will give output...

################## output variables ########################

# if we giving like this ..,

x = "I "
y = "love "
z = "python."

print(x,y,z)

# it will print as I love python.

# you can use this also + operator for concatenation this variable

print(x+y+z)

# it will also print the variable with no error

# we can add int or str or float 
# we can multiple them with str but not with int

# for e.g., 

a = "hello"
b = 5
print(a+b)

# it will give type error : unsupported operand type(s) for +: 'int' and 'str'

# we can only call those int and str as (,) comma only

# for e.g., 
print(a,b)
#it will print as hello5 

#########################################################################################################
