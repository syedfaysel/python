
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

"""
Notice that, the value of x is not changed even after the method called.
but the value of the list colors is changed.

Because, inside the method, num was passed by the value of x = 50, 
not the reference or location of x. 

On the other hand, clr was passed by the reference of the list colors. 
As the reference was passed, any changes made to the reference,
will eventually change  the actual variable. 
That's why the list colors is changed even outside the method but not the variable x.

understanding pass by value and pass by reference is really important.
"""


rajo = dict()
saifa = {"Name":"Saifa Tasnim", "ID":12425, "Gender":"female", "Dept": "CSE", "favs":["mahir","nipu", "rajo"]}

print(saifa)


print(saifa["favs"][2])