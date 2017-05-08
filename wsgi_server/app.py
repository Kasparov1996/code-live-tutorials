from webob import Request, Response

def dog_handler(request, response):
    response.write('<img src="http://cdn2-www.dogtime.com/assets/uploads/gallery/30-impossibly-cute-puppies/impossibly-cute-puppy-8.jpg">')

def cat_handler(request, response):
    response.write('<img src="http://cdn3-www.cattime.com/assets/uploads/2011/08/best-kitten-names-1.jpg">')

class WSGIApplication(object):
    def __init__(self):
        self.routes = []

    def handle(self, path, handler):
        self.routes.append((path, handler))

    def dispatch(self, request):
        for route in self.routes:
            if route[0] == request['PATH_INFO']:
                return route[1]
        return None

    def not_found(self, request, response):
        response.status = 404
        response.write("404 Not Found")

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response()
        handler = self.dispatch(environ)
        if handler:
            handler(request, response)
        else:
            self.not_found(request, response)
        return response(environ, start_response)


app = WSGIApplication()

app.handle('/dog', dog_handler)
app.handle('/cat', cat_handler)