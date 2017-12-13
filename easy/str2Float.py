from functools import reduce

def str2float(s):
    """利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456："""
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n = s[::-1].find('.')
    left, right = s.split('.')

    integer = reduce(lambda x, y: 10 * x + y, map(lambda x: digits[x], left))
    decimal = reduce(lambda x, y: 10 * x + y, map(lambda x: digits[x], right))
    res = integer + decimal / (10**n)
    print(res)
    return res


str2float('1234.45')
