# Build a fruit stand that has a barrel for fruit and fruits have
# a name and a price
# you should be able to get the total cost of the barrel given the number of fruit in it
# and their cost
# a barrel can only hold one fruit type

class Barrel:
    def __init__(self, type_of_fruit, count):
        self.type_of_fruit = type_of_fruit
        self.count = count

    def add_fruit(self):
        self.count += 1
        return f"{self.type_of_fruit} has been added."
    
    def fruit_type(self):
        return self.type_of_fruit
    
    def remove_amt(self, amount=0):
       self.count -= amount

    def reset_barrel(self):
         self.count == 0 




"""
Make a menu class that asks a user if they want to do:
1. add to a barrel
2. get the type of fruit in a barrel
3. remove an amount from the barrel
4. reset the barrel, emptying it and setting the type to none
5. exit

ALSO Make the needed barrel methods
"""
