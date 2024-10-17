from Lab3.Task1.Shape import Shape


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def p(self):
        return self.side * 4

    def area(self):
        return self.side ** 2