#!/usr/bin/python3
'''Class Rectangle that inherits from Base and is parent
of the Square class'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle sets a rectangle and display it with
    the (display) method'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize the Rctangle class with the new pararameters:
        width(required), height(required), x(optional), y(optional),
        and use the id setter in the Base class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        '''Return a string with the object info
        [Rectangle] (id) x/y - width/height'''
        return '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        '''Update the rectangle with *args or **kwargs.
        to args the input must be (id, width, height, x, y)'''
        numargs = len(args)
        if numargs > 0:
            self.id = args[0]
        if numargs > 1:
            self.width = args[1]
        if numargs > 2:
            self.height = args[2]
        if numargs > 3:
            self.x = args[3]
        if numargs > 4:
            self.y = args[4]
        if numargs == 0:
            for key, value in kwargs.items():
                exec('self.{} = {}'.format(key, value))

    def area(self):
        '''Return the rectangle's area (width * height)'''
        return self.__width * self.__height

    def display(self):
        '''Print the rectangle with the coordenates and the character #'''
        for i in range(0, self.y):
            print('')
        for i in range(0, self.area()):
            if not i % self.width:
                for j in range(0, self.x):
                    print(' ', end='')
            print('#', end='')
            if i and not (i + 1) % self.width:
                print('')

    def num_check(self, value, name):
        '''Check if the number is valid and print TypeError and ValueError'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in ('width', 'height'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and name in ('x', 'y'):
            raise ValueError('{} must be >= 0'.format(name))

    def to_dictionary(self):
        '''Return a dictionary representation of the rectangle'''
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    @property
    def width(self):
        '''Return the width value of the rectangle'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Sets the width value and raises if it fails'''
        self.num_check(width, 'width')
        self.__width = width

    @property
    def height(self):
        '''Return property value of the rectangle'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Sets the width value and raises if it fails'''
        self.num_check(height, 'height')
        self.__height = height

    @property
    def x(self):
        '''Return the x value of the rectangle'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Sets the x value and raises if it fails'''
        self.num_check(x, 'x')
        self.__x = x

    @property
    def y(self):
        '''Return the y value of the rectangle'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Sets the y value and raises if it fails'''
        self.num_check(y, 'y')
        self.__y = y
