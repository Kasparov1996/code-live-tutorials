from string import Template
import config
import os

class BaseHandler(object):
    def __init__(self):
        self.request = None
        self.response = None

    def render(self, filename, **context):
        filepath = os.path.join(config.TEMPLATE_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                contents = f.read()
            s = Template(contents)
            return s.substitute(**context)

    def __call__(self, request, response):
        self.request = request
        self.response = response
        action = request.method.lower()
        try:
            method = getattr(self, action)
        except AttributeError:
            raise AttributeError("No action for {}".format(action))
        method(**request.urlvars)