import random

def return_3(s=None, i=None):
    """
    >>> return_3(s=True)
    '3'

    >>> return_3(i=True)
    3

    >>> return_3(i=True)
    '4'
    """
    if s:
        return '3'
    elif i:
        return 3


if __name__ == '__main__':
    import doctest
    doctest.testmod()
