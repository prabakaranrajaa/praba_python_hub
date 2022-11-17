#################################
#				#
#	PYTHON			#
#       MODIFY STRINGS		#
#				#
#################################

# we can modify strings as 
# for e.g.,

x = "hello bro"
print(x.upper())
# it will print as HELLO BRO.
# all are will be upper case ... ABCDEFGH ......... 

x = "Hello BRO"
print(x.lower())
# it will print as hello bro
# whatever value it has it will print as lower case abcdefghi.........

# we can also replace the values 
# for e.g.,

name = "TOM LESTER"
print(name.replace("O" , "I"))
# it will replace it as TOM LESTER to TIM LESTER

# we can remove the white spaces
a = " hello world! "
# we have some spaces is starting and ending we can change them
print(a.strip())
# like this ... it returns the 'hello world!' only...


# we can split between any words 

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# that means we want to split when the comma , comes it will split as a array.

# for e.g.,

code = "i love python"
print(code.split())
# the output will be  [ 'i' , 'love' , python' ] # becoz it split when the space comes.


#########################################
#					#
# string concatenation			#
#					#
#########################################

# we can merge a string  combine , concatenate ... with + operator 

# for e.g.,

Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# the output will be helloworld 
# where is the space between them ?? ..... becoz it doesn't contains any spaces so it will print like this only
# if we want space

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# we can put like this or ,

a = "Hello "
b = "World"
c = a + b
print(c)
# we can put the space at the end of the hello or the starting of the world ...

################################3


# we can add a variable values in string
# for e.g.,

name = "rock"
msg = " hello " + name 
print(msg)

# we can give like this or 

name = "rock"
# we can print directly ...
print("hello ",name)

# or we can use f string 

name ="rock"
print(f'hello {name}.')
# we can use f string to combine or concatenate the strings ...

########################################

# we can use the format method for to pass thr argument

#  format() method to insert numbers into strings:

age = 19
msg = "My name is rock, and I am {}"
print(msg.format(age))

# it is the format string to combine 

# if we have multiple line  .. we can add but we need some order to put
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# like this we can print 


############# index format string ############

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# the index order it will take 
# first - price   		=== 0 index
# second - quantity 		=== 1 index
# third - itemno 		=== 2 index

##################################################

# escape charcaters for python
#Escape Characters
#Other escape characters used in Python:

#Code	Result	
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

# for e.g.,

x = 'hello\nworld'
print(x)
# the output be
# hello
# world
# the line will goes down.. like wise all escape charcaters has unique features u can try it...





