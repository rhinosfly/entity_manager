## @package shape
#
# definition for shape class and type enums

## imports
import pyray as pr

class Shape():
    def __init__(geometry):
        self.geometry = geometry
class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ctype(self):
        return pr.Vector2(self.x, self.y)
class Line(Shape):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def ctype(self):
        return (self.p1.ctype(), self.p2.ctype())
class Rectangle(Shape):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def ctype(self):
        return pr.Rectangle(self.x, self.y, self.width, self.height)
