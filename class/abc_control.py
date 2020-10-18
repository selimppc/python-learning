# this a classic example of polymorphism
# abstract base classes

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox.")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList.")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
texbox = TextBox()
draw([ddl, texbox])

# this a classic example of polymorphism
