# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

from numpy import pi

class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width
        pass

    def area(self):
        area=self.length*self.width
        return area
    
    def perimeter(self):
        perimeter=2*self.length+2*self.width
        return perimeter
    

class Circle:

    def __init__(self,radius):
        self.radius=radius
        pass

    def area(self):
        area=pi*self.radius**2
        return area
    
    def perimeter(self):
        perimeter=2*pi*self.radius
        return perimeter

        

rectangulo=Rectangle(10,4)  # Units in cm
circulo=Circle(2.5)         # Units in cm

print(f"""
      The area of the rectangle is {rectangulo.area()} cm2
      The perimeter of the rectangle is {rectangulo.perimeter()} cm""")

print("\n")

print(f"""
      The area of the circle is {round(circulo.area(),2)} cm2
      The perimeter of the rectangle is {round(circulo.perimeter(),2)} cm""")