from Lab3.Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def p(self):
        return (self.w + self.h) * 2

    def area(self):
        return self.w * self.h
