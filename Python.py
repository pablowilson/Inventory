class Footwear:
    """
      >>> f = Footwear('Sling-back', 8.5, '1234-0')
      >>> f.style
      'Sling-back'
      >>> f.size
      8.5
      >>> f.sku
      '1234-0'
      >>> f.type
      'Unspecified'
      >>> f.print_size()
      'size 8-1/2'
      >>> f2 = Footwear('Hightop', 10, '1234-19')
      >>> f2.print_size()
      'size 10'
      >>> print(f)
      Sling-back (size 8-1/2)
      >>> print(f2)
      Hightop (size 10)
    """
    def __init__(self, style, size, sku):
        self.style = style
        self.size = size
        self.sku = sku
        self.type = "Unspecified"
        
    def print_size(self):
        if(type(self.size) == int):
            return "size " + str(self.size)
        elif(type(self.size) == float):
            return "size " + str(int(self.size)) + "-1/2"
        else:
            return "you didnt type a number you twat"

    def __str__(self):
        return "{0} ({1})".format(self.style, self.print_size())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
