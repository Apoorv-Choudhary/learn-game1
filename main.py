from point import *
from rectangle import *

if __name__ == '__main__':
    point1 = Point(2, 3)
    point2 = Point(5, 6)

    rectangle = Rectangle(point1, point2)
    print(rectangle.get_rectangle())

    guess_point = Point(4, 4)
    print(guess_point.get_point())
    print(guess_point.is_inside_rectangle(rectangle))
