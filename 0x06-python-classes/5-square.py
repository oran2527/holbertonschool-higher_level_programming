#!/usr/bin/python3
class Square:
    """Square class."""

    def area(self):
        """Area function."""
        return self.__size ** 2

    def __init__(self, size=0):
        """Init function."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter function."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """my_print function."""
        x = 0
        x = self.__size

        if x is 0:
            print("")
        else:
            for i in range(0, x):
                for j in range(0, x):
                    print("#", end="")
                print("\n", end="")
