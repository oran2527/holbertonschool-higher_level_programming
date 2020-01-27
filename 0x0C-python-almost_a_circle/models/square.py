#!/user/bin/python3
""" module point 10 square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init function
        size: size
        x: x
        y: y
        id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str function"""
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)
