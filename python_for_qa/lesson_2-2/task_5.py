__author__ = 'Stepan_Pelykh'


def sum13(a):
    newlist = []
    for i in a:
        if not (isinstance(i, bool) or isinstance(i, str)):
            if i == 13:
                break
            else: newlist.append(i)
    return sum(newlist)

b = [1, 'ola', 2, 3, False, 3, 13, 13, 2, True]
c = []

print (sum13(b))
print (sum13(c))



