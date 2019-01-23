"""
try:
    pass
except EXCEPTION1:
    pass
except EXCEPTION2:
    pass
else:
    pass
finally:
    pass

        except与except, except与else之间是互斥关系，
        从上到下匹配，当匹配到第一个except,就不再匹配后面的except和else,
        finally是必执行语句。
        基于以上，当except之间是继承关系，且前面的except是后面except的父类，
        则子类except毫无意义，永远也不会执行，因为其错误被前面的父类except捕捉了。

        使用原则：子类except放到父类except前面，错误也就实现精确到模糊的匹配。

Version: 0.1
Author: slynxes
Date: 2019-01-21
"""
import logging


def except1():
    try:
        print('try:')
        1 / 0
    except ZeroDivisionError as e:
        print('except:')
        print(e)
    else:
        print('else')
    finally:
        print('finally')


def except2():
    """
    TypeError与ValueError不是继承关系，根据错误类型的不同而被这两个中的一个捕捉。
    :return:
    """
    try:
        print('try:')
        int('a')
        'a' / 3
    except TypeError as e:
        print('except: TypeError')
        print(e)
    except ValueError as e:
        print('except: ValueError')
        print(e)


def except3():
    """
    Exception是TypeError的父类，且Exception在TypeError的前面，TypeError永远捕捉不到错误。
    正确的做法是将父类Exception放到其子类后面。
    :return:
    """
    try:
        print('try:')
        'a' / 3
    except Exception as e:
        print('except: Exception')
        print(e)
    except TypeError as e:
        print('except: TypeError')
        print(e)


def foo():
    int('a')


def bar():
    foo()


def main():
    """
    被调用的函数错误，也能被当前except捕捉到
    :return:
    """
    try:
        bar()
    except ValueError as e:
        print('ValueError')
        print(e)


def next_main():
    main()


def err_logging():
    try:
        5 / 0
    except ZeroDivisionError as e:
        logging.exception(e)
    print('Error, but continue run...')


class TestError(ValueError):
    """
    自定义一个错误类
    """
    pass


def not_zero(s):
    """
    抛出错误
    :param s:
    :return:
    """
    if s == 0:
        raise TestError(f'{s} is a illegal value.')


def test_error():
    """
    except自定义的错误类
    :return:
    """
    try:
        print('try')
        not_zero(0)
    except TestError as e:
        print('except')
        print(e)


if __name__ == '__main__':
    test_error()

