import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, arg):
        result = math.sqrt((self.x - arg.x)**2 + (self.y - arg.y)**2)
        return result

# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
#
# print(p1.dist(p2))