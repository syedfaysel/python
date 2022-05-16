# Module 1 
Module 1 contains : 
**Lecture 1,2,3**

## Lecture 1

Intro to OOP | Class & Object

A class is a blueprint

An object is simply an object created from that class (blueprint)






## L4

Any property from design class cannot be accessed or used without the object reference. 

```py
#==== Design class ======
class Student: 
    def __init__(self,name, id):
        self.name = name
        self.roll = id

#=================
print(name) # will give us error
print(id) # will give us error

# only way to access poperty from design class is through object reference.
stu1 = Student('Rajo', 21101078) # stu1 object created

print(stu1.name)
# now it will print 'Rajo'


```

