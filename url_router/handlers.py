
class BaseHandler(object):
    def __init__(self, request=None, response=None):
        self.request = request
        self.response = response

    def __call__(self, request, response):
        self.request = request
        self.response = response
        action = request.method.lower()
        try:
            method = getattr(self, action)
        except AttributeError:
            raise AttributeError("No action for {}".format(action))
        method(**request.urlvars)

class DogHandler(BaseHandler):
    def get(self, id=None):
        self.response.write("<h1>This is the dog handler for id {}</h1>".format(id))

class CatHandler(BaseHandler):
    def get(self):
        self.response.write("<h1>This is the cat handler</h1>")