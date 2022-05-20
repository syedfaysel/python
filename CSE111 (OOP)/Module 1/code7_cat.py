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