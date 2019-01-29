"""
序列化
1. pickle
    该模块可将内存对象序列化后保存文件中，也可以从磁盘中读取文件反序列化为对象
2. json
    与其它语言交互，需要把对象序列化为json格式


Version: 0.1
Author: slynxes
Date: 2019-01-29
"""
import pickle
import json
import datetime

path = 'C:\\Users\\alandi\\Desktop\\test\\1.txt'
d = {'name': 'zhubiao', 'age': 20, 'score': 100}
# pickle 序列化
# 序列化为字节后，再保存于文件中
b = pickle.dumps(d)
with open(path, 'wb') as f:
    f.write(b)

# 同时完成序列化和保存
with open(path, 'wb') as f:
    pickle.dump(d, f)

# pickle 反序列化
# 读取文件后再反序列化
with open(path, 'rb') as f:
    r = f.read()
    pickle.loads(r)

# 同时完成读取文件和反序列化
with open(path, 'rb') as f:
    pickle.load(f)

path = 'C:\\Users\\alandi\\Desktop\\test\\2.txt'
# json 序列化
# 序列化为字节后，再保存于文件中
j = json.dumps(d)
with open(path, 'w') as f:
    f.write(j)

# 同时完成序列化和保存
with open(path, 'w') as f:
    json.dump(d, f)

# json 反序列化
# 读取文件后再反序列化
with open(path, 'r') as f:
    r = f.read()
    json.loads(r)

# 同时完成读取文件和反序列化
with open(path, 'r') as f:
    json.load(f)


# 对实例进行序列化
class Student(object):
    """
    测试类
    """
    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def score(self):
        return self._score


def student2dict(std):
    """
    实例转为字典类型
    :param std:
    :return:
    """
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 使用自定义的方法将实例转化为字典
s = Student('zhubiao', 20, 100)
json.dumps(s, default=student2dict)

# 使用内建字段__dict__将实例转化为字典类型
# 但是并不是所有的类都有__dict__字段
json.dumps(s, default=lambda obj: obj.__dict__)
