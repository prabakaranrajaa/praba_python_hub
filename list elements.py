#################################################
#						#
#						#
#	 	Python List			#
#						#
#						#
#################################################

# Lists are used to store multiple items in a single variable.

# Lists are created using square brackets
# list = [ ]

# for e.g.,

list = [ "apple" , "orange" , "banana" , "mango" ]
print(list)

# it will print output ['apple', 'orange', 'banana', 'mango']

# List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.

# dupilcate means it has same values as in the list 

list = [ "apple" , "orange" , "banana" , "mango" , "apple" , "cherry" ]
# here i have apple two times
# but it will allows two times ... and many times so it is allow duplicate value...
print(list)

# length is different from list
# list start from index 0 , 1 , 2 ,  3 ..... for countings
# length start from 1 , 2 , 3 ........ for countings



list = [ "apple" , "orange" , "banana" , "mango" ]
print(len(thislist))
# it will print the length as 4 

# list - items have any data 
# int or float or string or bool values whatever 

list = [ "apple" , 2 , False , 5.634 , 2j , "end" ]
print(list)
# it i print this , it will print as ['apple', 2, False, 5.634, 2j, 'end']

a = [ ]

# the empty list is will print type is list

a = [ 5 ]
print(type(a))
# or a single value cell type is list but in tuple it will be differ ...
# it will print type as list .

# 	difference between these 4 data types value .... 

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

a = [ 5 , 4 , 2 , 9 , 2 , 1 ]
print(a[2])

# the output will be  as 2  becoz the 0th index is 5 and 1st is 4 and the 2nd is 2.

a = [ 2 , 3 , 6 , 8 , 9 , 5 , 7 ]
print(a[-2])

# the negative indexing will get reverse from -1 , -2 , -3 , -4 .......



# like string we can do the list tooo as range of index
# here length and range index will take as 1 not 0 ....
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# the output will be ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# the output will be  ['apple', 'banana', 'cherry', 'orange']


# we can check the items ,

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# we can change the values ....

thislist = ["apple", "banana", "cherry"]
print(thislist)
# it will print the same .
thislist[1] = "orange"
# it will print after we changed on 1st index.
print(thislist)

# we can change range of items ..

a = [ 'batman' , 'superman' , 'ironman' , ' black adam ' , 'he man' , ' hti-man' , 'captain' ] 
print(a)
a[1:3] = [  'black panther' , 'hulk' ] 
print(a)

# the output will be ['batman', 'black panther', 'hulk', ' black adam ', 'he man', ' hti-man', 'captain']

# we can change 

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# the output will be ['apple', 'blackcurrant', 'watermelon', 'cherry']

# it will replace 1 value to 2 value ..
# we can change 2 or 3 value to single value ..


# insert items 
# insert()

thislist = ["apple", "banana", "cherry"]
####
thislist.insert(2, "watermelon")
####
print(thislist)
# the o/p will be as ['apple', 'banana', 'watermelon', 'cherry']

# we can put this insert value to insert any elements ....


# append items
# append()

# we can append any values ..

a = [ 1 , 2 , 3 , 4 , 5 ]
a.append(0)
print(a)

# it will be append on the last item... [ 1 , 2 , 3 , 4 , 5 , 0 ] 


# extend items 
# extend()

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# the o/p will be as ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# we can extend like this ...

# we can change iterable values from... 
# list  == / tuple , set , dict ..

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# the o/p will be as ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# remove items
# remove ()

# we can remove the items in list

a = [ 1 , 2 , 3 , 4 , 5 ]
a.remove(2)
print(a)

# it will be remove the value  ..
# it will not take as index value ..


# if we want to remove specified index
# we can pop


# pop items
# pop()

a = [ 1 , 2 , 3 , 4 , 5 , 6 ]
a.pop(2)
print(a)
#the o/p will be as [ 1 , 2 , 4 , 5 , 6 ] 


# if we want to remove the last item 
# we can give empty pop ()

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# it will remove the last item and it will give output..



# delete item

#  del 

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# it will remove first index item

# if we want to delete the entire item 

thislist = ["apple", "banana", "cherry"]
del thislist

# we can give like this ...

# clear items 

# clear()

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# the o/p will be as  [ ] 
# an empty cell


# In LIST we  can

# insert
# append
# extend
# remove
# pop
# del
# clear

########################################################

