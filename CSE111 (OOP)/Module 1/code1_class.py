"""Class, Object, Constructor, attributes, methods()"""

# class Design (Blueprint)

class Student: 
    
    def __init__(self,name, id):
        self.name = name #instance variable
        self.roll = id  #instance variable

    def info(self):
        print(self.name)
        print(self.roll)

    
        

#=====================================

# Creating Object or we can manipulate data using the class
# variable = class_Name()

stu1 = Student("Rajo", 21101078) #object 1
stu2 = Student("Faysel",21101079) #object 2

print(stu1, stu2) # output will show us the memory location or address of these objects/instances

stu1.info()
stu2.info()

print(stu1.roll, " ", stu2.roll)