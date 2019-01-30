"""
Description
http://werkzeug.pocoo.org/docs/0.14/tutorial/#introducing-shortly

Version: 0.1
Author: slynxes
Date: 2019-01-30
"""
import os
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


class Shortly(object):
    def __init__(self, config):
        self.redis = redis.Redis(config['192.168.0.201'], config['6379'])

    def dispatch_request(self, request):
        return Response('Hello World')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def application(environ, start_response):
    response = Response('Hello World!', mimetype='text/plain')
    return response(environ, start_response)

