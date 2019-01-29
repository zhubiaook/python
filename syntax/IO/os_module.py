"""
调用os和os.path模块操作文件或目录


Version: 0.1
Author: slynxes
Date: 2019-01-29
"""
import os


# 操作系统类型
# posix: Linux, Unix, MacOS
# nt: Windows
os_type = os.name

# 操作系统详细信息
# windows上不提供该函数
os_info = os.uname()


# 环境变量
os_environ = os.environ
# 获取PATH
os_PATH = os.environ.get('PATH')


# 合并路径
part1 = 'C:\\Users\\alandi'
part2 = 'Desktop\\test'
os.path.join(part1, part2)
# 拆分路径
os.path.split(part1)


# 创建、删除文件夹
os.mkdir('C:\\Users\\alanid\\Desktop\\test')
os.rmdir('C:\\Users\\alanid\\Desktop\\test')

# 重命名文件
os.rename('FILE1', 'FILE2')
# 删除文件
os.remove('FILE1')

# 列出文件
os.listdir('PATH')

# 判断是否是文件
os.path.isdir('PATH')
os.path.isfile('PATH')
os.path.islink('PATH')






