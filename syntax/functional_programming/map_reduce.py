"""
map(func, iterable)
    func(x)
reduce(func, iterable)
    func(x, y)

Version: 0.1
Author: slynxes
Date: 2019-01-14
"""
from functools import reduce


def capitalize_name(name):
    """
    字符串首字母大写
    :param name:
    :return:
    """
    return name.capitalize()


def normalize1(name_list):
    """
    使用map()规范化每个字符串元素
    :param name_list:
    :return:
    """
    return map(capitalize_name, name_list)


def normalize2(name_list):
    """
    使用map()规范化每个字符串，函数使用lambda
    :param name_list:
    :return:
    """
    return map(lambda name: name.capitalize(), name_list)


def str2num(str):
    """
    使用字典将字符转换为数字
    :param str:
    :return:
    """
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}
    return digits[str]


def fn(x, y):
    """
    将字符转换为数字
    :param x:
    :param y:
    :return:
    """
    global m, point
    if y == -1:
        point = -1
        return x
    else:
        if point == -1:
            m = m * 0.1
            return x + m * y
        else:
            return 10 * x + y


def str2float(str):
    """
    将字符串转换为浮点数
    :param str:
    :return:
    """
    point = 0
    m = 1
    return reduce(fn, map(str2num, str))


if __name__ == '__main__':
    m = 1
    point = 0
    print(str2float('10.235'))
