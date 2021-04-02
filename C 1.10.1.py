class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getSize(self):
        return print(f"Rectangle({self.x},{self.y},{self.width},{self.height})")

fig1 = Rectangle(10,4,3,2)

fig1.getSize()


