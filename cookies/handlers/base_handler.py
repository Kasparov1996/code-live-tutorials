import os
import config
from jinja2 import Environment, FileSystemLoader

jinja2_env = Environment(loader=FileSystemLoader(
    config.TEMPLATE_DIRS), autoescape=True)


class BaseHandler(object):
    def __init__(self):
        self.request = None
        self.response = None

    def write(self, text):
        self.response.write(text)

    def redirect(self, url, status=301):
        self.response.status = status
        self.response.location = url

    def render(self, filename, **context):
        template = jinja2_env.get_template(filename)
        self.write(template.render(**context))

    def __call__(self, request, response):
        self.request = request
        self.response = response
        self.response.cache_control.no_cache = True
        action = request.method.lower()
        try:
            method = getattr(self, action)
        except AttributeError:
            raise AttributeError("No action for {}".format(action))
        method(**request.urlvars)