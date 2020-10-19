class Shape:
    def __init__(self, height, length):
        self.height = height
        self.length = length


class Triangle(Shape):
    def area(self):
        s = self.height * self.length / 2
        return s


class Rectangle(Shape):
    def area(self):
        s = self.height * self.length
        return s


a = int(input())
b = int(input())
print(Triangle(a,b).area())
print(Rectangle(a,b).area())