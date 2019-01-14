"""
sorted(iterable, [key = func], [reverse = True/False])
    iterable: 可迭代对象，即排序对象
    key = func: 将iterable中的元素作为func的参数输入，以返回值进行排序，但结果还是对应的元素
    reverse: 是否翻转排序结果

Version: 0.1
Author: slynxes
Date: 2019-01-14
"""
from operator import itemgetter


def score_sorted(score, key='by_name'):
    """
    按名字或值排序，使用lambda或itemgetter创造函数
    :param score:
    :param key:
    :return:
    """
    if key == 'by_name':
        # return sorted(score, key=lambda x: x[0])
        return sorted(score, key=itemgetter(0))
    if key == 'by_value':
        # return sorted(score, key=itemgetter(1))
        return sorted(score, key=lambda x: x[1])


if __name__ == '__main__':
    stu_score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(score_sorted(stu_score, 'by_value'))

