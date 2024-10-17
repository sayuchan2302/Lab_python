from Lab3.Task1.Point import Point
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.point = Point(x, y)

    def inside(self, pointOther):
        return self.point.distanceTo(pointOther) < 0

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __mul__(self, other):
        return self.area() * other.area()

    def __truediv__(self, other):
        return self.area() / other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    @abstractmethod
    def p(self):
        pass

    @abstractmethod
    def area(self):
        pass
