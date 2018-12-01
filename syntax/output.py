"""
Several ways to print out the program
Version: 0.1
Author: slynxes
Date: 2018-12-01
"""
import math

# Print()
print('Hello World')
print(5 + 2)
print(bin(5))
print(oct(5))
print(hex(5))

# Formatted String Literals
num1 = 5
num2 = 10
result = num1 + num2
print(f'{num1} + {num2} = {result}')
print(f'The value of pi is {math.pi:.5f}')

# The String format() Method
print("I'm {}, I'm {} years old".format('slynxes', 26))
print("he's {1}, he's {0} years old".format(30, 'Alandi'))

# Old string formatting
print('The value of pi is %5.3f' % math.pi)


