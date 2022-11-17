#########################################
#										#
#										#
# 				TRY BLOCK     	        #
#				        				#
#########################################

# compiled time error  : means we missing colon or comma like that
# run time error : means it will occur error when we running 

# for e.g.,
a = 10 #/ 0 
print(a) # it will give runtime error : zero division error 

############################

try:
	a = 10/0
except Exception as e :
	print(e)
# it will give program o/p as division by zero

##############################

# try except else 

try :
	n = int(input(''))
	a = 10 / n
except Exception as e:
	print(e)
else :
	print(a)
	
##################################

# try except finally
# finally if we have except or we don't have except it will print finally

try :
	n = int(input(''))
	a = 10 / n
except Exception as e:
	print(e)
else :
	print(a)
finally :
	print('Tq u')
	
######################################

# type of exception

print(dir(locals()['__builtins__']))
# it will print all bultin exception'
print(len(dir(locals()['__builtins__'])))

#######################################

# name error exception
# if the definition or variable anything is not there it will exception
# if we want to print a there is no a defined value so it will take exception
try :
	print(a)
except Exception as e:
	print(e)
# or we can print customized message
	print('a is not defined')
	
#################################

try : 
	print(10/0)
except ZeroDivisionError as e:
	print(" denominator can't be zero ")

###############

try :
	print('rock')
except ValueError as e :
	print(e)
	print(' enter values only [numbers]')
	
################

try :
	a = [ 10 , 20 , 30 , 40 ]
	print(a[0])
	print(a[100])
# there is no index 100 
except IndexError :
	print('invalid index')
###################

try :
 f = open('sample.txt')
except FileNotFoundError :
	print('file not found')
else :
	print(f.read())
	
#####################

# handling multiple exception 

try :
 	a = 10/20
 	print(a)
 	b = [ 10 , 20 , 30 ]
 	print(b[10])
# index 10 is not there
except ZeroDivisionError :
	print('denominator can"t be zero')
except IndexError :
	print('Invalid Index')
	
# we can print multiple exception
################################################################
