__author__ = 'Stepan_Pelykh'


def dupl(a):
    list1 = []
    for i in a:
        if a.count(i) >= 2:
            continue
        else:
            list1.append(i)
    print 'List without duplicates -', list1

if __name__ == "__main__":
    a = [1, 2, 3, 4, 4, 6, 2]
    print a
    dupl(a)