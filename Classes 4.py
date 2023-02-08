import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        return self.x, self.y

    def dist(self, point2):
        return math.sqrt(pow(self.x - point2.x, 2) + pow(self.y - point2.y, 2))


point1 = Point(2, 3)
point2 = Point(1, 1)

print(point1.show())

point1.move(3, 4)
print(point1.show())
print(point1.dist(point2))
