"""This file contains the base code which will be tested with each testing tool
to examine their differences for the analysis.
"""

def mul(a, b):
    """This function will multiply the first parameter with the second one."""
    return a*b

def calc_sum(*args):
    """Calculates the sum of the given args"""
    return sum(args)


class Base:
    def __init__(self, a):
        self.a = a

    def square(self):
        """This will calculate the square of self.a.

        The method will store the result in self.q and return it.
        """
        self.q = self.a * self.a
        return self.q


if __name__ == '__main__':
    print(mul(4, 4))
    b = Base(3)
    print(b.square())
    print(b.q)
    print(calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))

