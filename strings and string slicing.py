##################################
#				 #
#				 #
#  	PYTHON STRINGS 		 #
#	 			 #
#				 #
##################################

# strings are letters numbers etc..,
# strings are in single quotes and double quotes and triple quotes

# for e.g., Double Quotes string

name = "ROCK"
print(name)
# name is variable and ROCK is a string

r_letters = " hello world 124 bye world "
print(r_letters)
# like these
# u can give either single or double quotes for string
#for e.g.,

x = "apple"
y = 'apple'
print(x)
print(y)
# for triple quotes for multiple lines strings 
#for e.g.,

sentence = """ hello guys i am rock , a python learner 
love to learn and code some interesting new stuffs
blah blah blah .... """
print(sentence)
# here triple quotes i used for little big sentences for some message u show to somewhere


#########################
#			#
#    STRINGS in array	#
#			#
#########################

# if i put some value in a varaible as string

code = "i luv python , it's amazing "
print(code)
# that means it will print all 
# but we need a particular array or character in that line so we can do like this .,

print(code[4])
# that means it will print  ' v ' only .
# becoz array are 
#	a 	b 	c	 d 	 e 		f
#	0 	1	2	 3       4 		5
# that like it will take all letters
#for e.g.,

a = "apple"
print(a[3])
# it will print as ' l '.

# we can use loop through strings 

# for e.g., 
# i am using for loop

for x in "rock" :
	print(x)
#it will print as 
#r
#o
#c
#k
# like this it will print answers...

#################
#		#
# string length #
#		#
#################

# if we want a length of a string line , we can't count if the string has many lines 
# so we use this function len() .
# for e.g.,

a = 'i luv python'
print(len(a))

# it will print as 12 , how many letters or there ... 
# here it is not like array string 
# note this point ..,
# array are calculated from ==== > 0 , 1 , 2 , 3 , 4 .....
# len are calculated from ===> 1 , 2 ,3 ,4 ....


#################
#		#
# check string	#
#		#
#################

# we can check string if it is there are not 

code = " i am interested in python"
if "am" in code :
	print("yes it was there")
else
	print("not there")
	
#if the 'am' in code it will check if it was there it will print yes or else it will print not.
# we will learn more about in if-else ..

#################################
#				#
#				#
#       String slicing 		#
#				#
#################################

# string slicing means if we  len the string in previous, but this time 
# we want a particular string letters .. for e.g.,

a = "i love python and it was amazing"
# i want the len 'python' to 'and'
print(a[7:18])
# it will print as python and

# for e.g.,

x = "hello world"
print(x[:5])
# it will print start to the given index 
# it will print  hello only...

# we can use it like this too...

x = "hello world"
print(x[6:])
# it will print after the 6 index that means it will print as world
# note that space will also be calculated as index ..

# we can use negative slicing 

x = "hello world!"
print(x[-5:-2])
# it will print as orl only ...
# becoz it will check from reverse order -1 , -2 -1 and -2 values will be removed
#   -3 -4 -5 are taken after -5 it will remvoe all -6 -7 that index will not taken 


### index error #####

# if the index is out of range 
# for e.g.,

x = "hello world"
print(x[15])
# it will not print 
# it will shows IndexError: string index out of range
##############################################################################################################
