class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_rectangle(self):
        return "Rectangle coordinates : ({}), ({})".format(self.point1.get_point(), self.point2.get_point())
