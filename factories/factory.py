import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # This is an inner class
    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    # Can make an instance of factory
    factory = PointFactory()


# class PointFactory:
#
#    @staticmethod
#    def new_cartesian_point(x, y):
#        return Point(x, y)
#
#    @staticmethod
#    def new_polar_point(rho, theta):
#        return Point(rho * math.cos(theta), rho * math.sin(theta))


# class Point:
# def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
#    if system == CoordinateSystem.CARTESIAN:
#        self.x = a
#        self.y = b
#    elif system == CoordinateSystem.POLAR:
#        self.x = a * math.sin(b)
#        self.y = a * math.sin(b)

# Can't overload init
# def __init__(self, rho, theta):


if __name__ == '__main__':
    p = Point(2, 3)  # can't hide initializer
    # p2 = PointFactory.new_polar_point(1, 2)
    # p3 = Point.PointFactory.new_polar_point(1, 2)
    p4 = Point.factory.new_polar_point(1, 2)
    print(p)
    # print(p2)
    # print(p3)
    print(p4)
