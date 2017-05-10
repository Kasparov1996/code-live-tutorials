from handlers.base_handler import BaseHandler

class CatHandler(BaseHandler):
    def get(self):
        self.response.write("<h1>This is the cat handler</h1>")