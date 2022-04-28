from abc import ABC, abstractmethod
import math
from matplotlib import pyplot as plt


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return self.h*self.v

    def perimeter(self):
        return 2*(self.h+self.v)

    def draw(self):
        plt.axes(xlim=(0, 10), ylim=(0, 10))
        x = [2, 2+self.h, 2+self.h, 2, 2]
        y = [2, 2, 2+self.v, 2+self.v, 2]
        plt.text(0.5, 9, '[ Rectangle ] \n Area = {:.1f}, Perimeter = {:.1f}'. format(self.area(), self.perimeter()))
        plt.plot(x, y)
        plt.title('ShapeGraph', loc='center', pad=10)
        plt.show()

class Triangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return 0.5*self.h*self.v

    def perimeter(self):
        return math.sqrt(self.v**2+self.h**2)+self.h+self.v

    def draw(self):
        plt.axes(xlim=(0, 10), ylim=(0, 10))
        x = [2, 2+self.h, 2, 2]
        y = [2, 2, 2+self.v, 2]
        plt.text(0.5, 9, '[ Tiriangle ] \n Area = {:.1f}, Perimeter = {:.1f}'. format(self.area(), self.perimeter()))
        plt.plot(x, y)
        plt.title('ShapeGraph', loc='center', pad=10)
        plt.show()

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi*(self.r**2)

    def perimeter(self):
        return 2*math.pi*self.r

    def draw(self):
        lines = plt.axes(xlim=(0, 10), ylim=(0, 10))
        circle_center = (4, 4)
        circle_radius = self.r
        circle_draw = plt.Circle(circle_center, circle_radius, fc='w', ec='b')
        lines.add_patch(circle_draw)
        lines.set_aspect('equal')
        plt.text(0.5, 9, '[ Circle ] \n Area = {:.1f}, Perimeter = {:.1f}'. format(self.area(), self.perimeter()))
        plt.title('ShapeGraph', loc='center', pad=10)
        plt.show()

class RegularHexagon(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return (3*math.sqrt(3)*(self.r**2))/2

    def perimeter(self):
        return 6*self.r

    def draw(self):
        plt.axes(xlim=(0, 10), ylim=(0, 10))
        x = [4, 4+self.r, 4+self.r+self.r/2, 4+self.r, 4, 4-self.r/2, 4]
        y = [2, 2, 2+self.r, 2+2*self.r, 2+2*self.r, 2+self.r, 2]
        plt.text(0.5, 9, '[ RegularHexagon ] \n Area = {:.1f}, Perimeter = {:.1f}'. format(self.area(), self.perimeter()))
        plt.plot(x, y)
        plt.title('ShapeGraph', loc='center', pad=10)
        plt.show()

def main():
    shapes = [
        Rectangle(5, 4),
        Triangle(3, 4),
        Circle(3),
        RegularHexagon(2),
    ]

    for shape in shapes:
        print(shape)
        print('넓이 = {}' .format(shape.area()))
        print('둘레 = {}' .format(shape.perimeter()))
        shape.draw()
        plt.show()

if __name__ == '__main__':
    main()
