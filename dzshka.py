class Shape:
    name = "Shape"
    color = "Green"

class Circle(Shape):
    color = "Blue"
    radius = 2
    area = 4
    def __init__(self):
        print("Circle")
        print(self.color)
        print(self.radius)
        print(self.area)
class Rectangle(Circle):
    color = "Red"
    length = 6
    width = 3
    area = 18
    def __init__(self):
        print("Rectangle")
        print(self.color)
        print(self.length)
        print(self.width)
        print(self.area)

class Triangle(Rectangle):
    color = "Yellow"
    base = 5
    height = 4
    area = 20
    def __init__(self):
        print("Triangle")
        print(self.color)
        print(self.base)
        print(self.height)
        print(self.area)
cl = Circle()
re = Rectangle()
tr = Triangle()