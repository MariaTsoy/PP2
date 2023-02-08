class Shape():
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, leng):
        Shape.__init__(self)
        self.length = leng

    def area(self):
        return self.length * self.length


shape = Shape()
shape.area()
square = Square(2)
print(square.area())
