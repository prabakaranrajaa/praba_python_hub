#########################################
#										#
#										#
#				Python If - Else 		#
#										#
#										#
#########################################


# python if - else statements are logical conditions ...
#	Equals: a == b
#	Not Equals: a != b
#	Less than: a < b
#	Less than or equal to: a <= b
#	Greater than: a > b
#	Greater than or equal to: a >= b

a = 10
b = 5
if b < a : 
	print('yes!!... a is greater')
	
# it will print o/p  yes!!. a is greater 

# we can put the statement without else or with else..

a = 10
b = 5
if b < a : 
	print('yes!!... a is greater')
else:
	print('no! b is greater)

# note : intedent is very important or else it will occur error 
# intendent 4 space or press tab button 1 time 

### elif 

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a = 50
b = 50
if a > b :
	print('a is greater ')
elif a == b :
	print('a is equal to b ')
else:
	print('nothing')
	
# if the condition is true it will stop first if or it will go elif 
# if elif is also false it will go ... else (finally)

# let's see a else conditon statement

a = 50
b = 1 
if a < b :
	print('b is greater ')
elif a == b :
	print(' a and b are equal')
else:
	print(' a is greater ')

# we can put the if-else statement with variable string data type 

# for e.g.,

a = 'rock'
b = 'helo'
if a == b :
	print('yes')
else : 
	print('no')
	
# the o/p is no 


# we can check anything with the if statement or we can print anything ....
l = [ 1 , 2 , 3 , 4 ,5 ]
if 5 in l :
	print('yes')
else:
	print('no')
	
# it will print yes.

# short -hand if statement 

# it will be executed in one line

a = 100
b = 50
if a > b: print("a is greater than b")

# for else

a = 10
b = 5
print('yes') if a > b  else print('no')

# the o/p will be yes ..

# for elif 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# we can give like this also 

# we can give compare not only two value we can compare many value
# for e.g., 

a = 50
b = 100
c = 200
if a < b and c > b :
	print('yes, it is true')
else:
	print('nope')
	
# we can use and , or operators here


########### NESTED - IF ###########################
# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  if x > 30 :
    print('and also above 30')
  if x > 40 :
  	print('and also above 40')
  else:
    print("but not above 20.")

# it will be print if the above statement is true , it will be print also that statement . 


# the o/p will be printed as 
#	Above ten,
#	and also above 20
#	and also above 30
#	and also above 40

#################################################3


# pass statement 

a = 10 
b = 20
if b > a :
	pass

# the o/p will be nothing can print and it won't give any error.

###############################################################################























































