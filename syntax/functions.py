"""
Functions Exercise

Version: 0.1
Author: Slynxes
Date: 2018-12-03
"""


def is_palindromic_str(n):
    """
    判断是不是回文数
    方法: 通过将数字转换为字符串, 对比字符串的首尾
    :param n:
    :return: bool, 是返回True, 否则False
    """
    num_str = str(n)
    num_str_len = len(num_str)
    count = num_str_len // 2
    i = 0
    palindromic = True
    while i < count:
        if num_str[i] != num_str[num_str_len - 1 - i]:
            palindromic = False
            break
        i = i + 1
    return palindromic


def is_palindromic_list(n):
    """
    判断是不是回文数
    方法：通过将数字转为列表，然后反转列表进行比较
    :param n:
    :return: bool, 是返回True, 否则False
    """
    num_list = list(str(n))
    num_list_reverse = num_list[:]
    num_list_reverse.reverse()
    return num_list_reverse == num_list


def is_palindromic_math(n):
    """
    判断是不是回文数
    方法：通过数学将数字反转，与原数据比较
    :param n:
    :return: bool, 是返回True, 否则False
    """
    temp = n
    n_compare = 0
    while temp > 0:
        n_compare = 10 * n_compare + temp % 10
        temp //= 10
    return n == n_compare


def f_default_arg(username='admin', password='123'):
    """
    函数参数添加默认值
    :param username:
    :param password:
    :return:
    """
    print(f'username: {username}, password: {password}')


def f_variable_length_arg(*arg):
    """
    可变长参数
    :param arg:
    :return:
    """
    for i in arg:
        print(i)

def f_variable_length_dict_arg(**args):
    """
    参数args是一个元素个数为任意个的字典
    :param args:
    :return:
    """
    for k, v in args.items():
        print(k, v)


def f_reference_value(my_list):
    """
    引用传递
    :param my_list:
    :return:
    """
    my_list.append([1, 3, 5])
    print(my_list)


if __name__ == '__main__':
    pass
