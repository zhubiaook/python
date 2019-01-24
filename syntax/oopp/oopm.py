"""
属性和方法的访问权限
    属性访问权限
        name : 可见
        _name : 隐藏，但仍然可以被访问
        __name : 隐藏，不可以访问
        __name__ : 可见，特殊用途

限定实例可使用的属性：__slots__
    Python是动态语言，动态语言允许我们在程序运行时绑定新的属性和方法，
    但我们可以使用__slots__来禁止实例绑定新的属性，限制实例可以访问的属性,
    但类属性并没有受到限制。
        __slots__ = 'NAME1', 'NAME2', ...

类属性和实例属性
    类属性：
        定义在类中，所有方法外
        访问：class_name.variable
    实例属性：
        定义在类方法中，默认在__init__方法中

类方法，静态方法，实例方法
    类方法
        @classmethod
        def func_name(cls):
            pass
    静态方法: 静态方法中不能出现self, 不然就变成实例方法了
        @staticmethod
        def func_name():
            pass
    实例方法: 实例方法中一定要用到self，不然其与静态方法有什么区别呢？
        def func_name(self):
            pass

特殊函数
    # 构造函数
    def __init__(self):
        pass

    # 实例在控制台上的输出
    def __repr__(self):
        return 'String'

    # 实例打印的输出
    def __str__(self):
        return 'String'

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""


class Student(object):
    gender = 'F'

    __slots__ = '_name', '_score', '_age', '_id'

    def __init__(self, name, score, age):
        """
        构造方法
        :param name:
        :param score:
        :param age:
        """
        self._name = name
        self._score = score
        self._age = age
        self._id = 0

    def __repr__(self):
        """
        实例在控制台上的输出
        :return:
        """
        return f'__repr__: {self.__class__.__module__}.{self.__class__.__qualname__}'

    def __str__(self):
        """
        print(实例)的输出
        :return:
        """
        # self.__class__.__module__ : 当前实例的类的模块名称
        # self.__class__.__qualname__ : 当前实例的类名称
        return f'__str__: {self.__class__.__module__}.{self.__class__.__qualname__}'

    def print_score(self):
        print(f'name = {self._name}, score = {self._score}, age = {self._age}')

    @property
    def scores(self):
        return self._score

    @scores.setter
    def scores(self, score):
        self._score = score

    @staticmethod
    def say_hello():
        """
        静态方法
        :return:
        """
        print('Hello World!')

    @classmethod
    def cm(cls):
        """
        类方法
        :return:
        """
        pass
