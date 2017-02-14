"""
    >>> fun(3)
    17
    >>> fprime(3)
    5
    >>> dub(1, 6)
    [2, 4, 6, 8, 10]
"""
def dub(j, k):
    s = []
    for i in range(j, k):
        s += [2 * i]
    return s
def fun(x):
    return 3 * x ** 2 - 13 * x + 29
def fprime(x):
    return 6 * x - 13
print(fun(4))
print(fprime(4))
print(dub(1, 5))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
