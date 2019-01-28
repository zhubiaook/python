"""
类的组成
    f, filed: 字段， 包括类字段，实例字段
    p, property: 实例属性
    m, method: 方法, 包括类方法，实例方法

字段和方法的访问权限
    字段访问权限
        name : 可见
        _name : 隐藏，但仍然可以被访问
        __name : 隐藏，不可以访问
        __name__ : 可见，特殊用途


类字段, 实例字段
    类字段：
        说明：
            与类相关的字段，是类成员
            定义在类中，所有方法外
        访问：
            class_name.variable, inst_name.variable
    实例字段：
        说明：
            与实例相关的字段，是实例成员
            定义在类方法中，默认在__init__方法中，不能使用类名访问实例字段
        访问：
            inst_name.variable

类方法，静态方法，实例方法
    类方法
        说明：
            类方法是与类有关系，与实例无关的方法， 类与实例都可以调用它，
            实例调用它，并不会体现出实例的特性，还是体现类的特性
        定义：
            @classmethod
            def func_name(cls):
                pass
        调用：
            class_name.func_name()
            inst_name.func_name()
    静态方法:
        说明：
            静态方法与类和实例均没有关系，只是通过类的方式将函数组织在一起而已
            静态方法中不能出现self, 不然就变成实例方法了
            类与实例都可以调用静态方法
        定义：
            @staticmethod
            def func_name():
                pass
        调用：
            class_name.func_name()
            inst_name.func_name()
    实例方法:
        说明：
            实例方法是与实例相关，与类无关的方法
            实例方法中一定要用到self，不然其与静态方法有什么区别呢？
            用实例调用实例方法，但也可以用类名模拟调用实例方法，其本质还是实例调用
        定义：
            def func_name(self):
                pass
        调用：
            inst_name.func_name()
            class_name.func_name(inst_name)

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

特殊字段
    __slots__
        类字段__slots__ 用于限定实例可使用的属性
        Python是动态语言，动态语言允许我们在程序运行时绑定新的属性和方法，
        但我们可以使用__slots__来禁止实例绑定新的属性，限制实例可以访问的属性,
        但类属性并没有受到限制。
        __slots__ = ('NAME1', 'NAME2', ...)

cls, self
    cls: 代表当前类本身
    self: 代表实例本身

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""
from datetime import datetime


class Student(object):
    # 类字段
    count = 0
    __slots__ = '_name', '_score', '_birthday', '_id'

    def __init__(self, name, score, birthday):
        """
        构造方法
        :param name:
        :param score:
        :param age:
        """
        self._name = name
        self._score = score
        self._birthday = birthday
        self._id = 0
        Student.count += 1

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

    def __add__(self, other):
        """
        实例相加
        :param other:
        :return:
        """
        return self._score + other.scores

    def print_score(self):
        print(f'name = {self._name}, score = {self._score}, age = {self._age}')

    @property
    def scores(self):
        """属性读取"""
        return self._score

    @scores.setter
    def scores(self, score):
        """属性赋值"""
        self._score = score

    @property
    def age(self):
        birthday_date = datetime.strptime(self._birthday, '%Y-%m-%d')
        return datetime.now().year - birthday_date.year

    @staticmethod
    def static_m():
        """
        静态方法
        :return:
        """
        print('Hello World!')

    @classmethod
    def class_m(cls):
        """
        类方法
        :return:
        """
        print(f'students count is: {cls.count}')


class Sportsman(object):
    pass


class HighSchoolStudent(Student):
    __slots__ = Student.__slots__ + ('_course', )
    pass


class CollegeStudent(Student):
    __slots__ = Student.__slots__ + ('_computer', '_physical')
    pass


class SecondClassStudent(HighSchoolStudent, Sportsman):
    __slots__ = HighSchoolStudent.__slots__ + CollegeStudent.__slots__
    pass
