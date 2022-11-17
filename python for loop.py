#########################################
#										#
#										#
#			Python FOR LOOP				#
#										#
#										#
#########################################


# for loop 
# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


for x in range(11) :
	print(x)


# the o/p as will print 
# 1 
# 2
# 3 
# 4 
# 5
# 6
# 7
# 8 
# 9 
# 10

# printing even numbers using for loop

for x in range(11) :
	if x % 2 == 0 :
		print(x)
		
# the o/p as 
# 2 
# 4
# 6
# 8 
# 10


# printing odd numbers using for loop 

for x in range(11):
	if x % 2 != 0 :
		print(x)
		
# the o/p as 
# 1
# 3
# 5 
# 7 
# 9

#################################################

# continue statement

for x in range(11) :
	if x % 5 == 0 :
		continue
	print(x)
	
# the o/p as 
# 1 
# 2
# 3 
# 4
# 6
# 7 
# 8 
# 9 

# it won't print 5 and 10 becoz we stop it and continue the loop

# we can print it with min range to max range
# for e.g.,

for x in range(5 , 11 ):
	print(x)
	
# the o/p as 
# 5
# 6
# 7 
# 8 
# 9 
# 10

# else in for loop

for x in range(5,20,3):
# here min range = 5 , max = 20 and 3 is adding to the next number
	print(x)
# finally else 
else:
	print('loop done')

# the o/p as 
# 5
# 8
# 11
# 14
# 17
# loop done

# break

for x in range(10) :
	if x == 5 :
		break
	print(x)
else:
	print('loop done')

# the o/p as 
# 1 
# 2
# 3
# 4

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

#########################################

# nested loop

# A nested loop is a loop inside a loop.

#for e.g

for x in range(1,2) :
	for y in range(0,2) :
		print(x,y)
	
# the o/p as
# 1 0
# 1 1

# pass statement in for loop 

# for e.g.,

for x in range(0,10) :
	pass

# having an empty for loop like this, would raise an error without the pass statement



###############################################################################################

