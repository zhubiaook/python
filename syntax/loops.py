"""
Loops Statement
Version: 0.1
Author: slynxes
Date: 2018-12-01
"""
import math
import random

# 求1到100的偶数之和
sum_even = 0
for num in range(2, 100, 2):
    sum_even += num
print(f'The sum of the even numbers from 1 to 100 is: {sum_even}')

# 猜数字游戏, 猜错了提示数字是大了还是小了
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

# 输入一个数，判断是不是素数
num = int(input('num = '))
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
if is_prime:
    print(f'{num} is a prime.')
else:
    print(f'{num} is not a prime.')

# 输入两个正整数，求最大公约数和最小公倍数
# 使用辗转相除法
input1 = int(input('num1 = '))
input2 = int(input('num2 = '))
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
least_common_multiple = (input1 * input2 / greatest_common_divisor)
print(f'The Greatest common divisor of '
      f'{input1} and {input2} is: {greatest_common_divisor},'
      f'\nand the least common multiple is {least_common_multiple}')
