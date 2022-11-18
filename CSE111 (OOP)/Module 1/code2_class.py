# House - class design
# TAW lecture 6

class House:
    
    def __init__(self):
        self.window = 4 # instance var with default value
        self.door = 2  # instance var with default value

    def view(self):
        print(f"{self.window} window, {self.door} doors")

#=====================================

house1 = House()
house2 = House()

house1.view()
house2.view()
# print the view with default values

# update the values
house1.door = 3
house2.window = 6

# call view() method again
house1.view()
house2.view()
# print the view with updated values