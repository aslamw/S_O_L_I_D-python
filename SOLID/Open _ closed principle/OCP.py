"""Neste exemplo, uma classe abstrata 'Shape' define um método area(). 
As subclasses Rectanglee Circleextendem Shapee implementam seu próprio 
cálculo de área. A classe 'Shape' está aberta para extensão, 
pois novas formas podem ser adicionadas extendendo a classe Shape, 
mas fechada para modificações, pois a lógica de cálculo de área está 
encapsulada nas subclasses existentes."""

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
