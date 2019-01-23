"""
返回函数，高阶函数除了可以接受函数作为参数外，还可以返回函数
def func1():
    ...
    def func2():
        ...
    ...
    return func2

Version: 0.1
Author: slynxes
Date: 2019-01-14
"""


def count():
    def add_num(x, y):
        return x + y
    return add_num


def func():
    for i in range(5):
        def sum_num():
            return i * i
    return sum_num


if __name__ == '__main__':
    f = count()
    print(f(2, 3))

