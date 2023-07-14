#!/usr/bin/python3
"""Module contains efinition of class Square"""


class square:
    """Square class definition"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a square insatance with kwargs"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Get the perimeter of a Square instance """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return string representation of a Square instance"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
