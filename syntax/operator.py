"""
Basic Operators
Version: 0.1
Author: slynxes
Date: 2018-12-01
"""

# Arithmetic Operators
# +
# -
# *
# /
# //
# %
# **
num1 = 5
num2 = 3
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2:.2f}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

# Comparison Operators
# >
# >=
# <
# <=
# !=
num1 = 5
num2 = 3
print(f'{num1} != {num2} : {num1 != num2}')

# Assignment Operators
# +=
# -=
# *=
# /=
# //=
# %=
# **=
num1 = 5
num2 = 3
num1 += num2
print(f'num1 = {num1}')

# Bitwise Operators
# &
# |
# ~
# ^
# <<
# >>
num1 = 0b110011
num2 = 0b100001
print(f'{bin(num1)} & {bin(num2)} = {bin(num1 & num2)}')
print(f'{bin(num1)} | {bin(num2)} = {bin(num1 | num2)}')
print(f'~{bin(num1)} = {bin(~num1)}')
print(f'{bin(num1)} ^ {bin(num2)} = {bin(num1 ^ num2)}')
print(f'{bin(num2)} << 2 = {bin(num2 << 2)}')
print(f'{bin(num2)} >> 2 = {bin(num2 >> 2)}')

# Logical Operators
# and
# or
# not
bool1 = True
bool2 = False
print(f'{bool1} and {bool2} = {bool1 and bool2}')
print(f'{bool1} or {bool2} = {bool1 or bool2}')
print(f'not {bool1} = {not bool1}')

# Membership Operators
# in
# not in
num1 = 5
array = {1, 3, 5}
print(f'{num1} in {array} = {num1 in array}')
print(f'{num1} not in {array} = {num1 not in array}')

# Identity Operators
# is
# is not
print(f'type(1) : {type(1)}')
print(f'type(True) : {type(True)}')
print(f'1 == True : {1 == True}')
print(f'1 is True : {1 is True}')
print(f'0 != False : {0 != False}')
print(f'0 is not False : {0 is not False}')
