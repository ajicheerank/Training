##1 Area of the circle
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def circle_area(self):
        return ("Area of the circle with {} is {}".format(self.radius, math.pi* (self.radius**2)))

if __name__ == '__main__':
    c = Circle (10)
    print(c.circle_area())

##2 Area of the rectangle

class Rectangle:
    def __init__(self,length,width):
        self._length = length
        self._width = width
    
    def rec_area(self):
        return ("Area of rectangle with length of {} and width of {} is {}".format \
                (self._length, self._width, (self._length * self._width)))
    
if __name__ == '__main__':
    c = Rectangle (10, 10)
    print(c.rec_area())

##3 Class Person

class Person:
    def __init__(self,name):
        self.name = name
    
    def legally_change_name(self, new_name):
        self.name = new_name
        
    def introduce_myself(self):
        return ("My name is {}".format(self.name))
    

if __name__ == '__main__':
    p = Person("Aji")
    print(p.introduce_myself())
    p = Person("Paul")
    print(p.introduce_myself())
    p.legally_change_name ("Paul Chamba")
    print(p.introduce_myself())
       