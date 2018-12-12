"""
Data Type Exercise

Version: 0.1
Author: Slynxes
Date: 2018-12-12
"""
import time
import os
import string
import random


def slide(chars):
    """
    跑马灯
    :param chars: 字符串
    :return:
    """
    while True:
        os.system('clear')
        print(chars)
        temp = chars[0:-1]
        chars = chars[-1] + temp
        time.sleep(2)


def random_str1(length):
    """
    生成指定长度的由字母、数字组成的随机字符串
    :param length:
    :return:
    """
    return random.sample(string.ascii_lowercase
                         + string.ascii_uppercase
                         + string.digits, length)


def random_str2(length):
    """
    生成指定长度的由字母、数字组成的随机字符串
    :param length:
    :return:
    """
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_str = ''
    for i in range(length):
        random_str = random_str + random.choice(letters)
    return random_str


def get_suffix(file_path):
    i = -1
    character = file_path[i]
    suffix = character
    while character != '.':
        character = file_path[i]


if __name__ == '__main__':
    print(random_str2(10))

