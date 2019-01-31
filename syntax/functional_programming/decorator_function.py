"""
装饰器(decorator)
    装饰器是一个函数，是一个返回函数的高阶函数
    @decorator
    def func
        ...
    等同于
    func = decorator(func)

    @decorator(args)
    def func
        ...
    等同于
    func = decorator(args)(func)

Version: 0.1
Author: slynxes
Date: 2019-01-15
"""
from datetime import datetime


def log(func):
    def wrapper(name):
        print(f'wrapper_name = {name}')
        print(datetime.now())
        name = name + 'func'
        return func(name)
    return wrapper


@log
def sum_num(name):
    print(f'sum_num: {name}')
    return 100


def decorator_f(func):
    def inter(name):
        name = name + ' good'
        return func(name)
    return inter


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(text)
            return func()
        return wrapper
    return decorator


@log('execute')
def now():
    print('2018-10-11')


if __name__ == '__main__':
    a = sum_num('good')
    print(a)

    now()
