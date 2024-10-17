from Lab3.Task1.Point import Point
from Lab3.Task1.Rectangle import Rectangle

p1 = Point (4,5)
p2 = Point (8,2)
    #overloading Point class
print (p1 + p2)
print (p1 - p2)
print (p1 * p2)
print (p1 / p2)
print (p1 >= p2)
print (p1 <= p2)
print (p1 != p2)
print (p1 == p2)
print (p1 > p2)
print (p1 < p2)
    #overloading shape
r1 = Rectangle(5,6,2,6)
r2= Rectangle(2,1,7,5)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)
print (r1 > r2)
print (r1 < r2)
print (r1 >= r2)
print (r1 <= r2)
print (r1 == r2)
print (r1 != r2)
    # distanceTo
print("len p1 -> p2 = ",p1.distanceTo(p2))
    #perimeter
print("perimeter r1 = " ,r1.p())
    # inside
print(r1.inside(p1))
    # area
print ("area r1 = " ,r1.area())