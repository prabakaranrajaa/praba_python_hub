##########################################
"""



		Python File-Handling
	

"""
###########################################


# file handling 

# read and write the file

file = open("sample.txt","r")  # put file location ... & 'r' means read mode 
print(file.read())

# it will give o/p as what we given in the file , it will give o/p.

######################


try:
	file=open("samples.txt","r") # giving wrong name as a file
	print(file.read())
except FileNotFoundError:
	print("Error: File Not Found")
else:
	file.close()

# it will give o/p as file not found

#####################

"""

readline in python 


"""

# if the file have many line we can use this 
# for e.g.,

file = open("sample.txt","r")
print(file.readline())

# it will print first line 

# the o/p as hello world

# if i want another line or more than line ,

file = open("sample.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())

# it will print 3 lines of it ....
"""
hello world

goodbye world

hello rock

"""
#######################

# if i want char of the line 

file = open("sample.txt","r")
print(file.readline())
print(file.readline(5)) # we can give like this 5th char want to print

# it will give o/p 
"""

hello world

goodb

"""

#########################


# readlines()


file = open("sample.txt","r")
print(file.readlines())

# it will give o/p as 
"""
['hello world\n', 'goodbye world\n', 'hello rock\n', 'leave me alone\n', 'nutter tools\n', 'thugs tools\n', 'professional tools\n', '\n']
"""
# it will print as list ...
###########################

# loop line by line ()


file = open("sample.txt","r")
for line in file:
	print(line)
	
# it will give o/p as 
"""
hello world

goodbye world

hello rock

leave me alone

nutter tools

thugs tools

professional tools

"""
# instead of using readline() , we can use loop line by line method for total lines output.

##############################

# write or overwrite a file

# write ()

file = open("sample.txt","w")
file.write("adding a new line in file")

file = open("sample.txt","r")
print(file.read())

# if the file has any line it will erased and it will print ur input line
# the o/p as 
"""
adding a new line in file # what we giving input 
"""
##########################

# overwrite()

file = open("sample.txt","a") # append mode or ovewriting the file
file.write("adding a 2nd line in this file")

file = open("sample.txt","r")
print(file.read())

# it will give o/p as

"""
adding a new line in file
adding a new line in fileadding a 2nd line in this file

"""
# it is appending on that file
###############################

# deleting a file 

# want to delete a file 

import os
if os.path.exists("delfile.txt") :# checking whether if the path contains that file
# if it is exist
	os.remove("delfile.txt")
	print('file successfully deleted')
else:
# if it is not exist , we can  give like this
	print("File Not Found") 
	
# here u can remove not only the file but also any folder

import os
if os.path.exists("newfolder12"):
	os.rmdir("newfolder12")		# rmdir for removing the folder
	print("folder removed")
else:
	print("folder is not exist")
		  
#######################################

#	file.close() 

# closing the file when we done the work

file = open("sample.txt","r")
print(file.read())
file.close()
# we read the file after closing.......

###################################

# create a file()

# if we want to create a file


# "x" = create a file, if the file is already there it will occur error as the file is already exist.

#############################
# creating a file
try :
	file = open("newfile.txt","x") 
	print("file is created")
except FileExistsError:
	print("File already exist")
	

# writing a line in file
file = open("newfile.txt","w")
file.write("this is new line of this file")
file.close()

# reading the file
file = open("newfile.txt","r")
print(file.read())
print("file is opened")

##############################


#############################################################################


"""
			Python File - Handling
			
 CREATING A FILE
 READING A FILE
 WRITING A FILE
 OVERWRITING A FILE
 READING LINES IN A FILE
 READING LINE OF CHAR IN A FILE
 DELETING A FILE

"""

##################################################################################









	
	
