# Module 1 
Module 1 contains : 
**Lecture 1-11**

## L1

Intro to OOP | Class & Object

A class is a blueprint

An object is simply an object created from that class (blueprint)




## L3

>object's memory location

self = unique memory address or location of individual obejct.





## L4

> parameterized constructor | Instance variable


> What is instance and attribute in Python?  

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

<br>


## L9  
  

> Import Class   
Example program - 5 : Designing a book class  
Getter , setter method


introdued with getter setter method. (know more from internet and upcoming lectures)  

Set Method
: Set method will <mark>update</mark> the variable or data.

Get Method
: Get method will <mark> return </mark>       the data to user which is updated by set method

get & set method comes in pair:  
(check full code on code5_book.py)

```py
def set_price(self,pricce):
    self.price = price

def get_price(self):
    return self.price

# we can access these methods like: 
#object_ame.set_price(argument)
book1.set_price(200)
print(book1.get_price)
```
<br>

**Importing a Class :**
<br>    

> To use a class in another program, we can import the class to that python file. There are some ways discussed in the details code. check code5_book.py, code6_test1.py  

<br>  


```py
# Designing a book class / Design class

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0
    # setter method
    def set_price(self,price):
        self.price = price

    # getter method
    def get_price(self):
        return self.price

    
    def details(self):
        print(f"Name of the Book : {self.name} \nAuthor: {self.author} \nPrice : {self.price}$")

#====================================
```


To import this class from a file let's say code5_book.py to another file code6_test1.py (in the same directory)

<mark>way 1: We can import the full python file which contains the Book class

```py
import code5_book

# to access the class inside the code5_book file,
# we need to reference it by the file_name

book1 = code5_book.Book("Opekkha", "Humayon Ahmed")

```

<mark>way 2: we can import only the class by using :

```py
from code5_book import Book
book2 = Book("Something Big", "Syed Rajo")

# to access the class inside the code5_book file,
# in that case we don't need to reference it by the file_name since we've imported the actual class Book

```

Know more about aliasing :

```py
import Book as b
# as b is used for aliasing, now Book can be accessed by typing b 
```

With that being said, lecture 9 ended here.

<br>


## L10
> Pass by reference

we pass an argument by the reference, (not the actual value)

```py
# cat class, pass by reference example

class Cat:
    def __init__(self, color, action):
        self.color =color
        self.action = action
    
    def view(self):
        print(f"{self.color} cat is {self.action}")

    #pass by reference
    def compare(self, anotherCat):
        if self.action == anotherCat.action:
            print(f"Both {self.color} and {anotherCat.color} cats are {self.action}")
        else:
            print(f"Action of {self.color} and {anotherCat.color} cats are different")


#=============================================

cat1 = Cat("Brown","Jumping")

cat2 = Cat("Black", "Running")

cat3 = Cat("White","Jumping")

cat1.view()

cat1.compare(cat2)
cat1.compare(cat3)

# in the compare method, we pass the argument by reference of another object. 

# we did not pass the actual object,
#  rater passed the reference or location of that object 
# so that the compare method can access that object and its attributes
```


## L11
<br>

> pass by reference example code

> More discussion on pass by value, pass by reference. **Important**


```py
class Cat:

    def __init__(self,color, action):
        self.color = color
        self.action = action
    
    # understanding pass by value and reference
    def view(self, num, clr):
        num = num + 10
        clr1 = clr
        clr1[0] = 'Green'

        print(f"Inside Method: clr1 = {clr1}")
        print(f"Inside Method: clr = {clr}")
        print(f"Inside Method num = {num}")

#=======================

c1 = Cat("Red","Jumping")
x = 50
colors = ['Black', 'Red', 'White']

#inside method
c1.view(x,colors)

#outside method
print(f"outside method: colors = {colors}")
print(f"outside method: num = {x}")

```

Notice that, the value of x is not changed even after the method called.
but the value of the list colors is changed.

Because, inside the method, num was passed by the value of x = 50, 
not the reference or location of x. 

On the other hand, clr was passed by the reference of the list colors. 
As the reference was passed, any changes made to the reference,
will eventually change  the actual variable. 
That's why the list colors is changed even outside the method but not the variable x.

understanding pass by value and pass by reference is really important.


With that being said, lecture 11 is done and module 1 is done.



