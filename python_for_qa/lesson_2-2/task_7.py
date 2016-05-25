__author__ = 'Stepan_Pelykh'


def palindrome(a):
    if a[::1]==a[::-1]:
        print (a + " - is a palindrome")
    else:
        print (a + " - is not a palindrome")

if __name__ == "__main__":
    a='blablalb'
    b='pararap'
    c='qaqaooaqaq'

palindrome(a)
palindrome(b)
palindrome(c)