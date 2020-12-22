import math

#Initializing Parent Class 
class Shape:
    def __init__(self, name):
        self.name = name
    #This function gets overridden by Subclasses/Child Classes    
    def area(self):
        area = 0
        return area
#Initializing Subclass Rectangle          
class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        return area
        

#Initializing Subclass Square    
class Square(Shape):
    def __init__(self, name, side):
        self.name = name
        self.side = side
    #Define method for area of a square A = x^2 (x squared)   
    def area(self):
        area = self.side **2
        return area
#Initializing Subclass Triangle
class RightTriangle(Shape):
    def __init__(self, name, leg1, leg2):
        self.name = name
        self.leg1 = leg1
        self.leg2 = leg2
    #Define method for Area of a Right Triangle provided the two perpindicular sides
    def area(self):
        area = (self.leg1 * self.leg2) / 2
        return area
    
#Initializing Subclass Circle
class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    #Define class method for area of a circle using the imported math.pi
    def area(self):
        area = math.pi * (self.radius)**2
        return area

#Storing the class objects and their attributes in a variable   

shape = Shape('Shape')    
rect = Rectangle('Rectangle', 5, 15)
sqr = Square('Square', 5)
tri = RightTriangle('Right Triangle', 1, 8)
crcl = Circle('Circle', 4)


#Printing the name and area of each Shape given the defined attributes


print("The area of the undefined {} is: {}".format(shape.name, shape.area()))
print("The area of the {} is: {}".format(rect.name, rect.area()))
print("The area of {} is: {}".format(sqr.name,  sqr.area()))
print("The area of the {} is: {}".format(tri.name, tri.area()))
print("The area of the {} is: {}".format(crcl.name, crcl.area()))

    
    
