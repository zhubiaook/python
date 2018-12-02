"""
Loops Statement

Version: 0.1
Author: slynxes
Date: 2018-12-01
"""
import math
import random


def sum_even_num(num):
    """
    求1到100的偶数之和
    :return: 无返回值
    """
    sum_even = 0
    for i in range(2, num, 2):
        sum_even += i
    print(f'The sum of the even numbers from 1 to {num} is: {sum_even}')


def guess_number_game():
    """
    猜数字游戏, 猜错了提示数字是大了还是小了
    :return:
    """
    count = 0
    num = random.randint(1, 100)
    while count < 1:
        answer = int(input('Input a number: '))
        if answer < num:
            print('Guess it is small')
        elif answer > num:
            print('Guess it is big')
        else:
            print('Congratulation! you guessed it!')
            break
        count = count + 1
    print(f'The answer is {num}, you guessed it {count} times.')
    if count == 7:
        print('Your IQ needs to be charged')


def is_prime_number(num):
    """
    判断是不是素数
    :param num:
    :return: 是返回True, 否则返回False
    """
    square_root = math.sqrt(num)
    end = int(square_root)
    is_prime = True
    if square_root - end:
        for divisor in range(2, end + 1):
            if num % divisor == 0:
                is_prime = False
                break
    else:
        is_prime = False
    return is_prime


def get_gcd_lcm(input1, input2):
    """
    输入两个正整数，求最大公约数和最小公倍数
    使用辗转相除法
    :param input1:
    :param input2:
    :return: (gcd, lcm)
    """
    num1 = input1
    num2 = input2
    while True:
        if num1 > num2:
            reminder = num1 % num2
            if reminder:
                num1 = reminder
                num1, num2 = num2, num1
            else:
                greatest_common_divisor = num2
                break
        elif num1 < num2:
            num1, num2 = num2, num1
        else:
            greatest_common_divisor = num1
            break
    least_common_multiple = (input1 * input2 // greatest_common_divisor)
    return greatest_common_divisor, least_common_multiple
