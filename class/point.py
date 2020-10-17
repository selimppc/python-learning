# first letter of every word will be uppercase.
class Point:
    default_color = 'red'

    # magic method __init__
    # constructor
    def __init__(self, x, y):
        """
            two attributes x and y 
            that belong point instances of point object
        """
        self.x = x
        self.y = y

    # define a function
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()

# class atrributes are shared of instances of class
print(Point.default_color)

# call the class like a function
point = Point(1, 2)
print(type(point))
print(isinstance(point, Point))
