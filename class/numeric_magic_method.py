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

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
# arithmetic operation
conbined = point + other
print(conbined.x, conbined.y)
