# Build a fruit stand that has a barrel for fruit and fruits have
# a name and a price
# you should be able to get the total cost of the barrel given the number of fruit in it
# and their cost
# a barrel can only hold one fruit type

# Fruit obj

class Fruit:
    def __init__(self, name, fruit_type):
        self.name = name
        self.fruit_type = None

# Barrel obj

class Barrel:

    def __init__(self, type, count):
        self.fruit_list = []

    def add_fruit(self):
        self.fruit_list.append(Fruit(name))
        # if options == "":
        #     self.fruit_count += 1
        #     print(f"{options} has been added.")
        # elif self.fruit_type == None:
        #     self.fruit_type = fruit
        #     self.fruit_count += 1
        # else:
        #     return "Invalid"
    
    def type_of_fruit(self):
        for i in self.fruit_list:
            pass
    
    def remove_amt(self):
        

    
    def reset_barrel(self):
        pass 




"""
Make a menu class that asks a user if they want to do:
1. add to a barrel
2. get the type of fruit in a barrel
3. remove an amount from the barrel
4. reset the barrel, emptying it and setting the type to none
5. exit

ALSO Make the needed barrel methods
"""