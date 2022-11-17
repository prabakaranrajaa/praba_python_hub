#########################################
#										#
#										#
#	  Python While Loop 				#
#										#
#########################################

# while loop

#  the while loop we can execute a set of statements as long as a condition is true.

# for e.g.,

i = 1
while i < 10 :
	print(i)
	i += 1

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


# break 
# if the condition is true it will break the loop and stop ...

# for e.g.,

i = 1 
while i < 10 :
	i + = 1
	if i == 3 :
		break
	print(i)
	
# the o/p as  
# 1
# 2
# 3


# continue  
# if the continue is true , it doesn't will print the number we given,
# continue statement we can stop the current iteration, and continue with the next.
i = 1 
while i < 10 :
 	i + = 1
 	if i == 3:
 		continue
 	print(i)

# the o/p as 
# 1 
# 2 
# 4 
# 5
# 6
# 7
# 8 
# 9 
# 10

# else statement in while loop
# we can run a block of code once when the condition no longer is true

i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")
  
# the o/p as 
# 1
# 2
# 3
# 4 
# 5
# 6 
# 7 
# 8 
# 9
# 1 is no longer less than 10

# we can print odd or even numbers with while loop .

# even numbers

i = 1
while i <= 20 :
	i += 1
	if i %2 == 0:
		print(i)
		
# the o/p as 
# 2 
# 4
# 6
# 8 
# 10
# 12
# 14
# 16
# 18
# 20


# odd numbers

i = 0
while i <= 19 :
	i += 1
	if i % 2 != 0 :
		print(i)


# the o/p as 
# 1
# 3
# 5 
# 7
# 9
# 11
# 13
# 15
# 17
# 19























