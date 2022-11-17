#####################################
# 									#
#									#
# 		Python Dictionaries 		#
#									#
#####################################

# Dictionaries = dict{}

# Dictionaries are used to store data values in key:value pairs...
# dict contains keys and values 

dict = {
	'name' : 'rock',
	'age' : 19 ,
	'code' : 'nothing'
}
print(dict)
# this will print the dict with keys and value 
# {'name': 'rock', 'age': 19, 'code': 'nothing'}


# if we want a single value .. # we can call like this ...

dict = {
	'name' : 'rock',
	'age' : 19 ,
	'code' : 'nothing'
}

print(dict['name'])

# the o/p will be as rock


# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# duplicates are not allowed here 
# duplicate keys are not allowed

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# here the key year comes two times but it will only one value as the o/p..

# the o/p will be as {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

# it will give the answer as 3 , becoz it didn't take duplicate keys 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(type(thisdict))
# dict can accept value str , int , float bool

# accessing items 
# get ()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
a = thisdict['model']
print(a)

# you can call this by a variable or u can call by this function get()
# for e.g.,

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
a = thisdict.get('brand')
print(a)


# keys()
# The keys() method will return a list of all the keys in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict.keys()
print(x)
# it will print o/p as the keys  dict_keys(['brand', 'model', 'year'])


# for adding items 

car = {
	'name' : 'benz',
	'speed' : '250 km/h',
	'type' : 'racing',
	'price' : '50M' ,
}
print(car)
# if we want to add a key and value 

x = car.keys()
print(x)
# for printing dict_keys

car['color'] = 'black'

print(x)
# printing dict_keys

print(car)
# printing the o/p car 



# as well as keys() we can call values() ...

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)

 # it will be o/p as dict_values(['Ford', 'Mustang', 1964])
 
 
# we can change the values 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
print(car)
# the o/p will be as  {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

### we can add a new item with value 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
print(car)

# we can change add and edit a item and update a new item


# keys() and values () contains both o/p is items()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)

# the o/p will be as dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# it gives the o/p as keys with values .

# like values and keys we can change items 


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print(car)

# the o/p will be as {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}


# keys() , values() , items() these three are similiar to add or edit or update a items .........


# we can change a values by this 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


# or we can add or update a value by this 
# update()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({'color':'red'})
print(thisdict)

# add or edit are most likely similiar becoz we are changing the values only and inserting a new keys ....


# for removing we can use pop()
# as like list , in list we can pop values 



# popitem()
# we can a pop a item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# it will pop the last value 


# del[]

# we can delete a single item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# model and it contains values will be removed and it will print answer...

# but we cannot delete a full dict with del function

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict)

#this will cause an error because "thisdict" no longer exists.

# if we want to delete total dict we can use this clear ()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# it will print the empty dict {} like set 

# note : dict and set are bot {}
# but dict contains keys and vaLue 
# but set doesn't contain the values and keys ........


# we can copy the dict by value copy()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# or else u can copy like this too

mydict1 = thisdict
print(mydict1)

# here dict is an data type value like that ...........

###### NESTED dictionary ###################


car = {
	'benz' : {
	'name' : 'mercedes' ,
	'year' : 2020
	},
	'lambo' : {
	'name' : 'lamboghirini gallodo',
	'year' : 2021
	},
	'bmw'  : {
	'name' : 'bmw m5 gt',
	'year' : 20222
	}
}
print(car)

# it will print o/p.

# u can give a variable 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# u can print also like.....


# dict 

# clear()
# keys()
# values()
# items()
# update()
# get()
# pop()
# copy()
# popitem()

#########################