"""
Complexity analysis

Version: 0.1
Author: Slynxes
Date: 2018-12-03
"""


def o_1(n):
    """
    O(1): 复杂度不随数据规模的增加而变化
    :param n:
    :return:
    """
    result = 2**n
    return result


def o_logn(n):
    """
    O(logn): 2^x = n, x = log2^n
    :param n:
    :return:
    """
    i = 1
    sum_num = 0
    while i < n:
        sum_num += i
        i = 2 * i


def o_n(n):
    """
    O(n)
    :param n:
    :return: 求n个数据之和
    """
    sum_num = 0
    for i in range(1, n):
        sum_num += i
    return sum_num


def o_n_2(n):
    """
    O(n^2)
    :param n:
    :return:
    """
    sum_num = 0
    for i in range(n):
        for j in range(n):
            sum_num = sum_num + i +j
    return sum_num


def o_nlogn(n):
    """
    O(nlogn)
    :param n:
    :return:
    """
    for i in range(n):
        j = 0
        while j < n:
            j = 2 * n


def o_m_add_n(m, n):
    """
    O(m + n)
    :param m:
    :param n:
    :return:
    """
    sum_num = 0
    for i in range(m):
        sum_num += i
    for j in range(n):
        sum_num += j
    return sum_num


def o_m_multi_n(m, n):
    """
    O(m * n)
    :param m:
    :param n:
    :return:
    """
    sum_num = 0
    for i in range(m):
        for j in range(n):
            sum_num = i + j
    return sum_num


if __name__ == '__main__':
    print(o_n(100))
