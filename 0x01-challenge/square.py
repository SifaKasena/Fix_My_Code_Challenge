#!/usr/bin/python3
"""
square class
"""


class Rectangle:
    """ Rectangle class definition """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a rectangle instance """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the rectangle """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Returns the perimeter of a rectangle """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returs a string representation of a rectangle instance """
        return "{}/{}".format(self.width, self.height)


class square(Rectangle):
    """ square class definition """

    def __init__(self, *args, **kwargs):
        """Initializes a square instance"""
        super().__init__(*args, **kwargs)

    
if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
