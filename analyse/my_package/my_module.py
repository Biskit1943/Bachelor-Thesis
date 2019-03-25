"""my_module.py"""

def my_sum(*args, l=None):
    result = 0
    if l and type(l) is list:
        for n in l:
            result += n
    else:
        for n in args:
            result += n

    return result

def my_pow(a, b):
    result = a
    for _ in range(1, b):
        result = result * a

    return result
