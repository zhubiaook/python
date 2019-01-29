"""
Description

Version: 0.1
Author: slynxes
Date: 2019-01-29
"""
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, World!</h1>']


httpd = make_server('', 8000, application)
print('Server Http on port 8000...')
httpd.serve_forever()
