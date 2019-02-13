"""
requests 模块

Version: 0.1
Author: Slynxes
Date: 19-2-2
"""
import requests

# requests.get()
r = requests.get('http://www.baidu.com')
# 响应状态码
print(r.status_code)
# 响应的内容：字符串
print(r.text)
# 响应的内容：字节
print(r.content)
# 响应头部
print(r.headers)

# 带参数的请求
# url中带请求参数
r = requests.get('http://www.baidu.com', params={'username': 'zhubiao', 'passwd': '123'})
# 带请求头部
r = requests.get('http://www.baidu.com', headers={'Host': 'www.baidu.com'})

#  requests.post()
url = 'https://acounts.douban.com/login'
user_info = {'from_email': 'zhubiaook@outlook.com', 'password': 'Slynxes123'}
r = requests.post(url, data=user_info)