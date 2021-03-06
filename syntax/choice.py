"""
Choice statement

if CONDITION:
    STATEMENT
elif CONDITION:
    STATEMENT
else:
    STATEMENT

if x:
    STATEMENT

    只要 x 是非空数值, 非空列表，非空字符串，非空集合... 则判断为True
    下面为Fase:
        ''
        {}
        []
        0
        0.0


Version: 0.1
Author: slynxes
Date: 2018-12-01
"""
import math


def verify_account():
    """
    验证输入的用户名和密码是否正确
    :return: 无返回值
    """
    username = input('username: ')
    password = input('password: ')
    if username == 'admin' and password == '123':
        print('Verification passed')
    else:
        print('Verification failed')


def f(x):
    """
    分段函数求职
           3x - 5  (x > 1)
    f(x) = x + 2   (-1 <= x <= 1)
           5x + 3  (x < -1)
    :return: 无返回值
    """
    if x > 1:
        print(f'f(x) = {3 * x - 5}')
    elif x >= -1:
        print(f'f(x) = {x +2}')
    else:
        print(f'f(x) = {5 * x + 5}')


def metric_imperial():
    """
    英制单位与公制单位转换
    1in= 2.54cm
    :return: 无返回值
    """
    unit = input('Please enter the length unit(cm/in): ')
    num1 = float(input('Please enter th length: '))
    if unit == 'cm' or unit == '厘米':
        print(f'{num1}{unit} = {num1 / 2.54:.2f}in')
    elif unit == 'in' or unit == '英寸':
        print(f'{num1}{unit} = {num1 * 2.54:.2f}cm')
    else:
        print('Please input correct UNIT')


def get_valid_num(prompt):
    """
    强制用户输入正数
    :param prompt: 提示词
    :return: 输入合法的正数时，返回该数，否则返回False
    """
    i = 1
    while i <= 3:
        input_str = input(prompt).strip()
        if input_str.isdigit() and float(input_str) > 0:
            return float(input_str)
        else:
            print("Please input valid number.")
            i += 1
    print("Error more than 3 times")
    return False


def triangle_area():
    """
    输入三角形的三边长，如果能构成三角形，就求其面积
    输入的不是数字时，提示用户
    输入的数字前后有空格时，去除
    提示用户以公制的m为单位
    :return: 无返回值
    """
    length1 = get_valid_num('length1 = ')
    if length1:
        length2 = get_valid_num('length2 = ')
    else:
        length2 = False

    if length2:
        length3 = get_valid_num('length3 = ')
    else:
        length3 = False

    if (length3 and length1 + length2 > length3
            and length1 + length3 > length2 and length2 + length3 > length1):
        p = (length1 + length2 + length3) / 2
        area = math.sqrt(p * (p - length1) * (p - length2) * (p - length3))
        print(f'The area of the triangle with length of {length1},'
              f'{length2}, {length3} is: {area}')

