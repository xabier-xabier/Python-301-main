# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self,name,mass,distance,temp_day,temp_night,diameter,atmosphere):
        self.name=name
        self.mass=mass
        self.distance=distance
        self.temp_day=temp_day
        self.temp_night=temp_night
        self.diameter=diameter
        self.atmosphere=atmosphere
        pass

    def __str__(self):
        return f"""
        The mass of {self.name} planet is {self.mass}, its diameter is {self.diameter} in (km)
        the distance between {self.name} to sun is {self.distance}. The temperature during day is around {self.temp_day}
        but during night is around {self.temp_night}. The atmosphere is composed by {self.atmosphere}"""

        pass
    pass

name="Jupiter"
mass="1.898 * 10^27 kg"
distance= "741000000 km"
temp_day="-100 Celsius"
temp_night="-160 Celsius"
diameter= 139820
atmosphere="Hydrogen and Helium"

jupiter=Planet(name,mass,distance,temp_day,temp_night,diameter,atmosphere)

print(jupiter)
