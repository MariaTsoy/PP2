class Shape():
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, leng, widt):
        Shape.__init__(self)
        self.length = leng
        self.width = widt

    def area(self):
        return self.length * self.width


rect1 = Rectangle(2, 3)
print(rect1.area())
