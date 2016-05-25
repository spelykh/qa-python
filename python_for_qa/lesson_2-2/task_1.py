__author__ = 'Stepan_Pelykh'


def conc(str):
    if len(str) < 10:
        return None
    else:
        res = str[:10]+str[-10:]
    return res

if __name__ == "__main__":
    print conc('0123456789adfthsdfhty9874563210')
