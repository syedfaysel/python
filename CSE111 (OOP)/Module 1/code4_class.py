# Lecture 8: Dog class

class Dog:
    def __init__(self, name, color):
        self.name = name 
        self.color = color


    def poke(self):
        print(f"{self.color} dog {self.name} is barking, Ghew Ghew")

    def updateColor(self, color):
        self.color = color

    def updateName(self, name):
        self.name = name

#=======================================


dog1 = Dog("Tommy","black")
dog2 = Dog("Alpha", "brown")


dog1.poke()
dog2.poke()

dog1.updateColor("white")   # color updated
dog2.updateName("Rover")    # name updated

dog1.poke()
dog2.poke()


#===========================================
#new topic learned in lecture 8

print(dog1.__dict__)
print(dir(dog1))

#know more about __dict__ attribute and dir() method.
# Check github readme.md


