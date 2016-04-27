__author__ = 'Stepan_Pelykh'
# Program calculates the number of times that the string 'hi' appears in the given string and change 'hi' to 'bye'.

my_string='Hi Mark you should me answer hi or hi-hi funny guy'
ms=my_string.lower()
print'''Number of 'hi' string = ''', ms.count('hi')
print('-----------------------')
print ms.replace('hi', 'by')
