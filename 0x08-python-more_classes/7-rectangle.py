#!/usr/bin/python3
class Rectangle:
    """Rectangle class."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ function. call setter"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width function getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """width function setter."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height function getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """height function setter."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area function."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter function."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """__str___ function."""
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string = string + str(self.print_symbol)
            if i is not self.__height - 1:
                string = string + '\n'
        return string

    def __repr__(self):
        """__repr__ function."""
        string1 = "Rectangle("
        a = str(self.__width)
        string2 = ", "
        b = str(self.__height)
        string3 = ")"
        return eval('string1 + a + string2 + b + string3')

    def __del__(self):
        """__del___ function."""
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
