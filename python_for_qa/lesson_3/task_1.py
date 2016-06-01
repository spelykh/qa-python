__author__ = 'Stepan_Pelykh'


# list comprehension

num = [i for i in range(1, 10000) if i % 2 == 0 and i % 3 == 0]
print(num)

# filter function

num1 = filter(lambda x: x % 2 == 0 and x % 3 == 0, range(1, 10000))
print(num1)

