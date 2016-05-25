__author__ = 'Stepan_Pelykh'


def last_element(str):
    if len(str) == 0:
        return None
    elif str.split(','):
        str2 = str.split(',')[-1]
        return str2
    else:
        return str

if __name__ == "__main__":
    print last_element('')
    print last_element('This,string,is,separated,by,comma')
    print last_element("this string doesn't contains comma")


