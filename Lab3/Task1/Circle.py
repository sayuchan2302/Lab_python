from Lab3.Task1.Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def p(self):
        return 2 * self.radius * 3.14

    def area(self):
        return self.radius ** 2 * 3.14