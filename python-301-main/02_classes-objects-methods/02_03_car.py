# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():

    def __init__(self,model,year,max_speed):
        self.model=model
        self.year=year
        self.max_speed=max_speed
        pass

    def use(self):
        self.max_speed+=5

    def __str__(self):
        return f"""
        The model of the car is {self.model}, the year is {self.year}
        and the maximum speed is {self.max_speed}"""
        pass

ferrari=Car("Ferrari", 2006,320)
toyota_fortuner=Car("Toyota fortuner",2010,220)

for i in range(1,11,1):
    ferrari.use()

print(ferrari)
print("\n")
print(toyota_fortuner)



    
