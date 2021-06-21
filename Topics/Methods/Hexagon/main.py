import math
    

class Hexagon:
    def __init__(self, t):
        self.t = t
    def get_area(self):
        s = (3 * math.sqrt(3) * self.t ** 2)/ 2
        return round(s, 3)
