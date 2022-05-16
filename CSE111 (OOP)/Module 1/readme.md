# Module 1 
Module 1 contains : 
**Lecture 1,2,3,4,5,6,7**

## Lecture 1

Intro to OOP | Class & Object

A class is a blueprint

An object is simply an object created from that class (blueprint)




## L3

>object's memory location





## L4
> parameterized constructor | Instance variable


> Waht is instance and attribute in Python?  

An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object and it is defined inside the constructor function, __init__(self,..) of the class.  
so, basically instance variable and attributes are similar.

<br>

Any property from design class (aka Instance variable) cannot be accessed or used without the object reference. 

```py
#==== Design class ======
class Student: 
    def __init__(self,name, id):
        self.name = name # instance var
        self.roll = id   # instance var

#=================
print(name) # will give us error
print(id) # will give us error

# only way to access poperty (instance variable) from design class  is through object reference.
stu1 = Student('Rajo', 21101078) # stu1 object created

print(stu1.name)
# now it will print 'Rajo' as we can access instance variable trhough object reference 


```

We can update instance variable even after creating object by using object reference. 
For example, if we want to change the name of stu1 object, we can do the below:
```py
#....
stu1.name = 'Faysel'
stu1.id = 21101048

```
This will update the instance variable (with respect to object)


Summary: We've learnt so far-   
* Default constructor 
* parameterized constructor
* Instance variable, attributes, properties.

