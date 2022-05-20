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
# Tester part, 

# b1 = Book("How to live alone", "Syed Faysel")

# b1.set_price(255)
# print(b1.get_price())

# b1.details()


# to use import class , go to code6_test1.py
    