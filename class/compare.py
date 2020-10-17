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

    # comparison magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point = Point(1, 2)
other = Point(1, 2)

# compare
# this will return False as both address of memories are different.
# after adding comparison magic method it will return True
print(point == other)


# Reference : https://rszalski.github.io/magicmethods/#comparisons
