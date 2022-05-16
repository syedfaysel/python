# car class

class Car:
    def __init__(self, name, model):
        self.name = name        #instance var
        self.model = model      #instance var
        self.wheel = 4          #instance var with default value
                                #can be updated anytime

    def view(self):
        print(f"The model of the {self.name} is {self.model}")
#===================================

car1 = Car("Audi", 2022)
car2 = Car("Lamborghini", 2025)

car1.view()
car2.view()