#####################################
#									#
#									#
# 			Python INPUT 			#	
#									#
#									#
#####################################

# input 
# input means we asking  something like 

# for e.g.,

name = input()
print(name)

# i am calling a variable as input for name , if i type a name in there interpreter
# it will print name  [ what i type i will give ] 

# we can call the input as any datatype like float , int , str....
# for e.g.,

number = int(input('enter ur number: '))
# calling a number as variable by giving int 
# it only accept int value or else it will occur error,
print(number)
print('hey!.. friend your number is : ',number)
# it will print output.

name = str(input('enter ur name : '))
# here i use f string for this 
print(f'hello {name} , today is a good day for u.')
# it will print o/p.

# like wise we can call any ..
# we can concatenate
# for e.g.,

a = int(input('enter the number : '))
b = int(input('enter the number : '))
c = a + b 
print(f' here ur number is : {c}')

# like this 

f_name = str(input('enter ur first name : '))
l_name = str(input('enter your last name : '))
name = f_name + l_name 
print(f"your good name is {f_name} {l_name}.")
print('tq u ...')

#######################################################################