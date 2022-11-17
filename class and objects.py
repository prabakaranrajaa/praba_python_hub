# PYTHON OOPS
# CLASS AND OBJECT

from cairo import STATUS_INVALID_CONTENT


class demo():
    pass

a = 10 
print(type(a))
# it will print class 'int'

# class is a type
print(type(demo))
# it will print class 'type'

print('--------------------------------------')

class car():
    pass

a = 10

swift=car()
# swift is object
# car is class
print(isinstance(a,int))
print(isinstance(swift,car))


print(type(swift))
# it will print as class '__main__.car'
# here main programming special variable car inside the class is swift

#########################################################

# class Attributes

class student():
    name = 'rock'
    age = 19
    
# get attribute = getattr() method
# we can pass 3 argument in attribute
print(getattr(student, 'name'))
print(getattr(student, 'age'))
# it will give error attribute error
print(getattr(student, 'code','i luv python'))
# now no error will occur

# dot notation (.)

print(student.name)
print(student.age)


#setattr setting attribute 

setattr(student,'name','! R O C K ')
print(student.name)
# it will change

# we can create ,  change , delete  in setattr

setattr(student,'code','python')
print(student.code)

student.city='tvl'
print(student.city)
# we can create dot notation object and we can print


print(student.__dict__)
print( '  - - - - - - - - - - - - - - - -- - ')

delattr(student, 'city')
print(student.__dict__)
print( '  - - - - - - - - - - - - - - - -- - ')
del student.code
print(student.__dict__)

print( '  - - - - - - - - - - - - - - - -- - ')
print( '  - - - - - - - - - - - - - - - -- - ')
print( '  - - - - - - - - - - - - - - - -- - ')


################################# 
# instance attributes

class user():
    course = 'java'
    

o = user()
print(user.__dict__)

print(user.course) # printing class attribute

print(o.__dict__)
print(o.course)
o.course = 'c++'
print(o.course)
print(o.__dict__)

# but it can't change the class attribute that means java

o2 = user()
print(o2.course)

# if we want instance attribute .. we can create a dict value
# but it can't change the main attribute with instance attribute


##############################################

# class methods

class meb():
    name = 'rock'
    age = 19
    
    def printall():
        print('name :',meb.name)
        print('age :',meb.age)
meb.printall()

print(meb.printall)

print(meb.__dict__)

#################################################

# instance methods

# if we want to call a instance methods 
# class  function and object we have to call .. is the procedure to call instance methods 

class mebs():
    name = 'rock'
    age = 19
    
    def printall(self,code):
        print('name :',mebs.name)
        print('age :',mebs.age)
        print('code : ',code)
                
o = mebs()
o.printall('python')
mebs.printall(o,'python')

#################################################
