"""
filter(function, iterable)
    function: 函数
    iterable: 可迭代对象
    filter()用于过滤iterable, 返回符合function条件的可迭代对象
    iterable的每个元素作为function的参数传入，进行判断，然后返回True或False
    最后将返回True的元素形成一个可迭代对象。

Version: 0.1
Author: slynxes
Date: 2019-01-13
"""


def odd_list(list_data):
    """
    过滤出列表中所有的奇数
    :param list_data:
    :return: 奇数列表
    """
    return list(filter(lambda x: x % 2 == 1, list_data))


def is_positive(num):
    """
    判断是否大于0
    :param num:
    :return:
    """
    return num > 0


def positive_list(list_data):
    """
    过滤出列表中所有正数
    :param list_data:
    :return: 正数列表
    """
    return list(filter(is_positive, list_data))

