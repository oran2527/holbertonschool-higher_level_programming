#!/usr/bin/python3
class MyList(list):
    """Mylist class."""

    def print_sorted(self):
        """print_sorted - function.
           self - object."""
        l = []
        l = self.copy()
        l.sort()
        print(l)
