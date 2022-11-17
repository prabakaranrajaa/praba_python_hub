#############################################################
#									                    	#
#									                     	#
#  					python Tuples () 		   	            #
#				                               			    #
#									                    	#
#############################################################

# tuples are represented by ().

tuple = ( 1 , 2 , 3 , 4 )
print(tuple)
print(type(tuple))


tuple = ( 'apple' , 'cherry' , 'banana' , 'kiwi' , 'melon' )
print(tuple)
print(type(tuple))

# these are examples of tuples .....

# tuples are ordered , unchangeable , allow duplicates ...

tuple = (  'apple' , 'cherry' , 'banana' , 'kiwi' , 'melon' )
print(len(tuple))

# the o/p will be as 5 ...

# a single item or value contains is not a tuple 
# for e.g.,

b = (5)
print(type(b))

a = ('apple')
print(type(a))

# these two are not tuples 
# these are int and str

# if we want this as tuple , use comma after the value 

b = (5,)
print(type(b))

a = ('apple',)
print(type(a))

# now it will be print as class tuple ...

# like list tuples have int , str , bool values ...


tuple = ( 5 , False , 'hello' , True , 32.42 , 5j )
print(tuple)

# it  will be the o/p as (5, False, 'hello', True, 32.42, 5j)

# u can write inside the tuple  .. list
# for e.g.,

tuple = ( 5 , False , 32.234 , 'bye' , [ 0 , 1 , 2 , 3 ] , True )
print(tuple)

print(tuple[4])

print(type(tuple[4]))
# this type is list 


# like wise list we can indexing , array , range we can do


# we cannot change the tuple value .. but , we can change the tuple to list and list to tuple ..


x = ( 1 , 2 , 3 , 4 , 5 )
print('tuple:',x)
y = list(x)
print('list:',y) # This will print as List
# now we can change whatever we want 
y[2] = 6
print('changed list:',y)  # we changed it , the o/p will printed..
# after we can change again to tuple
y = tuple(y)
print('again tuple:',y)
# now it is an tuple .


# the o/p will be as  #################
#	tuple: (1, 2, 3, 4, 5)
#  	list: [1, 2, 3, 4, 5]
#	changed list: [1, 2, 6, 4, 5]
#	again tuple: (1, 2, 6, 4, 5)
######################################

# we cannot append in tuples ....

x = ( 1 , 2 , 3 , 4 , 5 )
x.append(6)
print(x)

# AttributeError: 'tuple' object has no attribute 'append'
# an error will occur..

# but we can change the tuple to list and we can append list and we can changed into tuple 
# like as previous method 

x = ( 1 , 2 , 3 , 4 , 5 )
print('tuple:',x)
y = list(x)
print(' list : ' ,y)
y.append(6)
print('changed list:',y)
y = tuple(y)
print("again tuple:",y)


# the o/p will be as 
#	tuple: (1, 2, 3, 4, 5)
#	list :  [1, 2, 3, 4, 5]
#	changed list: [1, 2, 3, 4, 5, 6]
#	again tuple: (1, 2, 3, 4, 5, 6)
##################################################

# we can increment in tuple ...

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# it will be print as ( 'apple' , 'banana', 'cherry' , orange ')

# we cannot remove items in tuple ...
# but we can remove by changing the tuple to list and list to tuple ...
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# the o/p will be as ( 'banana' , 'cherry' )

# we can delete tuple totally ....
# but a error will occur 

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 
#this will raise an error because the tuple no longer exists.

# we can unpack a tuple and we can call by a variable
# for e.g.,

tuple = ( 'apple' , 'banana' , 'orange' , 'kiwi' )
(red,blue,green,yellow) = tuple 
print(red)
print(blue)
print(green)
print(yellow)

# we can call like this ......

# asterisk *
# if we call this aestrisk value , the after value will be comes under same value.

tuple = ( 'apple' , 'banana' , 'orange' , 'kiwi' , 'melon' , 'mango' , 'papaya' )

( red , blue , green , orange , *pink ) = tuple
print(red)
print(blue)
print(green)
print(orange)
print(*pink)


# the o/p will be as 

#apple
#banana
#orange
#kiwi
#melon mango papaya

#######################################3

# we can give the value aestrisk value in any place 

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# the o/p will be as 

# apple
# mango papaya pineapple
# cherry
###########################################


# we can use loop in tuples and list ...


# we can join tuples add and multiply

# we can add ....

x = ( 1 , 2 , 3 , 4 )
y = ( 'a' , 'b' , 'c' , 'd' )
c = x + y 
print(c)

# the o/p will be as (1, 2, 3, 4, 'a', 'b', 'c', 'd')

# we can multiply ...


x = ( 1 , 2 , 3 , 4 )
y = x * 2 
print(y)

#  the o/p will be as (1, 2, 3, 4, 1, 2, 3, 4)

###########################################

# we can count how many numbers are there with count()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

# it will be print as 2 
# becoz 5 is 2 times appears in the tuple ...
#######################