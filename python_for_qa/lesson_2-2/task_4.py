__author__ = 'Stepan_Pelykh'


def comb():
    i = [True, False]
    for a in i:
        for b in i:
            for c in i:
                res = (a or not b) and (c or not a)
                print 'a =', a, 'b =', b, ' c =', c, 'result is', res

if __name__ == "__main__":
    comb()