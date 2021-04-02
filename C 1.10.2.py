class Rectangle:
    def __init__(self, x, y):
        self.length = y
        self.width = x

    def get_info(self):
        return print(f"Rectangle: width = {self.width},\
length = {self.length}, square = {self.width * self.length}")


Rect1 = Rectangle(45, 32)

Rect1.get_info()
