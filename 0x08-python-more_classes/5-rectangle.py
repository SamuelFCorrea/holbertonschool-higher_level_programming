#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.__height = height
        self.__width = width

    def __str__(self) -> str:
        """Return a string"""
        rect = ''
        for i in range(0, self.area()):
            rect += '#'
            if i + 1 != self.area() and not (i + 1) % self.width:
                rect += '\n'
        return rect

    def __repr__(self) -> str:
        """Return a formal string"""
        return '{self.__class__.__name__}\
({self.width}, {self.height})'.format(self=self)

    def __del__(self):
        """Delete protocol"""
        print('Bye rectangle...')

    def area(self):
        """Return the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    @property
    def width(self):
        """Return property value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter property"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Return property value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter property"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
