# inheritance
# Base class
class Animal:
    """this class will be inheritated"""

    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    """
        Animal: Parent
        Mamman can : eat and walk
    """

    def __init__(self):
        self.weight = 2
        super().__init__()

    def walk(self):
        print('walk')


# print
m = Mammal()
print(m.age)
print(m.weight)
