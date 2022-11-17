#########################################
#					#
#	Python List items 		#
#					#
#					#
#########################################

# list sorting means
# alphabetically arrangement ...

a = [ "orange" , 'banana' , 'kiwi' , 'melon' , 'apple' , 'mango' ]
a.sort()
print(a)
# it will be sort as alphabetically...

# for numbers

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# also same  it will be [23, 50, 65, 82, 100]


########## sorting descending ###########

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# it will be print z to a ...

##########

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# like wise this also print backward 100 to 0....

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# this will be print as string lower to higher value 

# a to z ........


# for if we want normal reverse to print 


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# if we put reverse () 
# it will print normallly as cherry , kiwi , orange ,banana .........


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# copy()
# we can copy a list  and we can print 

###########333333  Join List ############################


a = [ 1 , 2 , 3 ]
b = [ 4 , 5 , 6 ]
c = a + b
print(c)

# it will be joining ...
# another method

a = [ 1 , 2 , 3 ]
b = [ 4 , 5 , 6 ]
a.extend(b)
print(a)

# it also give output


a = [ 1 , 2 , 3 , 4 ]
b = [ 'a' , 'c' , 'd' ]
for x in b :
    a.append(x)	
    
print(a)

# it will print as [ 1 , 2, 3 , 4 , 'a' ,'b' ,'c' ,'d' ].

####### list methods ###########

#	Method		Description
#	append()	Adds an element at the end of the list
#	clear()	Removes all the elements from the list
#	copy()	Returns a copy of the list
#	count()	Returns the number of elements with the specified value
#	extend()	Add the elements of a list (or any iterable), to the end of the current list
#	index()	Returns the index of the first element with the specified value
#	insert()	Adds an element at the specified position
#	pop()	Removes the element at the specified position
#	remove()	Removes the item with the specified value
#	reverse()	Reverses the order of the list
#	sort()	Sorts the list







