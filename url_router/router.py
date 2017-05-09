from webob import Request, Response
import re

def not_found(request, response):
    response.status = 404
    response.write("404 Not Found")

class Route(object):
    default_methods = ['GET']
    def __init__(self, path, handler, methods=None):
        self.path = path
        self.handler = handler

        if methods is None:
            self.methods = self.default_methods
        else:
            self.methods = methods
        self.urlvars = {}

    def match(self, request):
        regex = re.compile(self.path)
        match = regex.match(request.path)
        if match and request.method in self.methods:
            self.urlvars.update(match.groupdict())
            return True
        return False


class Router(object):
    def __init__(self):
        self.routes = []

    def handle(self, url, handler, *args, **kwargs):
        if not url.startswith("^"):
            url = "^" + url
        if not url.endswith("$"):
            url += "$"
        route = Route(path=url, handler=handler, *args, **kwargs)
        self.routes.append(route)

    def match(self, request):
        for route in self.routes:
            if route.match(request):
                request.urlvars = route.urlvars
                return route.handler
        return None

    def dispatch(self, request):
        handler = self.match(request)
        return handler

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response()
        handler = self.dispatch(request)
        if handler:
            handler()(request, response)
        else:
            not_found(request, response)
        return response(environ, start_response)