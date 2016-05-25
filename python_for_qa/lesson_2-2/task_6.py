__author__ = 'Stepan_Pelykh'


even_num = lambda a: {key: key ** 2 for key in xrange(2, a+1, 2)}

print even_num(100)
