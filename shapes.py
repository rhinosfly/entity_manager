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
    def smallest_rect(self):
        rec = Rectangle(0,0,0,0)
        if p1.x < p2.x:
            rec.x = p1.x
            rec.width = p2.x - p1.x
        else:
            rec.x = p2.x
            rec.width = p1.x - p2.x
        if p1.y < p2.y:
            rec.y = p1.y
            rec.height = p2.y - p1.y
        else:
            rec.y = p2.y
            rec.height = p1.y - p2.y
        return rec
            
class Rectangle(Shape):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def ctype(self):
        return pr.Rectangle(self.x, self.y, self.width, self.height)
