#########################################
#					#
#					#
#          Python Operators		#
#					#
#########################################


# operators are + , - , * , / , % , // .

#	Operator	Name	Example	
#	+	Addition	x + y	
#	-	Subtraction	x - y	
#	*	Multiplication	x * y	
#	/	Division	x / y	
#	%	Modulus	x % y	
#	**	Exponentiation	x ** y	
#	//	Floor division	x // y

# these are arithmetic operators 

# for .e.g. ,

print(10 + 5 ) 
# the answer will be 15 

print( 10 - 5 )
# the answer will be 5 

print( 10 * 5 )
# the answer will be 50 

print( 10 / 5 )
# the answer will be in float 2.0

print( 10 // 5 )    # this type answer will return quotient only 
# the ans wiil be 2 only

print( 10 % 3 ) 	# this type answer will be reminder  only
 # the ans will be 1 

print( 2 ** 3 ) # it's power  2 * 2 * 2 = 8
# the ans will be 8 

###################### 	Python Assignment Operators  	######################

# if we want to add increment means ,

x = 5
x = x + 3 
print(x)

# it will be print 8 
# instead of this , we can use like this

x = 5
x += 3
print(x)

# it will also return 8 


# for like all other operators 


# Operator	Example	Same As	
#	=	x = 5	x = 5	
#	+=	x += 3	x = x + 3	
#	-=	x -= 3	x = x - 3	
#	*=	x *= 3	x = x * 3	
#	/=	x /= 3	x = x / 3	
#	%=	x %= 3	x = x % 3	
#	//=	x //= 3	x = x // 3	
#	**=	x **= 3	x = x ** 3


# for all like this only .....


############### comparison operator ##################

# as per the boolean it's too like this 
#	operator 	name	example
#	==	Equal	x == y	
#	!=	Not equal	x != y	
#	>	Greater than	x > y	
#	<	Less than	x < y	
#	>=	Greater than or equal to	x >= y	
#	<=	Less than or equal to	x <= y


# for .e.g.,

x = 10 
y = 5 

print( x == y )
# it is False

# if it is this like !=

print( x != y )
# it will return True


x = 10
y = 9

print( x > y )
# it will return True

print ( x < y )
# it will return False

# like wise all operator comes ...

######################## Logical Operators	########################

#	Operator	Description						Example	
#	and 	Returns True if both statements are true			x < 5 and  x < 10	
#	or	Returns True if one of the statements is true			x < 5 or x < 4	
#	not	Reverse the result, returns False if the result is not True	not(x < 5 and x < 10)

x = 5 
print(x < 5 and x < 10 )
# it will return True

x = 5
print(not(x > 3 and x < 10))
# answer is True but the not operator will return False

# the identify operators are  are like [ is , not in ]

x = [ ' a ' , ' b ' , ' c ' , ' d ' ]
y = [ ' a ' , ' b ' , ' c ' , ' d ' ]

z = x

print( z is x )

# it will return True 

print( z is not y )
# the answer is False only but it will return True 

# already we saw in strings 
# like this ..,
x = [ 1 , 2 , 3 , 4 , 5 ]
print ( 1 in x )

# it will return True 

print ( 6 not in x )

# the answer is false becoz 6 is not there but this is not case so this will return False

#################	bitwise operators	 ################################


#	Operator	Name	Description
#	& 	AND	Sets each bit to 1 if both bits are 1
#	|	OR	Sets each bit to 1 if one of two bits is 1
#	 ^	XOR	Sets each bit to 1 if only one of two bits is 1
#	~ 	NOT	Inverts all the bits
#	<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#	>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#############################################################################################################


