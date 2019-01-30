"""
socket编程

Version: 0.1
Author: slynxes
Date: 2019-01-30
"""
import socket
import re
import threading
import time
# AF: Address Family
# PF: Protocol Family
# INET: IPv4, INET6: IPv6
# SOCK_STREAM: TCP协议
# SOCK_DGRAM: UDP协议


def client_program(url, port):
    """
    socket编程，实现请求网页
    :param url:
    :param port:
    :return:
    """
    url_g = re.match(r'(^[^/]*)(.*$)', url)
    host = url_g[1]
    path = url_g[2]
    request = b'GET ' + bytes(path, 'utf-8') + b' HTTP/1.1\r\nHost: ' \
              + bytes(host, 'utf-8') + b'\r\nConnection: close\r\n\r\n'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)

    "接收数据"
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    return data


def server_program():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 80))
    s.listen(5)
    print('Waiting for connection...')

    def tcplink(sock, addr):
        print(f'Accept new connection from {addr[0]}:{addr[1]}...')
        sock.send(b'Welcome!')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            sock.send(b'data..data...')
        sock.close()
        print(f'Connection from {addr[0]}:{addr[1]} closed')

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == '__main__':
    content = client_program('192.168.0.201/html/nice/index.html', 80)
    print(content)

