"""
模块导入
    导入过程：
        1. 根据搜索路径查找模块文件
        2. 将需导入的模块文件编译成.pyc的字节码文件，保存于模块所在路径下的__pycache__目录下。
    绝对导入：
        导入整个模块
            import module
            import module as ALALIS_MODULE
        导入模块中的方法、类
            from module import NAME1, NAME2, ...
            from module import NAME1 as ALAIS_NAME1, NAME2 as ALALS_NAME2, ...
            from module import *
    相对导入
        from . import module
        from .module import NAME1,
模块搜索路径
    1. 程序主目录
        项目根目录下
    2. 系统环境变量PYTHONPATH
    3. 标准库目录
        Python安装目录下的Lib目录下
    4. 第三方库site-packages目录下
        Python安装目录下的Lib/site-packages 或项目目录下的/venv/Lib/site-packages
模块属性
    __doc__: 模块帮助文档，模块最前面的注释语句
    __file__: 模块文件系统上的路径
    __name__: 模块的名称，当前模块为程序入口时为'__main__'，否则为package.module
    __package__: 模块所在的包名
    __cached__: 模块字节码缓存的路径

Version: 0.1
Author: slynxes
Date: 2019-01-23
"""
# 导入整个模块
import module_examples.m1 as m1

# 导入模块中的部分类或函数
from module_examples.m2 import Student as m2stu


if __name__ == '__main__':
    print(__name__)
    print(m1.__name__)