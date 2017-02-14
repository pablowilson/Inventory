
"""
  >>> n
  42

"""
n = 42
def hello(g):
    f = ''
    while (g > 0):
        f += 'tell me '
        g -= 1
    print(f)
hello(5000)
#Place your solution code on the line below


if __name__ == '__main__':
    import doctest
    doctest.testmod()




































