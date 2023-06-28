# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle():

    def __init__(self,owner,year,gas,insurance):
        self.owner=owner
        self.year=year
        self.gas=gas
        self.insurance=insurance
        pass

    def __str__(self):
        return f"""
            The owner of this vehicle is {self.owner}, was manufactured in {self.year} year
            uses {self.gas}"""
    

class Car(Vehicle):

    def __init__(self, owner, year, gas, insurance,brand,doors,engine):
        super().__init__(owner, year, gas, insurance)
        self.brand=brand
        self.doors=doors
        self.engine=engine

class Toyota(Car):

    def __init__(self, owner, year, gas, insurance, brand, doors, engine,model,color):
        super().__init__(owner, year, gas, insurance, brand, doors, engine)
        self.model=model
        self.color=color

    def __str__(self):
        return f"""
        The owner of this car is {self.owner}, was manufactured in {self.year}, uses {self.gas}.
        The car brand is {self.brand}, the car has {self.doors} doors. The size of the engine is {self.engine}.
        This Toyota model is {self.model} and is {self.color} color."""


class Motorbike(Vehicle):

    def __init__(self, owner, year, gas, insurance,brand,speed,engine):
        super().__init__(owner, year, gas, insurance)
        self.brand=brand
        self.speed=speed
        self.engine=engine


class Kawasaki(Motorbike):

    def __init__(self, owner, year, gas, insurance, brand, speed, engine,color,model):
        super().__init__(owner, year, gas, insurance, brand, speed, engine)
        self.color=color
        self.model=model

    def __str__(self):
        return f"""
        The owner of this motorbike is {self.owner}, was manufactured in {self.year}, uses {self.gas}.
        The motorbike brand is {self.brand}, maximum speed is {self.speed} km/h. the size of the engine is {self.engine}.
        This Kawasaki model is {self.model} and is {self.color} color."""


prius=Toyota("Raul Blanco",2015,"gasoline","yes","Toyota",5,"1798 cc","Prius","blue")
ninja=Kawasaki("Pedro Gonzalez",2018,"gasoline","yes","Kawasaki",325,"1000 cc","green","Ninja 1000sx")


print(prius)
print("\n")
print(ninja)
