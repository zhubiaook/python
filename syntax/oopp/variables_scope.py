"""
变量作用域
    全局变量
        定义在模块内，所有类和方法外
    类属性/类变量
        定义在类中，所有方法外
    实例属性/实例变量
        定义在实例方法中，默认定义在__init__方法中，
        形如self.variable
    局部变量
        定义在方法中的变量

Version: 0.1
Author: slynxes
Date: 2019-01-24
"""

# 全局变量
var1 = 'Global variable'


def func1():
    pass


class Student(object, name):
    # 类属性
    var2 = 'Class variables'

    def __init__(self, name):
        # 实例属性
        self._var3 = name

    def print_score(self):
        # 局部变量
        var4 = 100
        print(self._var3, var4)

