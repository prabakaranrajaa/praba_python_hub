############ init method ############

class user():
    def __init__(self):
        print('hello world')
        
gd = user()
gm = user()

# it will print hello world 2 times

######################################

class userm():
    def __init__(self,name):
        print('hello')
        self.name = name
        
    def printall(self):
        print('name :',self.name)
        
o1 = userm('rock')
o1.printall()
o2 = userm('lgrock')
o2.printall()
print(o1.__dict__)
print(userm.__dict__)

##########################################