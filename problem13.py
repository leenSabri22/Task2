from abc import ABC, abstractmethod


class SystemComponent(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(SystemComponent):
    def draw(self):
        print("Rectangle")


class Group(SystemComponent):
    def __init__(self):
        self.items = []

    def add(self, shape):
        self.items.append(shape)

    def draw(self):
        for item in self.items:
            item.draw()
