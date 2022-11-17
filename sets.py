##################################
#								 #
# 			Python SETS 		 #
#								 #
##################################


# sets {}

# A set is a collection which is unordered, unchangeable*, and unindexed.

set = { 'apple' , 'banana' , 'cherry' }
print(set)
# it will print o/p as {'banana', 'apple', 'cherry'}

# Note: the set list is unordered, meaning: the items will appear in a random order.


# sets are not allowed duplicate values..

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# here 2 apple is there 1 will be removed
# and the o/p will be as randomed order...

# like wise list & tuples 
# set contains data types 

set1 = {"abc", 34, True, 40, "male"}

print(set1)
# the o/p will be as randomed .......
print(type(set1))

# the type is set .

# for loop in set

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# it will be print the answer as randomed order ..

# NOTE : Once a set is created, you cannot change its items, but you can add new items. #

# add()
# for adding items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# it will add items and print answer as randomed ....

# update()
# updating the items in sets 
# we can add sets in sets  
 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# the o/p will be as randomed ..

# we can add set in list  or tuples 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# like this 
# as well as . it will print as randomed answer......


# removing or discarding items

# remove() or # discard () 

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# it will be removed items ,,,

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# it also remove but an error occur 


# pop ()

# deleting the particular item

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



# clear() 

# for clearing the set

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# the o/p will be as set() 

# set union and intersection like maths 

# union ()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# it will united the sets and randomed answer will come ...


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# union and update are like same only ...


# Note: Both union() and update() will exclude any duplicate items.


# intersection_update()

#The intersection_update() method will keep only the items that are present in both sets.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# it will be printed as {'apple'}

# intersection ()

#The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
# we can create a new  set and o/p as {'apple'} .

# symmetric_difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
# it will keep all and removed the duplicates and print the answer

# symmetric_difference()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
# it will return a new set and removed the duplicate items..




# sets 
######################################
# clear() 
# pop () 
# remove() or # discard () 
# update()
# add()
# union () and update() 
#intersection ()
#intersection_update()
#symmetric_difference()
#symmetric_difference_update()
########################################







