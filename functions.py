#####################################
#									#
#									#
#		Python Function 			#
#									#
#									#
#####################################

# function 

# we can call a function in anywhere...

# def for function

def hello():
	print('hello world')

hello()

# the o/p as hello world

# we can call this function again anywhere.......
hello()

# it's also will give o/p.

#########################################################


# no return type without argument

# without return we giving a value

def add()
	a = int(input('a : '))
	b = int(input('b : '))
	c = a + b
	print('Total : ',c)

add()

# now it will give o/p.


def sub(a,b):
	c = a - b
	print('difference : ',c)
	
sub(5,3)

# it will give o/p as 2

#############################################################


# return type without argument
# we returning a value in function when calling

def mul():
	a = int(input('a: '))
	b = int(input('b: '))
	c = a * b
	return c

x = mul()
print('mul',c)

##########################################################

# return type with argument

def div(a,b):
	c = a/b
	return c
	
x = div(5,2)
print('div : ',x)

#######################################################


# arbitrary argument function
# we can pass many value
# arbitrary = * symbol we have to give

def class_10(*students):
	print(students)
	
class_10('a','b','v','c','d','e')

# now it will print as tuple ...........
# the o/p will be as ('a','b','v','c','d','e')

#######################################################

# keyword argument function 

def message(name,age):
	print('name:',name,'age is ',a)

message('rock',19)
# it will print as rock age is 19

# but if u change the value as
message(19,'rock')
# it will print as 19 age is rock

# so we using keyword arugment as
message(age= 19 , name = 'rock')

# now it will print as rock age is 19

#############################################################


# arbitrary keyword argument function
# normal arbitrary function is single star *
# for arbitrary keyword function give double star **


def bio(**data):
	print(data)

bio(name = 'rock ' , age = 19 , code = 'python')

# the o/p will be as dictionary  format

# the o/p as {'name': 'rock ', 'age': 19, 'code': 'python'}

#############################################################


# default parameter function

def info(name,age,city='TN'):
	print('name :',name,'age is',age,'city :',city)
	
info('rock',19,'TVL')

# the o/p will be as name : rock age is 19 city :  TVL

# if we didn't give any argument for city , it will be print as default arugment as TN

info('rock',19)

# now the o/p will be as name : rock age is 19 city : TN


#########################################################

# passing list as an argument function

def total(marks):
	return sum(marks)
	
print('total:',total([55,65,90,90,95]))

# the o/p will be as total : 395
# we can passing a argument through list

########################################################

# recursive function

# a function wants to done their work , itself it call a function. it is recursive function

# for e.g.,

def factorial(x):
	if x == 0 :
	return 1
	elif x == 1 :
		return 1
	else:
		return(x*factorial(x-1))
		

fact = factorial(5)
print('Factorial :',fact)
# it will give o/p as 120

# how it's work

"""
factorial(5)
5*Factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""
#########################################################

# A lambda function is a small anonymous function.

''' 
syntax : lambda argumens : expression 
'''

# lambda functions 
# single argument lambda
c = lambda a : a + 50
print(c(5))

# it will take this as a : 5 + 50
# 55

####################################

c = lambda a , b : a*b
print(c(10,25))

# it will give o/p as 250


#####################################

x = lambda a , b , c : a + b * c
print(x(1,2,3))

# it will give o/p as 7 .

####################################

# we can use lambda in functions 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
# expression a calling a mydoubler
print(mydoubler(11))
# answer will be as 11 * 2 = 22.

#####################################

def lamb(n):
	return lambda a : a * n
	
my_d = lamb(2)
my_t = lamb(3)

print(my_d(11))
print(my_t(11))

# the o/p will be as 
# 22
# 33

########################################







