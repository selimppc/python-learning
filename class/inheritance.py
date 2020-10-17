# inheritance
# Base class
class Animal:
    """this class will be inheritated"""

    def eat(self):
        print('eat')


class Mammal(Animal):
    """
        Animal: Parent
        Mamman can : eat and walk
    """

    def walk(self):
        print('walk')


class Fish(Animal):
    """
        Animal: Parent
        Fish can : eat but can not walk, 
        can swim
    """

    def swim(self):
        print('swim')


# print
m = Mammal()
m.eat()
