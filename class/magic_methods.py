# first letter of every word will be uppercase.
class Point:

    # magic method __init__
    # constructor
    def __init__(self, x, y):
        """
            two attributes x and y 
            that belong point instances of point object
        """
        self.x = x
        self.y = y

    # magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
