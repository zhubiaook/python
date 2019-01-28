"""
文件读写

Version: 0.1
Author: slynxes
Date: 2019-01-28
"""

path = 'C:\\Users\\alandi\\Desktop\\test\\1.txt'

"""
Read File
"""
# read()        读取文件所有内容, 返回一个字符串
# readline()    一行一行的读取文件, 返回字符串
# readlines()   读取文件所有内容, 返回一个列表，列表的每个元素是一行字符串
#    'r'       open for reading (default)
#    'w'       open for writing, truncating the file first
#    'x'       create a new file and open it for writing
#    'a'       open for writing, appending to the end of the file if it exists
#    'b'       binary mode
#    't'       text mode (default)
#    '+'       open a disk file for updating (reading and writing)
#    'U'       universal newline mode (deprecated)
# rb: 读取二进制文件
with open(path, 'r', encoding='utf8') as f:
    print(f.read())

"""
Write File
"""
# write: 写入文件
# writeline: 将列表合并为数据流写入
# 'w': 覆盖已有的文件
# 'a': 追加到文件末尾
# 'wb', 'ab': 写入二进制文件
with open(path, 'w', encoding='utf8') as f:
    f.writelines(['Good New Year', 'nice'])



