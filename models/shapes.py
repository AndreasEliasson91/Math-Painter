from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x: int, y: int, color: tuple):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, canvas):
        pass


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, color: tuple):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, canvas):
        pass


class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.x:(self.x + self.width), self.y:(self.y + self.height)] = self.color


class Triangle(Shape):
    def __init__(self, x: int, y: int, base: int, height: int, color: tuple):
        super().__init__(x, y, color)
        self.base = base
        self.height = height

    def draw(self, canvas):
        pass


class Square(Shape):
    def __init__(self, x: int, y: int, width: int, color: tuple):
        super().__init__(x, y, color)
        self.width = width

    def draw(self, canvas):
        canvas.data[self.x:(self.x + self.width), self.y:(self.y + self.width)] = self.color
