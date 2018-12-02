"""
DESCRIPTION
Version: 0.0
Author: slynxes
Date: 2018-12-01
"""


def print_num(my_list):
    my_list.append([1, 2, 3])
    print(f'in: {my_list}')


your_list = [10, 20, 30]
print_num(your_list)
print(f'out: {your_list}')
