# Module 1 
Module 1 contains : 
**Lecture 1,2,3,4,5,6,7**

## L1

Intro to OOP | Class & Object

A class is a blueprint

An object is simply an object created from that class (blueprint)




## L3

>object's memory location

self = unique memory address or location of individual obejct.





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
* Unique Memory location for individual object or instance


## L5
> In depth session | Revision of prev lectures

**Method**
Method is nothing but a function. When a function is used inside the class, that is called method. 

There is only a single difference between method and function is that, a method will automatically take 'self' while a function will not. 

There are three types of methods in Python: instance methods, static methods, and class methods.

**For now, let's focus on Instance method:**

```py

# class Design (Blueprint)

class Student: 
    
    def __init__(self,name, id):
        self.name = name #instance variable
        self.roll = id  #instance variable

    def info(self):
        print(self.name)
        print(self.roll)

# here info() is an instance method.
```
In the above code, info() is an instance method(). To call this method, we must call it by object refernce. We can see that, info() method takes self as an parameter/argument.

```py
stu1 = Student('Rajo', 21101078)
stu2 = Student('Faysel', 21101079)

stu1.info() #info() method called for stu1 object
stu2.info() # info() method called for stu2 object
```
output:
code1_class.py

```cmd
Rajo
21101078
Faysel
21101079
```


## L6,L7,L8
Example program practice and revison
see code2_class.py, code3_class.py, code4_class.py


Python built in attribute : 
__ dict __   
by using __ dict __ attribute we can get the attributes through a dictionary of an object.

```py
print(objectName.__dict__)
```
This will print the dictionary showing all the attributes of an object .

Another built in method is **dir()** method. 
If we pass an object into this method, it will return us a list of all the built in methods, built in attributes and everything of the object.

```py
print(dir(objectName))
```

With that being said, done with lecture 8.



