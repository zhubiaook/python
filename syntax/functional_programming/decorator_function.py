"""
装饰器(decorator)
    装饰器是一个函数，是一个返回函数的高阶函数
    @decorator
    def func
        ...
    等同于
    decorator(func)

Version: 0.1
Author: slynxes
Date: 2019-01-15
"""
from datetime import datetime


def log(func):
    def wrapper(*args, **kw):
        print(f'call {func.__name__}')
        print(datetime.now())
        return func(*args, **kw)
    return wrapper


@log
def sum_num():
    pass


if __name__ == '__main__':
    sum_num()
